# GoDDD Code Reading


- Routing -> Handler( Context, Service, Logger ) [github](https://github.com/marcusolsson/goddd/blob/master/main.go#L171)

```
httpLogger := log.NewContext(logger).With("component", "http")

	mux := http.NewServeMux()

	mux.Handle("/booking/v1/", booking.MakeHandler(ctx, bs, httpLogger))
	mux.Handle("/tracking/v1/", tracking.MakeHandler(ctx, ts, httpLogger))
	mux.Handle("/handling/v1/", handling.MakeHandler(ctx, hs, httpLogger))
```
- booking/transport.go

```
// MakeHandler returns a handler for the booking service.
func MakeHandler(ctx context.Context, bs Service, logger kitlog.Logger) http.Handler {
	opts := []kithttp.ServerOption{
		kithttp.ServerErrorLogger(logger),
		kithttp.ServerErrorEncoder(encodeError),
	}

	bookCargoHandler := kithttp.NewServer(
		ctx,
		makeBookCargoEndpoint(bs),
		decodeBookCargoRequest,
		encodeResponse,
		opts...,
	)
	loadCargoHandler := kithttp.NewServer(
		ctx,
		makeLoadCargoEndpoint(bs),
		decodeLoadCargoRequest,
		encodeResponse,
		opts...,
	)
	requestRoutesHandler := kithttp.NewServer(
		ctx,
		makeRequestRoutesEndpoint(bs),
		decodeRequestRoutesRequest,
		encodeResponse,
		opts...,
	)
	assignToRouteHandler := kithttp.NewServer(
		ctx,
		makeAssignToRouteEndpoint(bs),
		decodeAssignToRouteRequest,
		encodeResponse,
		opts...,
	)
	changeDestinationHandler := kithttp.NewServer(
		ctx,
		makeChangeDestinationEndpoint(bs),
		decodeChangeDestinationRequest,
		encodeResponse,
		opts...,
	)
	listCargosHandler := kithttp.NewServer(
		ctx,
		makeListCargosEndpoint(bs),
		decodeListCargosRequest,
		encodeResponse,
		opts...,
	)
	listLocationsHandler := kithttp.NewServer(
		ctx,
		makeListLocationsEndpoint(bs),
		decodeListLocationsRequest,
		encodeResponse,
		opts...,
	)

	r := mux.NewRouter()

	r.Handle("/booking/v1/cargos", bookCargoHandler).Methods("POST")
	r.Handle("/booking/v1/cargos", listCargosHandler).Methods("GET")
	r.Handle("/booking/v1/cargos/{id}", loadCargoHandler).Methods("GET")
	r.Handle("/booking/v1/cargos/{id}/request_routes", requestRoutesHandler).Methods("GET")
	r.Handle("/booking/v1/cargos/{id}/assign_to_route", assignToRouteHandler).Methods("POST")
	r.Handle("/booking/v1/cargos/{id}/change_destination", changeDestinationHandler).Methods("POST")
	r.Handle("/booking/v1/locations", listLocationsHandler).Methods("GET")
	r.Handle("/booking/v1/docs", http.StripPrefix("/booking/v1/docs", http.FileServer(http.Dir("booking/docs"))))

	return r
}
```


- Cargo [github](https://github.com/marcusolsson/goddd/blob/master/cargo/cargo.go)

```
[Entity]
// Cargo is the central class in the domain model.
type Cargo struct {
	TrackingID         TrackingID
	Origin             location.UNLocode
	RouteSpecification RouteSpecification
	Itinerary          Itinerary
	Delivery           Delivery
}
```
```
[Value Object]
// TrackingID uniquely identifies a particular cargo.
type TrackingID string

...

// NextTrackingID generates a new tracking ID.
func NextTrackingID() TrackingID {
	return TrackingID(strings.Split(strings.ToUpper(uuid.New()), "-")[0])
}
```
```
[Repository]
// Repository provides access a cargo store.
type Repository interface {
	Store(cargo *Cargo) error
	Find(id TrackingID) (*Cargo, error)
	FindAll() []*Cargo
}
...

// Repositoryは 
// mongo使うパターン: mongo.go
// inmem使うパターン: inmem.goの中にすべて入っている
// mongoのセッションは DIとして渡される。
mongo.cargoRepository
type cargoRepository struct {
	db      string
	session *mgo.Session
}
// NewCargoRepository returns a new instance of a MongoDB cargo repository.
func NewCargoRepository(db string, session *mgo.Session) (cargo.Repository, error) {
	...
}
```

#### Service （重ねて使ってる）
- booking.service [github](https://github.com/marcusolsson/goddd/blob/master/booking/service.go#L44)

```
[Service]
type service struct {
	cargos         cargo.Repository
	locations      location.Repository
	handlingEvents cargo.HandlingEventRepository
	routingService routing.Service
}
```

- loggingService [github](https://github.com/marcusolsson/goddd/blob/master/booking/logging.go#L12) [Youtube](https://youtu.be/aL6sd4d4hxk?t=30m22s)

```
type loggingService struct {
	logger log.Logger
	Service
}

// オブジェクト指向で言うオーバーライドしてる感じ。
func (s *loggingService) BookNewCargo(origin location.UNLocode, destination location.UNLocode, deadline time.Time) (id cargo.TrackingID, err error) {
	defer func(begin time.Time) {
		s.logger.Log(
			"method", "book",
			"origin", origin,
			"destination", destination,
			"arrival_deadline", deadline,
			"took", time.Since(begin),
			"err", err,
		)
	}(time.Now())
	return s.Service.BookNewCargo(origin, destination, deadline)
}
```
- booking.instrumentingService

```
type instrumentingService struct {
	requestCount   metrics.Counter
	requestLatency metrics.Histogram
	Service
}

// オブジェクト指向で言うオーバーライドしてる感じ。
func (s *instrumentingService) BookNewCargo(origin, destination location.UNLocode, deadline time.Time) (cargo.TrackingID, error) {
	defer func(begin time.Time) {
		s.requestCount.With("method", "book").Add(1)
		s.requestLatency.With("method", "book").Observe(time.Since(begin).Seconds())
	}(time.Now())

	return s.Service.BookNewCargo(origin, destination, deadline)
}
```

- main.go

```
// どんどん上書いていってる。結果、LoggingとInstrumentができるServiceが出来上がる。
	var bs booking.Service
	bs = booking.NewService(cargos, locations, handlingEvents, rs)
	bs = booking.NewLoggingService(log.NewContext(logger).With("component", "booking"), bs)
	bs = booking.NewInstrumentingService(
		kitprometheus.NewCounterFrom(stdprometheus.CounterOpts{
			Namespace: "api",
			Subsystem: "booking_service",
			Name:      "request_count",
			Help:      "Number of requests received.",
		}, fieldKeys),
		kitprometheus.NewSummaryFrom(stdprometheus.SummaryOpts{
			Namespace: "api",
			Subsystem: "booking_service",
			Name:      "request_latency_microseconds",
			Help:      "Total duration of requests in microseconds.",
		}, fieldKeys),
		bs,
	)
```