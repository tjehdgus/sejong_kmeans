import pandas as pd
from gmplot import gmplot

center_file_path = 'c:\\data\\sejong\\세종시_횡단보도.csv'
file_paths = [
    'c:\\data\\sejong\\조치원_혜인.csv',
    'c:\\data\\sejong\\조치원횡단보도.csv',
    'c:\\data\\sejong\\종촌동.csv',
    'c:\\data\\sejong\\고운동.csv',
    'c:\\data\\sejong\\누리동.csv',
    'c:\\data\\sejong\\집현동.csv'
]

color = 'blue'

center_data = pd.read_csv(center_file_path)
center_lat = center_data['latitude'].mean()
center_lon = center_data['longitude'].mean()

gmap = gmplot.GoogleMapPlotter(center_lat, center_lon, 12, apikey='AIzaSyDfXHrCsrAFuw1WQrF5B5-Df9wb7kDRjIs')

for file in file_paths:
    data = pd.read_csv(file)
    latitudes = data['latitude']
    longitudes = data['longitude']
    gmap.scatter(latitudes, longitudes, color=color, size=2, marker=False)

gmap.draw("c:\\data\\map.html")
