import pandas as pd
import folium

# 첫 번째 데이터: 지하철역 좌표 (파란색)
data1 = pd.read_csv('c:\\data\\station_coordinate.csv', encoding='cp949')

# 두 번째 데이터: 버스정류장 좌표 (빨간색)
data2 = pd.read_csv('c:\\data\\버스정류장.csv', encoding='cp949')

# 세 번째 데이터: 횡단보도 좌표 (초록색)
data3 = pd.read_csv('c:\\data\\서울시횡단보도위치정보.csv', encoding='utf8')

# 네 번째 데이터: 따릉이 위치 (검정색)
data4 = pd.read_csv('c:\\data\\따릉이위치.csv', encoding='cp949')

# 지도 중심 좌표 계산
center_lat = data1['lat'].mean()
center_lon = data1['lng'].mean()

# 지도 생성
mymap = folium.Map(location=[center_lat, center_lon], zoom_start=10)

# 첫 번째 데이터 (파란색)
for i, row in data1.iterrows():
    folium.CircleMarker(location=[row['lat'], row['lng']], radius=1, color='blue', fill=True, fill_color='blue', fill_opacity=0.6).add_to(mymap)

# 두 번째 데이터 (빨간색)
for i, row in data2.iterrows():
    folium.CircleMarker(location=[row['Y좌표'], row['X좌표']], radius=1, color='red', fill=True, fill_color='red', fill_opacity=0.6).add_to(mymap)

# 세 번째 데이터 (초록색)
for i, row in data3.iterrows():
    folium.CircleMarker(location=[row['Y좌표'], row['X좌표']], radius=1, color='green', fill=True, fill_color='green', fill_opacity=0.6).add_to(mymap)

# 네 번째 데이터 (검정색)
for i, row in data4.iterrows():
    folium.CircleMarker(location=[row['위도'], row['경도']], radius=1, color='black', fill=True, fill_color='black', fill_opacity=0.6).add_to(mymap)

# 지도를 HTML 파일로 저장
mymap.save('map.html')

mymap
