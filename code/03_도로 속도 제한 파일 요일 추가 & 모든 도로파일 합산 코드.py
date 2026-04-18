#!pip install xlrd>=2.0.1
import pandas as pd
import os

# 파일들이 위치한 디렉토리 경로
directory_path = 'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\세종시 도로구간별 속도'

# 빈 리스트 생성
df_list = []

# 지정된 폴더의 모든 파일을 읽어서 처리
for filename in os.listdir(directory_path):
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        file_path = os.path.join(directory_path, filename)

        # 엑셀 파일 읽기
        df = pd.read_excel(file_path)

        # 데이터의 4번째 행부터 끝까지 슬라이싱 후 복사
        df2 = df.iloc[4:, :].copy()

        # 컬럼 이름 재지정
        df2.columns = ['일자', '도로명', '방향', '구간', '상세도로', '시', '00분', '15분', '30분', '45분']

        # '일자' 컬럼을 날짜 형식으로 변환
        df2['일자'] = pd.to_datetime(df2['일자'], format='%Y년%m월%d일', errors='coerce')

        # 요일 컬럼 추가
        df2['요일'] = df2['일자'].dt.day_name(locale='ko_KR')

        df_list.append(df2)

# 리스트에 저장된 데이터프레임을 모두 하나로 합침
final_df = pd.concat(df_list, ignore_index=True)

final_df2 = final_df.loc[
    ~(
        final_df['구간'].str.contains('평균통행속도', na=False) |
        final_df['일자'].astype(str).str.contains('평균통행속도', na=False) |
        final_df['도로명'].str.contains('평균통행속도', na=False) |
        final_df['방향'].str.contains('평균통행속도', na=False) |
        final_df['상세도로'].str.contains('평균통행속도', na=False)
    )
].copy()

final_df3 = final_df2.dropna()

final_df3
