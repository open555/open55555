# 자세한 온도 세분화와 옷차림 세분화는 추후에 진행할 예정 
import pandas as pd

clothing_data = {
    'temperature_range': ['추운 날씨', '적당한 날씨', '더운 날씨'],
    'tops': ['패딩, 기모제품', '자켓, 스웨터', '얇은 상의'],
    'bottoms': ['기모제품, 청바지', '슬랙스, 청바지', '반바지'],
    'footwear': ['부츠, 스니커즈', '구두, 부츠', '샌들, 슬리퍼'],
    'accessories': ['장갑, 히트텍', '모자, 스카프', '선글라스, 모자']
}

clothing_df = pd.DataFrame(clothing_data)
print(clothing_df)

# 날씨 카테고리 리스트 및 온도 구간 설정
temperature_categories = ['추운 날씨', '적당한 날씨', '더운 날씨']
temperature_ranges = [
    {'category': '추운 날씨', 'temperature_range': (-10, 10)},  # -10°C 이상 10°C 미만
    {'category': '적당한 날씨', 'temperature_range': (10, 25)},  # 10°C 이상 25°C 미만
    {'category': '더운 날씨', 'temperature_range': (25, 100)}  # 25°C 이상 100°C 미만 (100°C는 불가능하지만 예시로 포함)
]

# 온도 범주화 함수
def categorize_temperature(temp):
    for idx, temp_category in enumerate(temperature_ranges):
        if temp_category['temperature_range'][0] <= temp < temp_category['temperature_range'][1]:
            return idx  # 인덱스 반환
    return -1  # 범위에 속하지 않는 경우

# 데이터 생성
clothing_data = {
    'tops': ['패딩, 기모제품', '자켓, 스웨터', '얇은 상의'],
    'bottoms': ['기모제품, 청바지', '슬랙스, 청바지', '반바지'],
    'footwear': ['부츠, 스니커즈', '구두, 부츠', '샌들, 슬리퍼'],
    'accessories': ['장갑, 히트텍', '모자, 스카프', '선글라스, 모자']
}

# 데이터프레임 생성
clothing_df = pd.DataFrame(clothing_data)
clothing_df['temperature_category'] = range(len(temperature_categories))  # 인덱스 사용하여 온도 카테고리 지정
clothing_df.set_index('temperature_category', inplace=True)  # 인덱스 설정
print(clothing_df)

def recommend_clothing(temperature, location):
    # 온도에 따른 카테고리 결정
    temp_category = categorize_temperature(temperature)
    if temp_category == -1:
        return "온도 범위를 벗어났습니다."

    # 온도에 맞는 옷차림 추천
    tops = clothing_data['tops'][temp_category]
    bottoms = clothing_data['bottoms'][temp_category]
    footwear = clothing_data['footwear'][temp_category]
    accessories = clothing_data['accessories'][temp_category]

    # 결과 반환
    recommendation = f"장소: {location}\n온도: {temperature}°C\n\n추천 옷차림:\n상의: {tops}\n하의: {bottoms}\n신발: {footwear}\n액세서리: {accessories}"
    return recommendation

# 예시
temperature = 18
location = "서울"
print(recommend_clothing(temperature, location))


