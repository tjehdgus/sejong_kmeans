import osmnx as ox
import geopandas as gpd
import folium
import pandas as pd
from shapely.geometry import Point

# 행정동 리스트
administrative_dongs = [
    '용호동', '한별동', '누리동', '산울동', '해밀동', '고운동', '아름동', '도담동',
    '종촌동', '다정동', '새롬동', '한솔동', '가람동', '어진동', '나성동', '세종동',
    '반곡동', '소담동', '보람동', '대평동', '집현동', '합강동', '다솜동', '조치원읍'
]

combined_data = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\combined_coordinates.csv')
parking_data = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\세종시주차장위치.csv', encoding="cp949")

combined_data.rename(columns={'latitude': '위도', 'longitude': '경도'}, inplace=True)

map_center_lat = combined_data['위도'].mean()
map_center_lon = combined_data['경도'].mean()
mymap = folium.Map(location=[map_center_lat, map_center_lon], zoom_start=12)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#33FFA2', '#A233FF', '#FF9E33', '#33FFDD']

for i, dong in enumerate(administrative_dongs):
    try:
        location = f"{dong}, 세종시, South Korea"
        gdf = ox.geocode_to_gdf(location)

        if not gdf.empty:
            color = colors[i % len(colors)]

            for _, row in gdf.iterrows():
                folium.GeoJson(
                    row['geometry'],
                    style_function=lambda x, color=color: {
                        'fillColor': color, 'color': color, 'weight': 1, 'fillOpacity': 0.2
                    },
                    tooltip=dong
                ).add_to(mymap)

            polygon = gdf['geometry'].values[0]
            filtered_rows_combined = []

            for _, row in combined_data.iterrows():
                point = Point(row['경도'], row['위도'])
                if polygon.contains(point):
                    filtered_rows_combined.append(row)
                    folium.CircleMarker(location=(row['위도'], row['경도']), radius=5, color='green', fill=True, fill_opacity=0.6).add_to(mymap)

            for _, row in parking_data.iterrows():
                point = Point(row['경도'], row['위도'])
                if polygon.contains(point):
                    filtered_rows_combined.append(row)
                    folium.CircleMarker(location=(row['위도'], row['경도']), radius=5, color='blue', fill=True, fill_opacity=0.6).add_to(mymap)

            if filtered_rows_combined:
                filtered_df_combined = pd.DataFrame(filtered_rows_combined)
                output_csv_combined = f"C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\{dong}_combined_and_parking_coordinates.csv"
                filtered_df_combined.to_csv(output_csv_combined, index=False, encoding='utf-8-sig')
                print(f"{dong}의 좌표(기존+주차장)가 '{output_csv_combined}'로 저장되었습니다.")

    except Exception as e:
        print(f"{dong} 처리 중 오류 발생: {e}")

output_file = "c:\\data\\세종시_도로_및_주차장_지도.html"
mymap.save(output_file)

import webbrowser
webbrowser.open(output_file)
print(f"지도가 '{output_file}'로 저장되었습니다.")
