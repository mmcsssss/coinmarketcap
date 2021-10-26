##모듈 호출을 안하려고 requests 모듈에서  request, session 함수를 특정하여 불러옴
from requests import Request, Session
#from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

##JSON을 사용하기 위해 모듈 import
import json
##CSV를 사용하기 위해 모듈 import
import csv
##pandas를 import하고 pd로 줄여서 사용
import pandas as pd

#url 불러옴
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

###body 안에 들어갈 request body 파라미터 ###
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
##필요한 데이터, api인증 키 등의 부가정보##
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'Input Your API key',
}
##세션을 가져오는 명령어를 변수 session으로 정함##
session = Session()
##헤더 정보를 사용하여 세션 업데이트##
session.headers.update(headers)

## 1.request  세션을 url과 파라미터 정보로 활성화시킴
response = session.get(url, params=parameters)

## 2. json load 서버로부터 받은 response.text를 json모듈을 이용하여 json_data 변수 지정
json_data = json.loads(response.text)

##JSON 데이터에서 data 하위 부분을 데이터프레임화(행렬화) 
df = pd.json_normalize(json_data["data"])

##7개의 항목을 제외한 모든 열 제거
df_sample = df.drop(['symbol', 'slug', 'num_market_pairs' ,'id' ,'tags' ,'platform' ,'cmc_rank' ,'last_updated' ,'quote.USD.volume_24h', 'quote.USD.percent_change_1h' ,'quote.USD.percent_change_24h' ,'quote.USD.percent_change_7d','quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d', 'quote.USD.market_cap_dominance', 'quote.USD.fully_diluted_market_cap', 'last_updated', 'platform.id', 'platform.name', 'platform.symbol', 'platform.slug', 'platform.token_address', 'quote.USD.last_updated'], axis=1)
#df_sample1 = df_sample.replace('quote.USD.price', 'price', inplace=True)

##파일 이름 사용자로부터 입력받기
fname=input("저장하고싶은 파일 이름을 입력해주세요\n")

##사용자로부터 입력받은 파일명을 .csv파일로 저장
df_sample.to_csv("D:\\TEST\\"+fname+".csv")

#print(json_data)





















'''
with open("D:\\TEST\\result.csv", "w", encoding="utf-8") as f:

  for i in range(0,5000): 
    #print(json_data["data"][i]["max_supply"], file=f)
    name = json_data["data"][i]["name"];
    date_added = json_data["data"][i]["date_added"];
    circulating_supply=json_data["data"][i]["circulating_supply"];
    market_cap = json_data["data"][i]["quote"]["USD"]["market_cap"];
    price = json_data["data"][i]["quote"]["USD"]["price"];
    total_supply = json_data["data"][i]["total_supply"];
    max_supply = json_data["data"][i]["max_supply"];
    print(json_data["data"][i]["max_supply"], file=f)
'''


## 3. parsing && make csv (file write)
'''f=open('C:\\Users\\개발1팀 이희준\\Desktop\\업무\\api업무\\max_supply.csv', 'w',  encoding="utf-8")
for i in range(0,5000): 
  print(json_data["data"][i]["max_supply"], file=f)
      wr = csv.DictWriter(f, fieldnames = info[0].keys()) '''

'''info = str(json.loads(data)['data'])

print(info[0].keys())

with open("samplecsv.csv", 'w') as f: 
    wr = csv.DictWriter(f, fieldnames = info[0].keys()) 
    wr.writeheader() 
    wr.writerows(info) 


''' 
'''
  name = json_data["data"][i]["name"];
  date_added = json_data["data"][i]["date_added"];
  circulating_supply=json_data["data"][i]["circulating_supply"];
  market_cap = json_data["data"][i]["quote"]["USD"]["market_cap"];
  price = json_data["data"][i]["quote"]["USD"]["price"];
  total_supply = json_data["data"][i]["total_supply"];
  max_supply = json_data["data"][i]["max_supply"];



  ##fwrite(fp, "%s, %s, %s, %s, %s, %s", name, date_added, circulating_supply, max_supply, market_cap, price )
  '''
#f.close()

##print(data)

#python a.py "C:\\Users\\개발1팀 이희준\\Desktop\\업무\\api업무\\max_supply.csv"
