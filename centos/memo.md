# CentOS6.5サーバー構築まとめ


# サーバー起動〜初期設定

## ユーザー作成
- ssh接続: `ssh root@xxx.xxx.xxx.xxx -p 22`
- rootのパス変更: `passwd`
- user追加: `useradd xxx`
- userにパス設定: `passwd xxx`

## 公開鍵暗号方式
- 公開鍵&秘密鍵作成: `ssh-keygen`
- 秘密鍵を600: `chmod 600 id_rsa`
- /home/xxx/.ssh/に公開鍵転送: `scp -P 22 id_rsa.pub xx@xxx.xxx.xxx.xxx:`
- .sshを700 公開鍵をauthorized_keysにrename
- `vi /etc/ssh/sshd_config`

```
#PermitRootLogin yes
PermitRootLogin no
  
... 中略 ....
  
#PasswordAuthentication yes
PasswordAuthentication no
```
- `service sshd restart`

## sshのポート変更
-  0 ～ 65535までで変更: `vi /etc/ssh/sshd_config`

```
#Port 22
Port XXXXX
```
- 有効化: `/etc/rc.d/init.d/sshd restart`

## 日本語化
- `vi /etc/sysconfig/i18n`

```
LANG="ja_JP.UTF-8"
SYSFONT="latarcyrheb-sun16"
```

## sudoの有効化(root)
- `yum list installed | grep sudo`で確認。無ければinstall
- 対象ユーザをwheelグループに入れる: `usermod -G wheel XXXX`
- 確認: `id XXXX`
- 設定: `visudo` 以下コメント外す

```
%wheel        ALL=(ALL)       ALL
```

## パスを通す(一般ユーザ)
- `vi ~/.bash_profile` ３行追加

```
PATH=$PATH:$HOME/bin
PATH=$PATH:/sbin
PATH=$PATH:/usr/sbin
PATH=$PATH:/usr/local/sbin
```
- 有効化: `source ~/.bash_profile`

## ファイアーウォール
- 設定確認: `sudo iptables -L`
- 設定: `sudo vi /etc/sysconfig/iptables` xxxxxはsshのport番号に変えること

```
*filter
:INPUT   ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT  ACCEPT [0:0]
:RH-Firewall-1-INPUT - [0:0]

-A INPUT -j RH-Firewall-1-INPUT
-A FORWARD -j RH-Firewall-1-INPUT
-A RH-Firewall-1-INPUT -i lo -j ACCEPT
-A RH-Firewall-1-INPUT -p icmp --icmp-type any -j ACCEPT
-A RH-Firewall-1-INPUT -p 50 -j ACCEPT
-A RH-Firewall-1-INPUT -p 51 -j ACCEPT
-A RH-Firewall-1-INPUT -p udp --dport 5353 -d 224.0.0.251 -j ACCEPT
-A RH-Firewall-1-INPUT -p udp -m udp --dport 631 -j ACCEPT
-A RH-Firewall-1-INPUT -p tcp -m tcp --dport 631 -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# SSH, HTTP
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport XXXXX -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 80    -j ACCEPT

-A RH-Firewall-1-INPUT -j REJECT --reject-with icmp-host-prohibited

COMMIT
```

## 自動起動設定
- 確認: `chkconfig --list xxx`
- 設定: `sudo chkconfig xxx on`   

#### ランレベル
```
0:シャットダウン ( システム停止中 )
1:シングル ユーザー モード ( root のみ )
2:マルチ ユーザー モード ( ネットワークなし )
3:マルチ ユーザー モード ( テキスト )
4:未使用
5:マルチ ユーザー モード ( グラフィカル )
6:システム再起動
```
- ランレベルの確認: `runlevel`





# ミドルウェア

## Apache
#### 初期設定: `/etc/httpd/conf/httpd.conf`
```
	- L44 ServerTokens: クライアントに返す情報⇒`Prod`
	- L242 User&Group: ApacheのUserとGroup⇒`apache`
	- L292 DocumentRoot: Webサーバーのルートディレクトリ
	- L331 Options: indexを表示しないように⇒`-Indexes FollowSymLinks`
	- L536 ServerSignature: エラーページなどに出力されるサーバー情報
```
- 設定問題あるかテスト: `sudo apachectl configtest`

