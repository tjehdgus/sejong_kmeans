import pandas as pd
from gmplot import gmplot

center_file_path = 'd:\\sejong\\횡단보도\\세종시_횡단보도.csv'
file_paths = [
    'd:\\sejong\\횡단보도\\조치원_혜인.csv',
    'd:\\sejong\\횡단보도\\조치원횡단보도.csv',
    'd:\\sejong\\횡단보도\\고운동.csv',
    'd:\\sejong\\횡단보도\\종촌동.csv',
    'd:\\sejong\\횡단보도\\집현동.csv',
    'd:\\sejong\\횡단보도\\혜인이.csv'
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

gmap.draw("d:\\sejong\\횡단보도\\map.html")
