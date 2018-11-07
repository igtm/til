# Solution

1.pi.yaml to create the job is:

```
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```

After it completes, you'll execute a kubectl logs pi > pi.result.txt

2.nginx-pod.yaml

```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: 
      image: nginx
      ports:
        containerPort: 80
```

3.nginx-deployment.yaml:

```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 
  template:
    metadata:
      labels:
        app: nginx
        tier: frontend
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

4.with-files.yaml:

```
apiVersion: v1
kind: Pod
metadata:
  name: with-files
spec:
  containers:
  - image: nginx
    name: write-files
    volumeMounts:
    - mountPath: /tmp
      name: temp-volume
  volumes:
  - name: temp-volume
    emptyDir: {}
```

5.kubectl label node node-name rack=qa

6.Use kubectl logs counter > count.result.txt

7.web-dep.yaml:

```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: web-dep
  annotations:
    AppVersion: "3.4"
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2 
  template:
    metadata:
      labels:
        app: nginx
        tier: frontend
    spec:
      securityContext:
        runAsUser: 1000
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
        command: ["sleep","1000"]
```

8.kubectl set image deployment web-dep nginx=1.9

9.kubectl rollout undo deployment web-dep

10.kubectl scale deployment web-dep --replicas=3

11.kubectl expose deployment web-dep --type=NodePort --containerPort 80

12.ds.yaml

```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: zuul
spec:
  selector:
    matchLabels:
      quiet: "pod"
  template:
    metadata:
      labels:
        quiet: pod
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      containers:
      - name: gozer
        image: k8s.gcr.io/pause:2.0
```

13.kube-dns.yaml:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: kube-dns
  namespace: kube-system
data:
  upstreamNameservers: |
    ["8.8.8.8", "8.8.4.4"]

Using new (1.10+) CoreDNS Corefile would be:

.:53 {
        errors
        health
        kubernetes cluster.local  in-addr.arpa ip6.arpa {
           upstream  8.8.8.8 8.8.4.4
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
        }
        prometheus :9153
        proxy .  8.8.8.8 8.8.4.4
        cache 30
    }
```

14.zork.yaml:

```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: zork
  namespace: default
spec:
  selector:
    matchLabels:
      app: zork-app
  template:
    metadata:
      labels:
        app: zork-app
    spec:
      containers:
      - name: p114
        image: k8s.gcr.io/pause:2.0
        env:
        - name: FROBOZZ
          value: "web-dep.default"
```

15.spy.yaml:

```
apiVersion: v1
kind: Pod
metadata:
  name: spy
spec:
  tolerations:
  - key: node-role.kubernetes.io/master
    effect: NoSchedule
  containers:
  - name: sneak
    image: k8s.gcr.io/pause:20
```

16.The Kubernetes logs are located in /var/log/pods/

17.kubtctl exec -it counter2 -- cat /var/www/countlog > ~/home/logs/countlog

18.net-policy.yaml

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```
 
19.kubectl taint node master-node-name node-role.kubernetes.io/master-

20.my-secret.yaml:

```
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  username: YWRtaW4=
  password: aUhlYXJ0S2l0dGVucw==
```

Don't forget to run your secrets through base64!