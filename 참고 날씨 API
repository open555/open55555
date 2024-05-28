# 날씨 API를 가지고 와 연동시켜 저희가 맞는 옷차림을 찾아 매칭시킬 예정입니다.
# 날씨 API를 연동시키는 필요한 참고 코드입니다.

import requests
import json
import datetime

vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"

service_key = "YOUR SERVICE KEY"

today = datetime.datetime.today()
base_date = today.strftime("%Y%m%d") # "20200214" == 기준 날짜
base_time = "0800" # 날씨 값

nx = "60"
ny = "128"

payload = "serviceKey=" + service_key + "&" +\
    "dataType=json" + "&" +\
    "base_date=" + base_date + "&" +\
    "base_time=" + base_time + "&" +\
    "nx=" + nx + "&" +\
    "ny=" + ny

# 값 요청
res = requests.get(vilage_weather_url + payload)

items = res.json().get('response').get('body').get('items')
#{'item': [{'baseDate': '20200214',
#   'baseTime': '0500',
#   'category': 'POP',
#   'fcstDate': '20200214',
#   'fcstTime': '0900',
#   'fcstValue': '0',
#   'nx': 60,
#   'ny': 128},
#  {'baseDate': '20200214',
#   'baseTime': '0500',
#   'category': 'PTY',
#   'fcstDate': '20200214',
#   'fcstTime': '0900',
#   'fcstValue': '0',
#   'nx': 60,
#   'ny': 128},
#      'ny': 128},
#     {'baseDate': '20200214'
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
data['weather']
# {'code': '0', 'state': '없음', 'tmp': '9'} # 9도 / 기상 이상 없음
dust_url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?"

service_key = "YOUR SERVICE KEY"

item_code_pm10 = "PM10"
item_code_pm25 = "PM25"

data_gubun = "HOUR"
search_condition = "WEEK"

payload = "serviceKey=" + service_key + "&" +\
    "dataType=json" + "&" +\
    "dataGubun=" + data_gubun + "&" +\
    "searchCondition=" + search_condition  + "&" +\
    "itemCode="

# pm10 pm2.5 수치 가져오기
pm10_res = requests.get(dust_url + payload + item_code_pm10)
pm25_res = requests.get(dust_url + payload + item_code_pm25)
# xml 파싱하기
import xml.etree.ElementTree as elemTree

pm10_tree = elemTree.fromstring(pm10_res.text)
pm25_tree = elemTree.fromstring(pm25_res.text)

dust_data = dict()
for tree in [pm10_tree, pm25_tree]:
    item = tree.find("body").find("items").find("item")
    code = item.findtext("itemCode")
    value = int(item.findtext("seoul"))
    
    dust_data[code] = {'value' : value}

# 결과 값
dust_data
# {'PM10': {'value': 94}, 'PM2.5': {'value': 71}}
# PM10 미세먼지 30 80 150
pm10_value = dust_data.get('PM10').get('value')
if pm10_value <= 30:
    pm10_state = "좋음"
elif pm10_value <= 80:
    pm10_state = "보통"
elif pm10_value <= 150:
    pm10_state = "나쁨"
else:
    pm10_state = "매우나쁨"

pm25_value = dust_data.get('PM2.5').get('value')
# PM2.5 초미세먼지 15 35 75
if pm25_value <= 15:
    pm25_state = "좋음"
elif pm25_value <= 35:
    pm25_state = "보통"
elif pm25_value <= 75:
    pm25_state = "나쁨"
else:
    pm25_state = "매우나쁨"

# 미세먼지가 나쁜 상태인지(1)/아닌지(0)
if pm10_value > 80 or  pm25_value > 75:
    dust_code = "1"
else:
    dust_code = "0"

dust_data.get('PM10')['state'] = pm10_state
dust_data.get('PM2.5')['state'] = pm25_state
dust_data['code'] = dust_code

data['dust'] = dust_data
data['dust']
#{
# 'PM10': {'value': 94, 'state': '나쁨'},
# 'PM2.5': {'value': 71, 'state': '나쁨'}
#}
# 날씨 정보
# data
{
  'weather': {
    'code': '0', 'state': '없음', 'tmp': '9'
  },
  'date': '20200214',
  'dust': {
    'PM10': {'value': 94, 'state': '나쁨'},
    'PM2.5': {'value': 71, 'state': '나쁨'},
    'code': '1'
  }
}

# 참고 : https://ai-creator.tistory.com/31
