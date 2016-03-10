# Octave使い方(coursera)

### 基本
- `;`あり：出力しない

### 設定
- `PS1('>> ');`: プロンプトの記号を`>>`に変えて見やすくする
- `format long`: 出力される小数点を結構表示する
- `format short`: 普通 

### 定数
- `pi`: パイ

### 関数
- `disp`:出力
- `sprintf`: フォーマット形式出力

### 行列

``` 3×2
A = [1 2; 3 4; 5 6]
A =

   1   2
   3   4
   5   6
```

- `1:0.1:2`: 1〜2を0.1のステップで増えた数
- `1:6`: 1〜6の行ベクター
- `ones`: `1`の行列
- `zeros`: `0`の行列
- `rand`: ランダム数字の行列
- `hist`: ヒストグラム表示 [詳細](http://qiita.com/noanoa07/items/a20dccff0902947d3e0c)
- `eye`: 単位行列