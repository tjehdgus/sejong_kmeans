import pandas as pd
import folium

# 5개의 CSV 파일 경로
center_file_path = 'c:\\data\\sejong\\세종시_횡단보도.csv'
file_paths = [
    'c:\\data\\sejong\\종촌동.csv',
    'c:\\data\\sejong\\고운동.csv',
    'c:\\data\\sejong\\누리동.csv',
    'c:\\data\\sejong\\집현동.csv'
]

# 지도에 표시할 각 파일마다 다른 색상 목록
colors = ['blue', 'green', 'red', 'purple']

# 중심 좌표 계산
center_data = pd.read_csv(center_file_path)
center_lat = center_data['latitude'].mean()
center_lon = center_data['longitude'].mean()

mymap = folium.Map(location=[center_lat, center_lon], zoom_start=12)

for file, color in zip(file_paths, colors):
    data = pd.read_csv(file)
    for i, row in data.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=2,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.6
        ).add_to(mymap)

mymap
