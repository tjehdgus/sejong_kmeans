import pandas as pd

data = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\이동데이터.csv')
data

# 주어진 조건에 맞는 데이터 필터링
filtered_data = data[
    (data['WEEK_CD'] == 1) &
    (data['OD_TYPE_CD'] == 2)
][['DPTR_LEGALDONG_CD', 'ARVL_LEGALDONG_CD', 'OD_TYPE_CD', 'WEEK_CD', 'TM_CD', 'CFTM_AVE_TRFC_QTY', 'CFTM_AVE_EXPDG_TRFC_QTY']]

# 번호 -> 행정동 매핑
dongs = {
    29010110: '조치원읍',
    29010310: '연기면',
    29010320: '연동면',
    29010330: '부강면',
    29010340: '금남면',
    29010350: '장군면',
    29010360: '연서면',
    29010370: '전의면',
    29010380: '전동면',
    29010390: '소정면',
    29010610: '한솔동',
    29010670: '새롬동',
    29010660: '보람동',
    29010640: '대평동',
    29010710: '소담동',
    29010690: '도담동',
    29010590: '아름동',
    29010600: '고운동',
    29010560: '종촌동',
    29010680: '다정동',
    29010700: '해밀동',
    29010720: '반곡동'
}

filtered_data['출발지'] = filtered_data['DPTR_LEGALDONG_CD'].map(dongs)
filtered_data['도착지'] = filtered_data['ARVL_LEGALDONG_CD'].map(dongs)

이동 = filtered_data.dropna(subset=['출발지', '도착지'])
이동

이동.to_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\이동.csv', encoding='utf-8-sig', index=False)
