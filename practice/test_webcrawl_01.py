"""
web crawling  --> 웹 사이트에서 내가 원하는 정보를 긁어온다(수집)

웹 브라우저(개인 pc)           웹 서버(NAVER)
 --> NAVER 웹 사이트            : 이미지, 텍스트, 내용, ~~~~

https://www.naver.com  -> request  -> 메인사이트 소스(이미지, 동영상, 텍스트)
네이버 소스 렌더링        <-  response  <-

HTML
#: ID 선택자
.: Class 선택자

"""
# 웹 크롤링 => 다음 뉴스

import requests
from bs4 import BeautifulSoup

# requests => 웹사이트 코드 복사 GET

# BeautifulSoup4 => request GET 해온 코드에서 필요한 정보만 find 해서 가져오기

url = 'https://news.v.daum.net/v/20211021152915953'
result = requests.get(url)

# result.text

doc = BeautifulSoup(result.text,'html.parser')
#title = doc.select('h3.tit_view') # 중복을 위해 list 로 반환
#title2 = doc.select('h3.tit_view')[0]
title3 = doc.select('h3.tit_view')[0].get_text()

#print(title)
#print(title2)
print('# 뉴스 제목:{}'.format(title3))


