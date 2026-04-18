import pandas as pd
from gmplot import gmplot

center_file_path = 'c:\\data\\sejong\\세종시_횡단보도.csv'
file_paths = [
    'c:\\data\\sejong\\조치원_혜인.csv',
    'c:\\data\\sejong\\조치원횡단보도.csv'
]

colors = ['blue', 'red']

center_data = pd.read_csv(center_file_path)
center_lat = center_data['latitude'].mean()
center_lon = center_data['longitude'].mean()

gmap = gmplot.GoogleMapPlotter(center_lat, center_lon, 12, apikey='AIzaSyDfXHrCsrAFuw1WQrF5B5-Df9wb7kDRjIs')

for file, color in zip(file_paths, colors):
    data = pd.read_csv(file)
    latitudes = data['latitude']
    longitudes = data['longitude']
    gmap.scatter(latitudes, longitudes, color=color, size=2, marker=False)

gmap.draw("c:\\data\\map.html")
