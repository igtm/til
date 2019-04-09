# coding: utf-8
import MeCab
import a30

if __name__ == '__main__':

    FNAME = 'neko.txt'
    FNAME_PARSED = 'neko.txt.mecab'

    # 形態素解析
    a30.parse_neko(FNAME, FNAME_PARSED)

    # 1文ずつ辞書のリストを作成
    lines = a30.neco_lines(FNAME_PARSED)
    verbs = set()
    verbs_test = []
    for line in lines:
        print(line)
        for morpheme in line:
            if morpheme['pos'] == '動詞':
                verbs.add(morpheme['surface'])
                verbs_test.append(morpheme['surface'])

    #print(sorted(verbs, key=verbs_test.index))
