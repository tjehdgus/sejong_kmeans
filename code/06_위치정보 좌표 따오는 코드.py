import pandas as pd
import requests

# Google Geocoding API 키
API_KEY = ''

# 주소를 입력 받아 위도와 경도를 반환하는 함수
def get_lat_lon(address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': address,
        'key': API_KEY
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            lat = data['results'][0]['geometry']['location']['lat']
            lon = data['results'][0]['geometry']['location']['lng']
            return lat, lon
    return None, None

# 데이터 불러오기
df = pd.read_csv('c:\\data\\필요한주차장.csv', encoding="utf-8")

# 위도, 경도를 저장할 새로운 컬럼 추가
df['위도'] = None
df['경도'] = None

# 각 주소에 대해 위도와 경도를 추출하여 저장
for idx, row in df.iterrows():
    address = row['대지위치']
    lat, lon = get_lat_lon(address)
    df.at[idx, '위도'] = lat
    df.at[idx, '경도'] = lon

# 결과를 새로운 CSV 파일로 저장
df.to_csv('c:\\data\\세종시필요한주차장위치.csv', index=False, encoding="utf-8-sig")
