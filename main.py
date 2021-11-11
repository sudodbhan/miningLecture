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

# (0) 자료형은 데이터를 저장하는 형태

# (1) list 자료형
# 난 dict랑 다르게 key가 아니라 순서대로 가지고 올래
def studyList():
    # step1: 빈 리스트 만들기
    dataList = list()

    # step2: 리스트에 데이터 넣기
    dataList.append(1) #dataList[0]
    dataList.append(2) #dataList[1]
    dataList.append(3) #dataList[2]
    dataList.append(4) #dataList[3]
    dataList.append("한다빈") #dataList[4]
    dataList.append("송수윤") #dataList[5]

    # step3: data 출력해보기
    print("한다빈") # print(dataList[4])
    print(dataList[5])
    print(dataList)
    print(len(dataList))


    # step4: 리스트 안에 리스트 넣어보기
    subDataList = list()
    subDataList.append("market data")
    subDataList.append("financial data")
    subDataList.append("consumer report data")

    dataList.append(subDataList)
    print(subDataList)
    print(dataList)

    # step5: 리스트 안에 dict(dictionary) 넣기
    dataDict = dict()
    dataDict["상품 개수"] = 100
    dataDict["상품 가치"] = 10000
    dataDict["시장성"] = "70%"

    dataList.append(dataDict)
    print(dataDict)
    print(dataList)

# (2) dict 자료형 (key - value 자료형)
# 난 list랑 다르게 순서가 아닌 key로 가지고 올거야
def studyDict():
    # dict 자료형은 dictionary의 줄임말
    # dict 자료형은 색인을 이용한다고 생각하면 됨 -> key가 색인의 역할을 한다.

    bigDict = dict()
    print(bigDict)

    bigDict['data_key'] = "data_value" # data는 data_value이고 data_key data_value이고 찾아가기 위한 색인일 뿐
    print(bigDict)
    print(bigDict['data_key'])

    bigDict['송수윤의 여자친구'] = 29
    bigDict['한다빈의 여자친구'] = 30
    bigDict['이준혁의 여자친구'] = 23

    print(bigDict)
    print(bigDict['송수윤의 여자친구'])

    bookInfoDict = dict()
    bookInfoDict['Title'] = "계량경제학"
    bookInfoDict['Contents'] = "선형 회귀 분석 및 기초 통계학에 대해서 다룬다."
    bookInfoDict['MonetaryValue'] = 50000
    bookInfoDict['Currency'] = "won"
    bookInfoDict['Page'] = 400

    print(bookInfoDict)

    bigDict["book1"] = bookInfoDict

    print(bigDict)
    print(bigDict["book1"]["Title"])
    book1_dict = bigDict["book1"]
    print(book1_dict["Title"]) # bigDict["book1"]["Title"] 랑 똑같음


# 함수 접기 ctrl + .
def requestKaKaoAPI():
    kakao_params = {'query': '오구', 'sort': 'recency', 'page': 10, 'size': 50}
    kakao_APIkey = 'KakaoAK 062eab1d406948b525f9990bde4698b3'
    kakao_header = {'Authorization':kakao_APIkey}

    response = requests.get(url="https://dapi.kakao.com/v2/search/web", params=kakao_params, headers=kakao_header)
    # print("response", response) # response의 start line
    # print("response.json", response.json()) # response의 내용물(body)를 json이라는 형식으로 줌
    # print(response.json()["documents"][0])
    # print(response.json()["documents"][0]['contents'])

    ''' header에 인증 정보가 없으면 아래와 같이 뜬다.
    response <Response [401]>
    response.json {'errorType': 'AccessDeniedError', 'message': 'cannot find Authorization : KakaoAK header'}
    '''
    return response

def returnOne() :
    return 1 # returnOne()은 결국 1이 된다.

def returnTwo():
    a = 2
    b = 4
    c = a+b

    return 2 # returnTwo() 위에서 무슨 짓을해도 결국 2가 된다.

def returnString():
    return "산업은행"

def returnParams(parameter):
    return parameter


# data를 입맛대로 자르고 noise를 제거하는걸 파싱이라고 함
def parsingJsonResponse(response):
    json_response = response.json()
    list_data = json_response["documents"]
    # print("[list_data]:", list_data)
    # print("[list_data size]:", len(list_data))
    # print("list_data[0]:", list_data[0])
    # print("[contents]:", list_data[0]['contents'])
    # print("[datetime]:", list_data[0]['datetime'])
    # print("[title]:", list_data[0]['title'])
    # print("[url]:", list_data[0]['url'])


    # for data_dict in list_data:
    #     print(data_dict["contents"])

    for data_dict in list_data:
        print(data_dict["url"])


if __name__ == '__main__':

    respones_return = requestKaKaoAPI()
    parsingJsonResponse(respones_return)

    # studyList()
    # studyDict()

    # one = returnOne()
    # print(one)
    #
    # a = returnTwo()
    # print(a)
    #
    # b = returnString()
    # print(b)
    #
    # ret1 = returnParams(1001)
    # print(ret1)
    #
    # ret2 = returnParams("송수윤")
    # print(ret2)
    #
    # ret3 = returnParams(returnOne())
    # print(ret3)

    # # 참고 중괄호 쓰는 기준
    # a = 1
    # b = 2
    # c = 3
    # # 여러개 묶어서 하고싶을 때 중괄호로 쓴다
    # abc_key_value = {'key_a': 1, "key_b": 2, "key_c": 3}
    # print(abc_key_value['key_c'])
    #
    # requestKaKaoAPI()