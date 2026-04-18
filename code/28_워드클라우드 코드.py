import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
import pandas as pd
import random

def related_wordcloud_with_emotion(location, keyword, exclude_words=None):
    # 감정 분석 파일 로드
    positive = open("c:\\data\\pos_pol_word.txt", encoding="utf8")
    negative = open("c:\\data\\neg_pol_word.txt", encoding="utf8")

    pos = positive.read().split('\n')
    neg = negative.read().split('\n')

    pos1 = list(filter(lambda x: len(x) > 1, pos))
    neg1 = list(filter(lambda x: len(x) > 1, neg))

    with open(location, 'r', encoding='utf8') as f:
        text = f.read()

    related_words = []
    okt = Okt()
    for sentence in text.split('.'):
        if keyword in sentence:
            nouns = okt.nouns(sentence)
            for i in nouns:
                if len(i) > 1:
                    related_words.append(i)

    if related_words:
        top_words = Counter(related_words).most_common(200)
    else:
        print(f'{keyword}과 연관된 단어가 없습니다.')
        return

    if exclude_words is None:
        exclude_words = []

    filtered_top_words = [(word, count) for word, count in top_words if word not in exclude_words]

    if not filtered_top_words:
        print("제외 단어를 제외한 결과가 없습니다.")
        return

    dct = {'키워드': [], 'cnt': []}
    for key, value in filtered_top_words:
        dct['키워드'].append(key)
        dct['cnt'].append(value)

    df = pd.DataFrame(dct)
    df.columns = ['title', 'count']

    wc = df.set_index('title').to_dict()['count']
    neg_in_text = [word for word in wc.keys() if word in neg1]

    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        if word in neg_in_text:
            return 'red'
        else:
            return 'black'

    mask = np.array(Image.open("c:/data/as.png"))

    wordCloud = WordCloud(
        font_path="c:/Windows/Fonts/malgunbd.ttf",
        width=1200,
        height=1200,
        max_font_size=150,
        min_font_size=10,
        max_words=200,
        background_color='white',
        mask=mask,
        contour_width=0,
        relative_scaling=0.5,
        collocations=False,
        prefer_horizontal=0.5,
        random_state=42
    ).generate_from_frequencies(wc)

    plt.imshow(wordCloud.recolor(color_func=color_func), interpolation='bilinear')
    plt.axis('off')
    plt.show()

    output_image_path = "c:\\data\\wordcloud_output.png"
    wordCloud.to_file(output_image_path)


# 함수 실행
exclude_words = ['세종', '세종시', '주차']
related_wordcloud_with_emotion("c:\\data\\세종시전기자전거.txt", "주차", exclude_words)
