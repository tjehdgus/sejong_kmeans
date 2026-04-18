import pandas as pd

# 데이터 불러오기
df = pd.read_csv('c:\\data\\sejong\\지수_계산_결과_어린이보호구역적용.csv', encoding='utf-8-sig')

# 요일, 도로명, 구간, 방향별 지수합 평균 계산
grouped_df = df.groupby(['도로명', '구간', '방향']).agg(지수합평균=('지수_합', 'mean')).round(2).reset_index()

grouped_df

# 결과를 CSV로 저장
output_file_path = "c:\\data\\sejong\\지수합평균_도로별_결과_어린이보호구역적용.csv"
grouped_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
print(f"지수합평균 결과가 {output_file_path}에 저장되었습니다.")
