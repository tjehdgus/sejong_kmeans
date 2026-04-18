import pandas as pd
import folium

# CSV 파일 불러오기
data_blue = pd.read_csv('c:\\data\\전체 주차장 위치.csv', encoding="utf-8")   # 첫 번째 파일 (파란 점)
data_red = pd.read_csv('c:\\data\\세종특별자치시_어린이 보호구역_기타상세_20230412.csv', encoding='euc-kr')  # 두 번째 파일 (빨간 점)

# 지도 중심을 설정하기 위해 평균 좌표를 계산
center_lat = (data_blue['위도'].mean() + data_red['위도'].mean()) / 2
center_lon = (data_blue['경도'].mean() + data_red['경도'].mean()) / 2

# 지도 생성
mymap = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# 첫 번째 파일의 데이터를 파란색 점으로 표시
for i, row in data_blue.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(mymap)

# 두 번째 파일의 데이터를 빨간색 점과 300미터 반경의 원으로 표시
for i, row in data_red.iterrows():
    # 빨간 점
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=5,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6
    ).add_to(mymap)

    # 반경 200미터의 원
    folium.Circle(
        location=[row['위도'], row['경도']],
        radius=200,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.2
    ).add_to(mymap)

mymap
