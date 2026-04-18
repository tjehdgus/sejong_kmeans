import osmnx as ox
import geopandas as gpd
import folium
import pandas as pd
from shapely.geometry import Point

# CSV 파일에서 좌표 데이터 읽기
data = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\combined_coordinates.csv')

# 행정동 리스트
administrative_dongs = [
    '용호동', '한별동', '누리동', '산울동', '해밀동', '고운동', '아름동', '도담동',
    '종촌동', '다정동', '새롬동', '한솔동', '가람동', '어진동', '나성동', '세종동',
    '반곡동', '소담동', '보람동', '대평동', '집현동', '합강동', '다솜동', '조치원읍'
]

map_center_lat = 36.5
map_center_lon = 127.3
mymap = folium.Map(location=[map_center_lat, map_center_lon], zoom_start=12)

for dong in administrative_dongs:
    try:
        location = f"{dong}, 세종시, South Korea"
        gdf = ox.geocode_to_gdf(location)

        if not gdf.empty:
            for _, row in gdf.iterrows():
                folium.GeoJson(
                    row['geometry'],
                    style_function=lambda x: {'fillColor': 'blue', 'color': 'blue', 'weight': 1, 'fillOpacity': 0.2},
                    tooltip=dong
                ).add_to(mymap)

            polygon = gdf['geometry'].values[0]
            filtered_rows = []
            for _, row in data.iterrows():
                point = Point(row['longitude'], row['latitude'])
                if polygon.contains(point):
                    filtered_rows.append(row)
                    folium.CircleMarker(
                        location=(row['latitude'], row['longitude']),
                        radius=5,
                        color='green',
                        fill=True,
                        fill_opacity=0.6,
                        popup=f"Coordinates: ({row['latitude']}, {row['longitude']})"
                    ).add_to(mymap)

            if filtered_rows:
                filtered_df = pd.DataFrame(filtered_rows)
                output_csv = f"C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\{dong}_coordinates.csv"
                filtered_df.to_csv(output_csv, index=False)
                print(f"{dong}의 좌표가 '{output_csv}'로 저장되었습니다.")
    except Exception as e:
        print(f"{dong} 처리 중 오류 발생: {e}")
