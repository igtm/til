# iOS Swift3勉強
- Umedy動画勉強
- https://www.udemy.com/best-ios-10-swift-3-xcode-8-course


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
