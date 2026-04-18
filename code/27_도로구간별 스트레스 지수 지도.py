import pandas as pd
import folium

file_paths = [
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\어울로,시청대로,일반국도36호선.txt',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\허석만로,행복대로,한누리대로,충현로집현중앙로.txt',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\절재로,조치원로,지방도604호선,지방도96호선,집현서로.txt',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\세종1로.txt',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\남세종로, 달빛로, 미리내로, 보듬7로, 보듬8로, 보담서로, 새내로, 세종로, 소담로.txt',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\갈매로.txt',
    'C:\\Users\\tjehd\\OneDrive\\바탕 화면\\세종시\\갈매로2.txt'
]

dfs = []
for file_path in file_paths:
    df = pd.read_csv(file_path, sep='\t', on_bad_lines='skip')
    df = df[df['latitude'] != 'latitude']
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    df[['color', 'opacity', 'width', 'name']] = df[['color', 'opacity', 'width', 'name']].fillna(method='ffill')
    dfs.append(df)

pd.set_option('display.max_row', None)
df_combined = pd.concat(dfs, ignore_index=True)

map_center_lat = df_combined['latitude'].mean()
map_center_lon = df_combined['longitude'].mean()
mymap = folium.Map(location=[map_center_lat, map_center_lon], zoom_start=14)

for name, group in df_combined.groupby('name'):
    locations = group[['latitude', 'longitude']].values.tolist()
    folium.PolyLine(
        locations,
        color=group['color'].iloc[0],
        weight=2.5,
        opacity=float(group['opacity'].iloc[0])
    ).add_to(mymap)

mymap.save("c:\\data\\세종시 도로 지도.html")

import webbrowser
webbrowser.open("c:\\data\\세종시 도로 지도.html")
