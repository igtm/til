# 脱WebStorage! ハイブリッドアプリのデータ永続化(PouchDBでSQLite on Ionic)
### はじめに
[ここ](http://gonehybrid.com/dont-assume-localstorage-will-always-work-in-your-hybrid-app/)で行ってるように、ハイブリッドアプリでlocalstorageを使うのはよろしくない。
なのでSQLiteを使う。
慣れ親しんだJSONで扱える[PouchDB](http://pouchdb.com/)がよさ気なので使ってみた。

### 基本チュートリアル(これが１番わかりやすい)
- [ionic+PouchDB+SQLite](http://gonehybrid.com/how-to-use-pouchdb-sqlite-for-local-storage-in-your-ionic-app/)


### 補足
- [テーブルは`type`プロパティで表現](http://stackoverflow.com/questions/30066753/pouchdb-structure)
- DB保存場所:`/Users/[username]/Library/Developer/CoreSimulator/Devices/[id]/data/Containers/Data/Application/[id]/Documents`
- 全件取得:`DB.allDocs({ include_docs: true, attachments: true })`

``` 例)DB.allDocsの返却値
{"total_rows":253,
"offset":0,
"rows":[
	{"id":"000C105E-A22C-F4EA-A184-85C22E979B99",
	"key":"000C105E-A22C-F4EA-A184-85C22E979B99",
	"value":{"rev":"1-cc517b7f911eedde487b9a0bf4e520fb"},
	"doc":{"id":68,
			"name":"test",
			"age":25,
			"type":"users",
			"_id":"000C105E-A22C-F4EA-A184-85C22E979B99",
			"_rev":"1-cc517b7f911eedde487b9a0bf4e520fb"
			}
	},..
```
- DBに変更があるごとに`_rev`が変わるので変更した後帰ってくる`rev`を`_rev`に入れなおす必要あり。


### パフォーマンス(on iOS Simulator)
SQLiteは遅いらしいので計測

``` 全件削除(81rows)
// 397ms かかった
function removeAll(){
            var data = [];
            return $q.when(_db.allDocs({
                include_docs: true,
                attachments: true
            })).then(function(res){
                var rows = res.rows;
                for(var i=0;i<rows.length;i++){
                    var doc = rows[i].doc;
                    doc._deleted = true;
                    data.push(doc);
                }
                return $q.when(_db.bulkDocs(data));
            });
        }
```
確かにlocalstorageよりは遅い
[特にwindowsとかはもっと遅いらしい](http://sqlite.1065341.n5.nabble.com/Windows-slow-vs-iOS-OSX-fast-Performance-td65794.html)
##### 工夫
- 毎回DBにアクセスするのは時間もかかるし、angularのdata-bindingも生かせないんで、`$rootScope.$VM`にDBと同期させて保持させておく。それをラッピングしたModelFactoryでも作って、findの時は全て$VMから取得。変更を加える場合はDBに変更を加えて、返ってきたobjectの`rev`を$VMにある`_rev`をそれぞれ`id`と`_id`で比較ループして入れなおす。最後に`_rev`が新しくなったobjectを$VMに入れなおすって行く形をとる。起動時に全て`$VM`に入れてからこれらを行えばうまく少ないDBアクセス回数で運用できそう。
- `_id`以外の検索がめんどくさいので`_id`の[prefix検索](http://pouchdb.com/api.html#prefix-search)を使ってtable全件取得とか出来るように、`{_id:"users-1"}`みたいにするといい。

``` 例)変更が完了した後帰ってくるobject
{"ok":true,"id":"users-1","rev":"84-1092ef4c3c55010372d3b86ee96e2aa4"}
```

### 公式API等
- [PouchDB API](http://pouchdb.com/api.html)
- [iOS Data Storage Guide](https://developer.apple.com/icloud/documentation/data-storage/index.html)
