import pandas as pd

# CSV 파일 읽기
file_path_2분기 = 'C:\\data\\세종도시교통공사_공공자전거(어울링) 이용 현황 2024년 2분기.csv'
file_path_1분기 = 'C:\\data\\세종도시교통공사_공공자전거(어울링) 이용 현황 2024년 1분기.csv'

df_2분기 = pd.read_csv(file_path_2분기, encoding='cp949')
df_1분기 = pd.read_csv(file_path_1분기, encoding='cp949')

# 두 CSV 파일 합치기
df = pd.concat([df_1분기, df_2분기], ignore_index=True)

# 반납시간에서 시간을 추출
df['반납시간'] = pd.to_datetime(df['반납시간'])
df['반납시간_시간'] = df['반납시간'].dt.hour
df['반납시간_분'] = df['반납시간'].dt.minute

# 출퇴근 시간대 (7시 30분 ~ 8시 30분 및 18시 ~ 19시)
rush_hour_start_morning = (7, 30)
rush_hour_end_morning = (8, 30)
rush_hour_start_evening = (18, 0)
rush_hour_end_evening = (19, 0)

# 출퇴근 시간대에 해당하는 반납 데이터 필터링
rush_hour_morning = df[
    ((df['반납시간_시간'] == rush_hour_start_morning[0]) & (df['반납시간_분'] >= rush_hour_start_morning[1])) |
    ((df['반납시간_시간'] == rush_hour_end_morning[0]) & (df['반납시간_분'] <= rush_hour_end_morning[1])) |
    ((df['반납시간_시간'] > rush_hour_start_morning[0]) & (df['반납시간_시간'] < rush_hour_end_morning[0]))
]

rush_hour_evening = df[
    (df['반납시간_시간'] >= rush_hour_start_evening[0]) & (df['반납시간_시간'] < rush_hour_end_evening[0])
]

rush_hour_count = rush_hour_morning['반납시간'].count() + rush_hour_evening['반납시간'].count()

non_rush_hour_rentals = df[~df.index.isin(rush_hour_morning.index) & ~df.index.isin(rush_hour_evening.index)]
non_rush_hour_count = non_rush_hour_rentals['반납시간'].count()

print(f"출퇴근 시간대 반납 횟수 (7:30 ~ 8:30 및 18:00 ~ 19:00): {rush_hour_count}")
print(f"비출퇴근 시간대 반납 횟수: {non_rush_hour_count}")
print(round((rush_hour_count / (rush_hour_count + non_rush_hour_count)) * 100, 2), '%')
