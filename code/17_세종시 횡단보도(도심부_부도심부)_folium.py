import pandas as pd
import folium

# CSV 파일에서 위도와 경도 데이터를 불러오기
data = pd.read_csv('c:\\data\\세종시_횡단보도.csv', encoding="utf-8")

center_lat = data['latitude'].mean()
center_lon = data['longitude'].mean()

mymap = folium.Map(location=[center_lat, center_lon], zoom_start=10)

for i, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=2,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(mymap)

mymap
