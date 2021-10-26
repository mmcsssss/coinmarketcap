##모듈 호출을 안하려고 requests 모듈에서  request, session 함수를 특정하여 불러옴
from requests import Request, Session
#from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#import sys
#운영체제 제어 모듈
import os

##JSON을 사용하기 위해 모듈 import
import json
##CSV를 사용하기 위해 모듈 import
import csv
##pandas를 import하고 pd로 줄여서 사용
import pandas as pd

#존재 확인할 파일 이름 입력
findfname = input("존재 여부를 확인할 txt파일 이름을 입력해주세요\n")

#findfile 함수에 찾을 파일 경로+이름 입력
findfile=('D:\\TEST\\'+findfname+'.txt')



#파싱하고자 하는 txt 파일이 존재할 경우 json 파싱 후 csv 파일 저장작업으로 진입
if os.path.isfile(findfile):
  print("파일이 이미 존재합니다. api에서 다운로드 하지 않고 txt파일 내용으로 JSON 파싱을 하겠습니다.\n")
  with open("D:\\TEST\\"+findfname+".txt", "r", encoding="utf-8") as f:
    contents = f.read() # string 타입 

    #print(contents) # 출력 확인 완료
    json_data = json.loads(contents)

  ##JSON 데이터에서 data 하위 부분을 데이터프레임화(행렬화) 
  df = pd.json_normalize(json_data["data"])

  ##7개의 항목을 제외한 모든 열 제거
  df_sample = df.drop(['symbol', 'slug', 'num_market_pairs' ,'id' ,'tags' ,'platform' ,'cmc_rank' ,'last_updated' ,'quote.USD.volume_24h', 'quote.USD.percent_change_1h' ,'quote.USD.percent_change_24h' ,'quote.USD.percent_change_7d','quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d', 'quote.USD.market_cap_dominance', 'quote.USD.fully_diluted_market_cap', 'last_updated', 'platform.id', 'platform.name', 'platform.symbol', 'platform.slug', 'platform.token_address', 'quote.USD.last_updated'], axis=1)

  ##파일 이름 사용자로부터 입력받기
  fname=input("JSON 데이터 파싱이 완료되었습니다. 파싱된 데이터를 csv 파일로 저장합니다. 저장하고싶은 csv 파일 이름을 입력해주세요\n")

  ##사용자로부터 입력받은 파일명을 .csv파일로 저장
  df_sample.to_csv("D:\\TEST\\"+fname+".csv")
  print("csv 파일 저장이 완료되었습니다. 프로그램을 종료합니다")


#파싱하고자 하는 txt파일이 없을 경우 api에서 JSON데이터 다운로드 후 json 파싱 ~ csv 저장작업
else:
  print("파일이 존재하지 않습니다. api에서 데이터 다운로드를 하겠습니다.\n")
    #url 지정
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

  ###body 안에 들어갈 request body 파라미터 ###
  parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
  }
  ##필요한 데이터 형식, api인증 키 등의 부가정보##
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Input Your API Key',
  }
  ##세션을 가져오는 명령어를 변수 session으로 정함##
  session = Session()
  ##헤더 정보를 사용하여 세션 업데이트##
  session.headers.update(headers)

  ## 1.request  세션을 url과 파라미터 정보로 활성화시킴
  response = session.get(url, params=parameters)

  ## 2. json load 서버로부터 받은 response.text를 json모듈을 이용하여 json_data 변수 지정
  json_data = json.loads(response.text)

  stname = input("api에서 데이터를 불러왔습니다. 불러온 데이터를 txt파일로 저장합니다. 저장하고싶은 txt 파일 이름을 입력해주세요\n")
  with open("D:\\TEST\\"+stname+".txt", "w", encoding="utf-8") as f:
    #json.dump 사용시 "가 '로 저장되는 문제가 없음 / print(json_data)는 "가 '로 저장되어서 JSON으로 활용이 까다로워짐
    json.dump(json_data, f)
    print("파일 저장이 완료되었습니다. JSON 파싱을 시작합니다.\n")
  ##JSON 데이터에서 data 하위 부분을 데이터프레임화(행렬화) 
  df = pd.json_normalize(json_data["data"])

  ##7개의 항목을 제외한 모든 열 제거
  df_sample = df.drop(['symbol', 'slug', 'num_market_pairs' ,'id' ,'tags' ,'platform' ,'cmc_rank' ,'last_updated' ,'quote.USD.volume_24h', 'quote.USD.percent_change_1h' ,'quote.USD.percent_change_24h' ,'quote.USD.percent_change_7d','quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d', 'quote.USD.market_cap_dominance', 'quote.USD.fully_diluted_market_cap', 'last_updated', 'platform.id', 'platform.name', 'platform.symbol', 'platform.slug', 'platform.token_address', 'quote.USD.last_updated'], axis=1)
  #df_sample1 = df_sample.replace('quote.USD.price', 'price', inplace=True)

  ##파일 이름 사용자로부터 입력받기
  fname=input("JSON 파싱이 끝났습니다. 파싱된 데이터를 csv파일로 저장합니다. 저장하고싶은 csv 파일 이름을 입력해주세요\n")

  ##사용자로부터 입력받은 파일명을 .csv파일로 저장
  df_sample.to_csv("D:\\TEST\\"+fname+".csv")
  print("csv 파일 저장이 완료되었습니다. 프로그램을 종료합니다.")