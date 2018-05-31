# 俺用リファレンス

## UICollectionView(コレクション)

#### レイアウト全般

- http://techlife.cookpad.com/entry/2017/06/29/190000

#### 行数設定

- https://stackoverflow.com/a/41409642

#### Self-Sizing

- https://qiita.com/usagimaru/items/e0a4c449d4cdf341e152


## UITabView(タブ)

```swift
import UIKit

class MainTabBarViewController: UITabBarController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
        let first = ViewController()
        let second = SecondViewController()

        first.tabBarItem = UITabBarItem(tabBarSystemItem: UITabBarSystemItem.featured, tag: 1)
        second.tabBarItem = UITabBarItem(tabBarSystemItem: UITabBarSystemItem.featured, tag: 2)

        let myTabs = [first, second]

        self.setViewControllers(myTabs, animated: false)
    }

}


```