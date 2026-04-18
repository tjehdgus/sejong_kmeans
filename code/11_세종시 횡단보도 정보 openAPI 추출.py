import requests
import pandas as pd
from google.colab import files

# API 엔드포인트
url = 'http://apis.data.go.kr/5690000/sjCrosswalkInformation/sj_00001170'

# API 요청에 필요한 파라미터 기본값 설정
params = {
    'serviceKey': '',  # 인증키
    'pageUnit': 100,
    'pageIndex': 1,
    'dataTy': 'json'
}

# 전체 데이터를 저장할 리스트 초기화
all_data = []

# 첫 번째 호출로 전체 페이지 수 계산
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    if 'body' in data and 'items' in data['body']:
        total_count = data['header']['totalCount']
        page_unit = params['pageUnit']
        total_pages = (total_count // page_unit) + (1 if total_count % page_unit != 0 else 0)

        all_data.extend(data['body']['items'])

        for page in range(2, total_pages + 1):
            params['pageIndex'] = page
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if 'body' in data and 'items' in data['body']:
                    all_data.extend(data['body']['items'])
            else:
                print(f"Error: {response.status_code} at page {page}")
                break
    else:
        print("응답 데이터에 'items'가 없습니다.", data)
else:
    print(f"Error: {response.status_code}")

# 모든 데이터를 DataFrame으로 변환
if all_data:
    df = pd.DataFrame(all_data)
    df.to_csv('crosswalk_data.csv', index=False, encoding='utf-8-sig')
    print("모든 페이지의 데이터가 성공적으로 저장되었습니다.")
    files.download('crosswalk_data.csv')
else:
    print("데이터가 없습니다.")
