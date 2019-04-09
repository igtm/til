# coding: utf-8
import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib as mpl
import a30

if __name__ == '__main__':

    FNAME = 'neko.txt'
    FNAME_PARSED = 'neko.txt.mecab'

    # 形態素解析
    a30.parse_neko(FNAME, FNAME_PARSED)

    # 1文ずつ辞書のリストを作成
    lines = a30.neco_lines(FNAME_PARSED)
    word_counter = Counter()
    for line in lines:
        word_counter.update([morpheme['surface'] for morpheme in line])

    # 上位10件
    size = 10
    list_word = word_counter.most_common(size)
    print(list_word)

    # 分解
    list_zipped = list(zip(*list_word))
    words = list_zipped[0]
    counts = list_zipped[1]

    # Font: 日本語が表示できないので設定
    mpl.rcParams['font.family'] = 'IPAexGothic'

    # グラフのデータ指定
    plt.bar(
        range(0, size),
        counts,
        align='center'
    )

    # x軸のラベルの指定
    plt.xticks(
        range(0, size),
        words
    )

    # x軸の値の範囲
    plt.xlim(
        xmin=-1, xmax=size
    )

    # グラフのタイトル、ラベル指定
    plt.title(
        '頻出単語上位10件',
    )
    plt.xlabel(
        '出現頻度が高い10件',
    )
    plt.ylabel(
        '出現頻度',
    )

    # グリッド
    plt.grid(axis='y')

    plt.show()
