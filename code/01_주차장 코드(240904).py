import pandas as pd

# 모든 열을 출력할 수 있도록 설정
pd.set_option('display.max_columns', None)

# CSV 파일 읽기
df = pd.read_csv('C:\\data\\건축인허가_주차장.csv', encoding='euc-kr')

# '적재_연월'이 202405인 행 필터링
df2 = df.loc[df['적재_연월'] == 202405, :]

# 검색할 단어 리스트
search_words = [
    '용호동', '한별동', '누리동', '산울동', '해밀동', '고운동', '아름동', '도담동', '종촌동', '다정동',
    '새롬동', '한솔동', '가람동', '어진동', '나성동', '세종동', '반곡동', '소담동', '보람동', '대평동',
    '집현동', '합강동', '다솜동','조치원읍'
]

# 단어 리스트를 '|'로 연결한 패턴 생성
pattern = '|'.join(search_words)

# '대지위치' 열에 주어진 단어들이 포함된 행만 필터링
filtered_df = df2[df2['대지위치'].str.contains(pattern)].copy()

# 필요한 열만 선택
df3 = filtered_df[['대지위치', '옥내자주식대수(대)', '옥외자주식대수(대)']].copy()

# 파생 컬럼 '총주차대수(대)' 생성 (loc 사용)
df3.loc[:, '총주차대수(대)'] = df3['옥내자주식대수(대)'] + df3['옥외자주식대수(대)']

# '대지위치'로 그룹화하여 '총주차대수(대)'를 합산, 대지위치 중복 제거
result = df3.groupby('대지위치', as_index=False)['총주차대수(대)'].sum().reset_index()

# 결과 출력
filtered_result = result[result['총주차대수(대)'] > 10]

a = filtered_result[filtered_result['대지위치'].str.contains('어진동 581')]
a
