import pandas as pd
from sklearn.cluster import KMeans
import folium
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

data1 = pd.read_csv('c:\\data\\station_coordinate.csv', encoding='cp949')
data2 = pd.read_csv('c:\\data\\버스정류장.csv', encoding='cp949')
data3 = pd.read_csv('c:\\data\\서울시횡단보도위치정보.csv', encoding='utf8')
data4 = pd.read_csv('c:\\data\\따릉이위치.csv', encoding='cp949')

data1_coords = data1[['lat', 'lng']].values
data2_coords = data2[['Y좌표', 'X좌표']].values
data3_coords = data3[['Y좌표', 'X좌표']].values
data4_coords = data4[['위도', '경도']].values

independent_data = pd.DataFrame(data1_coords.tolist() + data2_coords.tolist() + data3_coords.tolist(), columns=['lat', 'lng'])
dependent_data = pd.DataFrame(data4_coords, columns=['lat', 'lng'])

lat_min, lat_max = 37.4133, 37.7151
lng_min, lng_max = 126.7341, 127.2693

independent_data_filtered = independent_data[
    (independent_data['lat'] >= lat_min) & (independent_data['lat'] <= lat_max) &
    (independent_data['lng'] >= lng_min) & (independent_data['lng'] <= lng_max)
]

center_lat = independent_data_filtered['lat'].mean()
center_lon = independent_data_filtered['lng'].mean()

mymap = folium.Map(location=[center_lat, center_lon], zoom_start=12)

# 종속변수 데이터 (검정색, 따릉이 위치)만 표시
for i, row in dependent_data.iterrows():
    folium.CircleMarker(location=[row['lat'], row['lng']], radius=3, color='black', fill=True, fill_color='black', fill_opacity=0.6).add_to(mymap)

# K-means clustering (2763개 클러스터)
kmeans = KMeans(n_clusters=2763, random_state=42)
kmeans.fit(independent_data_filtered)

centroids = kmeans.cluster_centers_

# 클러스터 중심점 시각화 (오렌지색)
for center in centroids:
    folium.Marker(
        location=[center[0], center[1]],
        popup='클러스터 중심점',
        icon=folium.Icon(color='orange', icon='info-sign')
    ).add_to(mymap)

mymap