#### チューニング
- [不要モジュールの無効化](http://akabeko.me/blog/2012/04/revps-04-apache/#revps-04-03): `/etc/httpd/conf/httpd.conf`
- [チューニング](http://qiita.com/kou/items/acb3dcf1dcb428d7a3ec)
- [httpd.conf](http://linux.kororo.jp/cont/server/httpd_conf.php)
- [モジュール詳細一覧](https://httpd.apache.org/docs/2.2/ja/mod/)


#### セキュリティ
- [パーミッション関連](http://egapool.hatenablog.com/entry/2013/11/29/184300)
- [セキュリティ向上Tips](http://builder.japan.zdnet.com/tool/20386932/)
- [セキュリティ](http://www.rem-system.com/apache-security01/)
- [セキュリティ](http://www.websec-room.com/2014/02/09/1822)

#### バーチャルホスト
- [公式バーチャルホスト設定(英語)](https://wiki.centos.org/TipsAndTricks/ApacheVhostDir)
- [wwwへリダイレクト](http://www.itmedia.co.jp/help/tips/linux/l0397.html)

#### SSL
- [わかりやすいSSL](http://www.atmarkit.co.jp/ait/articles/1301/23/news107.html)
- [同じくわかりやすいSSL](http://knowledge.sakura.ad.jp/beginner/2813/)

#### その他設定
- [Digest認証](http://hizadegozaru.0t0.jp/blog/blog/2015/04/04/digest%E8%AA%8D%E8%A8%BC%E3%81%AE%E8%A8%AD%E5%AE%9A%EF%BC%88apache-centos-6%EF%BC%89/)
- [FW IPS WAF概念がわかりやすい](http://www.slideshare.net/CitrixSystemsJapan/waf-49536255?ref=https://www.desktop2cloud.jp/product/citrix-netscaler/ns-hardware/extend-waf-performance-cloud-load-balancer-interlop2015.html)

## Mysql
- [yumで最新版インストールする方法](http://www.tecmint.com/install-latest-mysql-on-rhel-centos-and-fedora/)
- 設定ファイル: `/etc/my.cnf` [文字化け対策](http://qiita.com/WizowozY/items/5d7224be92aa8364a42a)
- 初期自動設定コマンド: `mysql_secure_installation`
- ※ [Access denied for user ‘root’@’localhost’ (using password: NO)の対処](http://www.goofoo.jp/2011/11/1457)

## 各種インストール
#### PHP
###### インストール
- [php5.6](https://inexio.jp/20140624-323)
- OPcache: `yum install --enablerepo=remi --enablerepo=remi-php56 php-opcache`
- APCu: `yum --enablerepo=remi-php56 install php-pecl-apc`

###### 設定
- [php.ini](http://webkaru.net/php/php-ini/)

#### phpMyAdmin

###### インストール
- [本家download](https://www.phpmyadmin.net/downloads/)
- install: `wget https://files.phpmyadmin.net/phpMyAdmin/4.5.2/phpMyAdmin-4.5.2-all-languages.tar.gz`
- 展開: `tar zxvf phpMyAdmin-4.5.2-all-languages.tar.gz`
- 出来上がったものを好きな場所へmv
- 設定: `/etc/httpd/conf.d/phpmyadmin.conf`  

```
<Directory "/var/www/html/phpMyAdmin">
Order deny,allow
Deny from all
Allow from "社内ipアドレス"
</Directory>
```
- 反映: `sudo service httpd restart`


## 便利ツール
- [logwatch](http://www.happyquality.com/2012/02/02/1924.htm)(ログ収集・メール送信ツール): `sudo logwatch --print`


## Tips
- Linuxファイル構造: [FHS](http://www.linuxmaster.jp/linux_skill/2010/02/06linux.html)
