import pandas as pd
import folium

data = pd.read_csv('c:\\data\\세종시주차장위치.csv', encoding="cp949")

center_lat = data['위도'].mean()
center_lon = data['경도'].mean()

mymap = folium.Map(location=[center_lat, center_lon], zoom_start=10)

for i, row in data.iterrows():
    folium.CircleMarker(
        location=[row['위도'], row['경도']],
        radius=5,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.6
    ).add_to(mymap)

mymap.save('map.html')

mymap
