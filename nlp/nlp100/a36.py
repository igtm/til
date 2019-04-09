# coding: utf-8
import MeCab
from collections import Counter
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

    print(word_counter.most_common())
