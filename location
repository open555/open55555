# 지역의 위도와 경도를 입력하면 온도와 날씨정보가 뜨게끔 하는 코드

import requests
import datetime

API_Key = "GnN6ZfisAdn3qQa34ktd+Z+++jaBYfhYjNgg7h3tlIwDdm+3H2MxKqDJrN9QC6WC4kQoC8yckS3Qgwm9CqzoSQ=="
URL = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

today = datetime.datetime.today()
base_date = today.strftime("%Y%m%d")
base_time = "0800"

nx = input("격자 좌표 nx 값을 입력하세요: ")
ny = input("격자 좌표 ny 값을 입력하세요: ")
# 제주도 53 38, 서울 60 127

params = {
    "serviceKey": API_Key,
    "dataType": "json",
    "base_date": base_date,
    "base_time": base_time,
    "nx": nx,
    "ny": ny,
    "numOfRows": 10,
    "pageNo": 1
}

res = requests.get(URL, params=params)

items = res.json().get('response').get('body').get('items')

data = dict()
data['date'] = base_date

weather_data = dict()
for item in items['item']:
    # 기온
    if item['category'] == 'TMP':
        weather_data['tmp'] = item['fcstValue']

    # 기상상태
    if item['category'] == 'PTY':

        weather_code = item['fcstValue']

        if weather_code == '1':
            weather_state = '비'
        elif weather_code == '2':
            weather_state = '비/눈'
        elif weather_code == '3':
            weather_state = '눈'
        elif weather_code == '4':
            weather_state = '소나기'
        else:
            weather_state = '없음'

        weather_data['code'] = weather_code
        weather_data['state'] = weather_state

data['weather'] = weather_data

print(f"격자 좌표 ({nx}, {ny})의 오늘 기온:", weather_data.get('tmp', '정보 없음'), "도")
print(f"격자 좌표 ({nx}, {ny})의 오늘 날씨 상태:", weather_data.get('state', '정보 없음'))
