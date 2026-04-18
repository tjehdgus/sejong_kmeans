import pandas as pd

# 파일 경로
df = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\세종시_교통사고데이터(2021~2023).csv')

df['사고일시'] = df['사고일시'].str.replace('년 ', '-').str.replace('월 ', '-').str.replace('일 ', ' ').str.replace('시', ':00')

# '사고일시' 열을 datetime 형식으로 변환
df['사고일시'] = pd.to_datetime(df['사고일시'])

# 시군구 필터링 리스트
target_regions = ['용호동', '한별동', '누리동', '산울동', '해밀동', '고운동', '아름동', '도담동', '종촌동', '다정동',
                  '새롬동', '한솔동', '가람동', '어진동', '나성동', '세종동', '반곡동', '소담동', '보람동', '대평동',
                  '집현동', '합강동', '다솜동', '조치원읍']

# 가해운전차종 및 피해운전차종 필터링
pm_vehicle_types = ['자전거', '개인형이동수단(PM)']

# 시군구 필터링
filtered_df = df[df['시군구'].str.contains('|'.join(target_regions), na=False)]

# 가해운전차종 또는 피해운전차종이 '자전거' 또는 '개인형이동수단(PM)'인 경우 필터링
filtered_df = filtered_df[
    (filtered_df['가해운전자 차종'].isin(pm_vehicle_types)) |
    (filtered_df['피해운전자 차종'].isin(pm_vehicle_types))
]

# 결과 출력
filtered_df[['사고일시', '시군구', '도로형태', '가해운전자 차종', '피해운전자 차종']]
