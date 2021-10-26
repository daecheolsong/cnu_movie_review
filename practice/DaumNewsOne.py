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
result = requests.get(url) # response [200] 200:success

# result.text

doc = BeautifulSoup(result.text,'html.parser')
# doc.select('h3.tit_view') # 중복을 위해 list 로 반환
# doc.select('h3.tit_view')[0]
# . -> class tag 구별하기 위함 # -> id
title = doc.select('h3.tit_view')[0].get_text() # tag 제거
contents = doc.select('section p') # section tag 안에 있는 p tag
contents.pop(-1) # 마지막 이메일 정보 삭제 remove 는 인덱스가 아님




#print(contents) list
# len(contents) section 안에 있는 p tag 개수

content = '' # 본문 총합
for info in contents:
    content += info.get_text()

print('################################################')
print('# 뉴스 제목: {}'.format(title))
print('################################################')
print('# 뉴스 본문: {}'.format(content))
