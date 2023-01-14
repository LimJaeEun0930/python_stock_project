import requests
import zipfile
import json
import dart_fss as dart
api_key = "22bdee0a83989a1d67be8aef7fbd914deb34129a"

res = requests.get("https://opendart.fss.or.kr/api/fnlttMultiAcnt.json",
                   params={"crtfc_key": api_key,"corp_code":"00126380" ,"bsns_year":"2022","reprt_code": "11014"})
#다중회사 주요계정 개발가이드 요청 URL과 params에는 crtfc_key(API인증키),corp_code(회사고유번호),bsns_year(사업연도),reprt_code(보고서코드.몇분기인지) 등의 정보가 들어있다.


f = res.json() #f는 바로 dic타입이 된다.
# dic = json.loads(f)
lis = f['list'] #[객체] . 배열안에 객체가 하나 있는 형태. f['list'][0]은 객체가 된다.

print(lis) # type: list

print(f['list'][0]) # type:#dictionary  #여기에 기업정보(유동자산,종목코드 등..)이 한꺼번에 들어있다. 가공필요

print(lis[0]['rcept_no']) #f['list'][0]객체안에 'rcept_no'키값을 넣어서 20221114001832라는 밸류를 얻었다.
