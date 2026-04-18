import pandas as pd

# 데이터 로드
df = pd.read_csv("f:\\data\\filled_file2.csv")

# 새벽시간대인 행 데이터에서 제외
df2 = df[~df['시'].isin(['01시', '02시', '03시', '04시', '05시'])]

# 1. 요일, 도로명, 구간, 시, 방향별 시간대별 평균 통행속도 계산
day_time_mean_v = df2.groupby(['요일', '도로명', '구간', '시', '방향'])[['00분', '15분', '30분', '45분']].mean().reset_index()

# 2. 구간별(요일, 도로명, 구간, 방향)로 각 시간대의 최대값을 계산
max_values = df2.groupby(['요일', '도로명', '구간', '방향'])[['00분', '15분', '30분', '45분']].max().reset_index()

# 3. 구간별 최대값보다 작은 값 중에서 가장 큰 값을 계산하는 함수 정의
def get_second_largest(group):
    result = {}
    for time_col in ['00분', '15분', '30분', '45분']:
        max_val = group[time_col].max()
        second_largest = group[time_col][group[time_col] < max_val].max()
        result[time_col] = second_largest
    return pd.Series(result)

# 4. 구간별 최대값보다 작은 값 중에서 가장 큰 값 계산
second_largest_values = df2.groupby(['요일', '도로명', '구간', '방향']).apply(get_second_largest).reset_index()

# 5. 평균과 두 번째로 큰 값을 병합 (최대값으로 사용)
final_df = pd.merge(day_time_mean_v, second_largest_values, on=['요일', '도로명', '구간', '방향'], suffixes=('_평균', '_최대값'))

# 6. 최대값과 평균값의 차이를 계산하는 새로운 컬럼 추가
final_df['00분_차이'] = final_df['00분_최대값'] - final_df['00분_평균']
final_df['15분_차이'] = final_df['15분_최대값'] - final_df['15분_평균']
final_df['30분_차이'] = final_df['30분_최대값'] - final_df['30분_평균']
final_df['45분_차이'] = final_df['45분_최대값'] - final_df['45분_평균']

# 7. 최종 출력
final_result = final_df[['요일', '도로명', '구간', '시', '방향',
                         '00분_평균', '15분_평균', '30분_평균', '45분_평균',
                         '00분_최대값', '15분_최대값', '30분_최대값', '45분_최대값',
                         '00분_차이', '15분_차이', '30분_차이', '45분_차이']]

final_result

# CSV 파일로 저장
final_result.to_csv("f:\\data\\세종시_구간통행속도_전처리_최종.csv", encoding="utf-8-sig", index=False)
print("CSV 파일이 '세종시_구간통행속도_전처리_최종.csv'로 저장되었습니다.")
