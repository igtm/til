# iOS Swift3勉強
- Umedy動画勉強
- https://www.udemy.com/best-ios-10-swift-3-xcode-8-course

### ラベル
- 「⌘ +」で ラベルの幅を自動フィット

### ボタン
- Tag: 複数ボタン=１つのメソッド の場合、どのボタンが押されてきたかを検知できるようにするためのもの。`sender.tag`

### ImageView
- Assets.xcasestsに入れた画像を使える


### 座学
##### pt と pixel の違い
- pt:  1 / 72 inch
- 1x: 1pt = 1pixel
- 2x: 1pt = 4pixel
- 3x: 1pt = 9pixel


### CocoaPods使い方
- `sudo gem install cocoapods`
- `pod init`: Podfile新規作成

```
platform :ios, '9.0'


target 'Clima' do
  # Comment the next line if you're not using Swift and don't want to use dynamic frameworks
  use_frameworks!


  # Pods for Clima

  pod 'SwiftyJSON'
  pod 'Alamofire'
  pod 'SVProgressHUD'
  
end
```
- `pod install`: Podfileに書いてある pod からインストール
- `pod update`: アップデート
- `Hoge.xcworkspace` が出来る。 `.xcodeproj` ではなく `.xcworkspace` にcocoapodsが入っているので以降はコチラを開く


### CoreLocation 位置情報取得


- ViewController

```
import UIKit
import CoreLocation


class WeatherViewController: UIViewController, CLLocationManagerDelegate {
    
    //Constants
    let WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"
    let APP_ID = "894417bd55cdd22c9093cd7e889a8648"
    

    //TODO: Declare instance variables here
    let locationManager = CLLocationManager()
    

    
    //Pre-linked IBOutlets
    @IBOutlet weak var weatherIcon: UIImageView!
    @IBOutlet weak var cityLabel: UILabel!
    @IBOutlet weak var temperatureLabel: UILabel!

    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        //TODO:Set up the location manager here.
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyHundredMeters
        locationManager.requestWhenInUseAuthorization()
    
        
        
    }
}
```

- info.plist

```
Privacy - Location Usage Description
Privacy - Location When In Use Usage Description
天気予報情報を取得するために位置情報の取得をおこないます
```


### Segue セグエ
##### 新しいViewController作成
- 右下からViewController を引っ張ってきて作成
- New File
- Source > Cocoa Touch Class を選び Next
- Class名を入力し、Subclassを `UIViewController` にして作成

##### セグエの作り方２つ
1. **要素** から次のViewControllerへ ctrl + 引っ張って離す
2. **上部黄色のViewConroller** から次のViewControllerへ ctrl + 引っ張って離す

- ViewController同士のセグエの場合は、要素個別のアクション時に`performSegue`を呼び出して、指定のセグエを使って画面遷移する必要がある。
- 画面遷移時、値を渡したい時は `prepare` を使う。
- performSegue() -> prepare() ---> SecoundViewController.viewDidLoad()
- セグエのIdentifier に `goToSecoundScreen` と設定した場合以下のようになる

```
    @IBAction func buttonPressed(_ sender: Any) {
        // 画面遷移
        performSegue(withIdentifier: "goToSecoundScreen", sender: self)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "goToSecoundScreen" {
            // segue.destination は UIViewControllerなので segue.indentifier が goToSecoundScreenの時は 絶対 SecoundViewController なので キャストして扱う。
            let destinationVC = segue.destination as! SecoundViewController
            // 遷移先ViewControllerのパラメータをいじる。
            destinationVC.textPassedOver = textField.text!
        }
    }

```
- [参考](http://qiita.com/treastrain/items/8c298886cc8f3cf124f2)

##### 画面戻るときに値を渡したい時
- Delegate Patternを使う
- 単純に protocol（interface）を定義し、遷移元クラスはそれを実装しておく。遷移先クラスに遷移元インスタンスを入れておくプロパティを定義。`prepare` メソッド実行時に、遷移先クラスに `self` を渡す。遷移元に値を渡す時は、そのprotocolに定義したメソッドを呼び出して値を渡す。

- WeatherViewController

```
class WeatherViewController: UIViewController, ChangeCityDelegate {

    //Write the userEnteredANewCityName Delegate method here:
    func userEnteredANewCityName(city : String) {
        print(city)
    }

    
    //Write the PrepareForSegue Method here
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        if segue.identifier == "changeCityName" {
            let destinationVC = segue.destination as! ChangeCityViewController
            
            destinationVC.delegate = self
        }
    }
}
```
- ChangeCityViewController

```
//Write the protocol declaration here:
protocol ChangeCityDelegate {
    func userEnteredANewCityName(city: String)
}


class ChangeCityViewController: UIViewController {
    
    //Declare the delegate variable here:
    var delegate : ChangeCityDelegate?
    
    //This is the pre-linked IBOutlets to the text field:
    @IBOutlet weak var changeCityTextField: UITextField!

    
    //This is the IBAction that gets called when the user taps on the "Get Weather" button:
    @IBAction func getWeatherPressed(_ sender: AnyObject) {
        
        //1 Get the city name the user entered in the text field
        let cityName = changeCityTextField.text!
        
        //2 If we have a delegate set, call the method userEnteredANewCityName
        // ? => Optional Chaining
        // あれば実行、なければ実行しない。
        delegate?.userEnteredANewCityName(city: cityName)
        
        //3 dismiss the Change City View Controller to go back to the WeatherViewController
        self.dismiss(animated: true, completion: nil)
        
    }
    
    @IBAction func backButtonPressed(_ sender: AnyObject) {
        self.dismiss(animated: true, completion: nil)
    }
    
}
```