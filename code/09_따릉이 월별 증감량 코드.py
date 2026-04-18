import pandas as pd

# 첫 번째 파일 읽기 (엑셀 파일)
file_path = 'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\서울특별시 공공자전거 일별 대여건수_23.1-6.xlsx'
df2023_1 = pd.read_excel(file_path)
df2023_1.columns = ['대여일시', '대여건수']

df2023_2 = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\서울특별시 공공자전거 일별 대여건수_23.7-12.csv', encoding='euc-kr')
df2023_2.columns = ['대여일시', '대여건수']

df2022_1 = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\서울특별시 공공자전거 일별 대여건수_22.01-22.06.csv', encoding='euc-kr')
df2022_1 = df2022_1.iloc[:, :2].copy()
df2022_1.columns = ['대여일시', '대여건수']

df2022_2 = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\서울특별시 공공자전거 일별 대여건수_22.07-22.12.csv', encoding='euc-kr')
df2022_2 = df2022_2.iloc[:, :2].copy()
df2022_2.columns = ['대여일시', '대여건수']

df2021_1 = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\서울특별시 공공자전거 일별 대여건수_21.01.01~21.06.30.csv', encoding='euc-kr')
df2021_1 = df2021_1.iloc[:, :2].copy()
df2021_1.columns = ['대여일시', '대여건수']

df2021_2 = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\서울특별시 공공자전거 일별 대여건수_21.07-21.12.csv', encoding='euc-kr')
df2021_2 = df2021_2.iloc[:, :2].copy()
df2021_2.columns = ['대여일시', '대여건수']

# 두 데이터프레임을 행 기준으로 이어붙이기
df_combined = pd.concat([df2023_1, df2023_2, df2022_1, df2022_2, df2021_1, df2021_2], ignore_index=True)

df_combined['대여일시'] = pd.to_datetime(df_combined['대여일시'])
df_combined['대여일시'] = df_combined['대여일시'].dt.to_period('M')
df_combined = df_combined.dropna()

# 쉼표 제거 및 정수형 변환
df_combined['대여건수'] = df_combined['대여건수'].replace(',', '', regex=True).astype(int)

df_cnt_y = df_combined.groupby('대여일시').sum().reset_index().copy()
df_cnt_y['이전월_대여건수'] = df_cnt_y['대여건수'].shift(1).copy()

# 증감율 계산
df_cnt_y['증감율'] = ((df_cnt_y['대여건수'] - df_cnt_y['이전월_대여건수']) / df_cnt_y['이전월_대여건수']) * 100
df_cnt_y['증감율'] = df_cnt_y['증감율'].fillna(0)

df_cnt_y
