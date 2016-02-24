# Unixコマンドメモ
### 便利コマンド

- [type](http://itpro.nikkeibp.co.jp/atcl/column/15/042000103/080600042/?rt=nocnt): コマンドの保存場所分かる

### ディレクトリ/ファイル のみにchmodを適応する方法
- `find . -type f -print | xargs chmod 644`
- `find . -type d -print | xargs chmod 550`
- 空白が含まれる名前には適応できない。