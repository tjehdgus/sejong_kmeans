import pandas as pd
import folium

# CSV 파일에서 위도와 경도 데이터를 불러오기
data = pd.read_csv('c:\\data\\전체 주차장 위치.csv', encoding="utf-8")

# 지도 중심을 설정하기 위해 평균 좌표를 계산
center_lat = data['위도'].mean()
center_lon = data['경도'].mean()

# 지도 생성
mymap = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# 각 데이터의 위도, 경도에 점(CircleMarker) 추가
for i, row in data.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(mymap)

# 지도를 HTML 파일로 저장
mymap.save('map.html')

mymap
