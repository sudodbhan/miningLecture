''' 여러 줄 주석

https://velog.io/@surim014/HTTP%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

HTTP Request의 구성 요소

1. start line
HTTP 메소드 (GET, POST)와 데이터를 요청할 URL
-> 용건부터 스타트

2. 헤더(머리)
- 주로 인증 정보를 저장
- 인코딩이나 부차적인 정보가 가끔 들어감

3. 바디(몸)
- 내가 업데이트 할 정보가 있을 때 작성
(POST에서만 작성하고 GET에서는 작성 안함)

예를 들어 배민 통헤사 치킨을 시킬때 POST문으로 업데이트 시 body 주문자 정보 및 배달주소 같은게 넘어가게 됨

'''

import requests

if __name__ == '__main__':

    # 참고 중괄호 쓰는 기준
    a = 1
    b = 2
    c = 3
    # 여러개 묶어서 하고싶을 때 중괄호로 쓴다
    abc_key_value = {'key_a': 1, "key_b": 2, "key_c": 3}

    kakao_params = {'query': '오구', 'sort': 'recency', 'page': 10, 'size': 50}
    kakao_APIkey = 'KakaoAK 062eab1d406948b525f9990bde4698b3'
    kakao_header = {'Authorization':kakao_APIkey}

    response = requests.get(url="https://dapi.kakao.com/v2/search/web", params=kakao_params, headers=kakao_header)
    print("response", response) # response의 start line
    print("response.json", response.json()) # response의 내용물(body)를 json이라는 형식으로 줌
    print(abc_key_value['key_c'])
    print(response.json()["documents"][0])
    print(response.json()["documents"][0]['contents'])

    ''' header에 인증 정보가 없으면 아래와 같이 뜬다.
    response <Response [401]>
    response.json {'errorType': 'AccessDeniedError', 'message': 'cannot find Authorization : KakaoAK header'}
    '''