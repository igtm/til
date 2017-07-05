# DDD勉強

- [Youtube](https://www.youtube.com/watch?v=1OgvUIsv96o)
- 値オブジェクト
	- Stringly Typed code => Strongly Typed code
	- emailをただ文字列として扱うと、それが本当に正しいメアドなのかを都度バリデーションしないといけない。Emailオブジェクトとして受け渡しすれば、Emailオブジェクトが定義したメアドを都度、呼び出すだけでOK！

	
- ドメインイベント
	- 処理が終わったあとに、別のことしたいみたいなことが後からあるかもしれない。普通にやると、そのコードを触らずに実装することはできない。でも何かした後、イベントを発火しておけば、その後に処理したいものはそれを購読しておけば、いくらでも外で実装ができる。
	- 購入がcompleteした後に、期間限定のポイントを付加したい場合、'complete'みたいなeventをpublishして、それをsubscribeしてポイント付加を実装すればいい。complete処理は一切触らなくていい。

- [DDD難民に捧げる Domain-Driven Designのエッセンス](https://www.ogis-ri.co.jp/otc/hiroba/technical/DDDEssence/chap2.html)
- サービス
	- ドメインで扱う概念の中には、1つの機能や処理が単体で存在していて、もの（オブジェクト）として扱うのが不自然なものもある。そうしたものは、サービスという形でユビキタス言語に組み込む。サービスは基本的に状態をもたない（stateless）。
- ファクトリ
	- オブジェクトや集約の生成処理はそれ自体複雑になりうるため、ファクトリを導入して生成処理をカプセル化*2する。オブジェクトの生成そのものがドメインモデル上で重要な意味をもつことは（ほとんど）ないため、ファクトリはドメインモデルの一部ではない。あくまで、ドメインの設計上必要な一要素、という位置付けになる。
- レポジトリ
	- DBへの永続化や問い合わせ処理の複雑さによって、ドメインモデルが汚染されないようにするため、リポジトリという永続化／問い合わせ専用オブジェクトをドメイン設計に導入する

- [レイヤー設計とか、オブジェクト指向とか、DDDとか、その辺](http://mattun.hatenablog.com/entry/2014/07/19/135320)
- コントローラからはRepositoryを呼んではいけない、っていうのがある。（これは海外でもあるっぽい。）代わりにServiceを呼ぶべきであると。
- そもそも、ドメインオブジェクトのインタラクションはServiceLayerに委譲するので、Repositoryどころか、他のEntityの振舞いとかドメイン層の振舞いはどれもやってはいけないはず。コントローラの役割はServiceLayerの結果をビューに渡すなどの処理のみしか許されていない。
- ServiceがDDDにあるような1ドメインモデルとしてのServieならRepository禁止はDAOと混同しているからで、純粋なドメインモデルとしてのRepositoryはコントローラで呼んでもいいはず。Serviceをかぶせることを強制してしまうと、それこそ、どこで何をやっているのか分からなくなる。
- 一般的なEntity問い合わせの責務はRepositoryに集約されるべき。

-[DDD の Java EE 実装サンプル - Cargo Tracker を読み解く](http://qiita.com/opengl-8080/items/4f8938c65d8a2b7e50d0)
- 「アプリケーション層は薄く保つ」「ドメインの知識が漏れている」
- アプリケーション層の目的は「ドメインオブジェクトを連携させて処理を実現する」こと

- [](https://thinkinginobjects.com/2012/08/26/dont-use-dao-use-repository/)
-  You avoid to expose the type of Accounts identity to the Repository interface. It makes my life easy
-  Repositoryのインターフェースは、Entityの何がindentityかという情報が外に漏れ出ない。UserRepository.delete(uid: 3) ではなく、UserRepository.delete(User)とする。使う人は何がidかを知らないでいい。