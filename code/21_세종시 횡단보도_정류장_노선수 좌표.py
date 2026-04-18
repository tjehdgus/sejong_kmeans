import pandas as pd
from gmplot import gmplot
import webbrowser

coordinate_bounds_1 = {
    'latitudes': [36.5231, 36.4973, 36.4738, 36.46462, 36.47581, 36.48788, 36.50058, 36.50624, 36.53241],
    'longitudes': [127.22716, 127.23064, 127.24508, 127.26714, 127.30464, 127.33417, 127.33752, 127.31366, 127.27536]
}
coordinate_bounds_2 = {
    'latitudes': [36.62317, 36.61325, 36.6065, 36.61373, 36.59375, 36.58679, 36.58231, 36.58706, 36.59258,
                  36.59774, 36.60615, 36.61077, 36.61752],
    'longitudes': [127.2844, 127.27788, 127.28269, 127.28586, 127.28028, 127.28415, 127.29333, 127.30097,
                   127.30453, 127.30582, 127.30402, 127.3017, 127.29672]
}

min_lat_1 = min(coordinate_bounds_1['latitudes'])
max_lat_1 = max(coordinate_bounds_1['latitudes'])
min_lon_1 = min(coordinate_bounds_1['longitudes'])
max_lon_1 = max(coordinate_bounds_1['longitudes'])

min_lat_2 = min(coordinate_bounds_2['latitudes'])
max_lat_2 = max(coordinate_bounds_2['latitudes'])
min_lon_2 = min(coordinate_bounds_2['longitudes'])
max_lon_2 = max(coordinate_bounds_2['longitudes'])

df = pd.read_csv('C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\세종특별자치시_노선별 정류장현황_20230602.csv', encoding='cp949')
df_grouped = df.groupby(['정류장ID', '정류장명', 'GPS_X', 'GPS_Y']).size().reset_index(name='count')

filtered_df_1 = df_grouped[(df_grouped['GPS_Y'] >= min_lat_1) & (df_grouped['GPS_Y'] <= max_lat_1) &
                           (df_grouped['GPS_X'] >= min_lon_1) & (df_grouped['GPS_X'] <= max_lon_1)]
filtered_df_2 = df_grouped[(df_grouped['GPS_Y'] >= min_lat_2) & (df_grouped['GPS_Y'] <= max_lat_2) &
                           (df_grouped['GPS_X'] >= min_lon_2) & (df_grouped['GPS_X'] <= max_lon_2)]
filtered_df = pd.concat([filtered_df_1, filtered_df_2])

map_center_lat = (min(min_lat_1, min_lat_2) + max(max_lat_1, max_lat_2)) / 2
map_center_lon = (min(min_lon_1, min_lon_2) + max(max_lon_1, max_lon_2)) / 2

gmap = gmplot.GoogleMapPlotter(map_center_lat, map_center_lon, 13, apikey='AIzaSyDfXHrCsrAFuw1WQrF5B5-Df9wb7kDRjIs')

latitudes = []
longitudes = []
for index, row in filtered_df.iterrows():
    latitudes.extend([row['GPS_Y']] * int(row['count']))
    longitudes.extend([row['GPS_X']] * int(row['count']))

gmap.scatter(latitudes, longitudes, color='red', size=5, marker=False)

file_paths = [
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\조치원_혜인.csv',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\조치원횡단보도.csv',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\종촌동.csv',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\고운동.csv',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\누리동.csv',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\집현동.csv'
]

for file in file_paths:
    data = pd.read_csv(file)
    gmap.scatter(data['latitude'], data['longitude'], color='blue', size=5, marker=False)

output_file = "c:\\data\\bus_stop_filtered_combined_map.html"
gmap.draw(output_file)
webbrowser.open(output_file)
print("Google 지도에 필터링된 정류장이 연한 분홍색 및 파란색 점으로 표시된 파일이 생성되고 브라우저에서 열렸습니다.")
