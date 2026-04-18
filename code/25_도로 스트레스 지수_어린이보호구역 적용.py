import pandas as pd

# 데이터 불러오기
df = pd.read_csv('c:\\data\\sejong\\세종시_구간통행속도_전처리_최종.csv', encoding='utf-8-sig')

# 지수 계산을 위한 함수 (최대값이 30 이하일 경우 지수 값을 4로 설정)
def calculate_index(avg, max_val):
    if max_val <= 30:
        return 4
    ratio = (1 - (avg / max_val)) * 100
    if ratio <= 20:
        return 0
    elif 20 < ratio <= 25:
        return 1
    elif 25 < ratio <= 35:
        return 2
    elif 35 < ratio <= 45:
        return 3
    else:
        return 4

df['00분지수'] = df.apply(lambda row: calculate_index(row['00분_평균'], row['00분_최대값']), axis=1)
df['15분지수'] = df.apply(lambda row: calculate_index(row['15분_평균'], row['15분_최대값']), axis=1)
df['30분지수'] = df.apply(lambda row: calculate_index(row['30분_평균'], row['30분_최대값']), axis=1)
df['45분지수'] = df.apply(lambda row: calculate_index(row['45분_평균'], row['45분_최대값']), axis=1)

df['지수_합'] = df['00분지수'] + df['15분지수'] + df['30분지수'] + df['45분지수']

result_df = df[['요일', '도로명', '구간', '시', '방향', '00분_평균', '15분_평균', '30분_평균', '45분_평균',
                '00분_최대값', '15분_최대값', '30분_최대값', '45분_최대값',
                '00분지수', '15분지수', '30분지수', '45분지수', '지수_합']]

result_df

# 결과 저장
output_file_path = "c:\\data\\sejong\\지수_계산_결과_어린이보호구역적용.csv"
result_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
print(f"지수 계산 결과가 {output_file_path}에 저장되었습니다.")
