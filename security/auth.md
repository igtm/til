# 認証システムの比較検討

## Mobile認証自体
- [OWASP: Top Ten Mobile Controls](https://docs.google.com/document/d/1QOWOrsAo-33bHLdAZksKa4F_8_A_6XndoDF6ri4na_k/edit)
- [mobile全般](https://stormpath.com/blog/the-ultimate-guide-to-mobile-api-security/)
- [JWT](http://sssslide.com/speakerdeck.com/harukasan/json-web-token-authentication-for-mobile-application)
- [セキュリティ向上Tips](http://developer.telerik.com/featured/securing-phonegapcordova-hybrid-mobile-app/)
- [モバイルアプリのユーザ認証方法についてまとめてみた](http://qiita.com/ledmonster/items/0ee1e757af231aa927b1)
- [JWS 脆弱性](http://oauth.jp/blog/2015/03/16/common-jws-implementation-vulnerability/)
- [JWT slide](http://www.slideshare.net/briandavidcampbell/i-left-my-jwt-in-san-jose)

#### Tips
- [RSAにsetPasswordする](http://stackoverflow.com/questions/13635018/phpseclib-password-protected-rsa-and-user-authentication)
- [RSA公開鍵のファイル形式とfingerprint](http://qiita.com/hotpepsi/items/128f3a660cee8b5467c6)
- [Cookie-based Auth vs Token-based Auth](https://docs.google.com/drawings/d/1wtiF_UK2e4sZVorvfBUZh2UCaZq9sTCGoaDojSdwp7I/edit)
- [HTTP Authorizationヘッダを環境変数にセットする](http://sasakure.hatenablog.com/entry/20120726/1343279313)
- [PHP 安全なパスワードハッシュ](http://bashalog.c-brains.jp/14/03/26-190413.php)

#### メモ
- 秘密鍵を秘密鍵pemに変換`openssl rsa -in id_rsa -outform pem >id_rsa.pem`
- 公開鍵pemを作る`ssh-keygen -f jwt.pub -e -m pem`



## その他

#### OAuth2.0
- [よくわかるページ](http://www.atmarkit.co.jp/ait/articles/1209/10/news105.html)
- [さらに詳しく](http://www.atmarkit.co.jp/fsmart/articles/oauth2/02.html)

#### CSRF

#### その他重要ワード
- P2PE(Point to Point Encryption)


#### 事例

