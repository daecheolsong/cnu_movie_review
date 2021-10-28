#Daum News에서 페이지를 돌면서 뉴스 기사의 제목과 본문을 수집

import requests
from bs4 import BeautifulSoup
# 'https://news.daum.net/breakingnews/digital' 실제 URL 주소
# ?query_parameter


index = 0



#Page 반복
for page_number in range(1, 4):
    url = 'https://news.daum.net/breakingnews/digital?page={}'.format(page_number)
    result = requests.get(url)

    doc = BeautifulSoup(result.text, 'html.parser')
    url_list = doc.select('ul.list_news2 a.link_txt')

    # Page 내에서 뉴스목록 반복
    for url in url_list:
        index += 1 # News Count
        print('■■ NEWS -> {}번 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■'.format(index))
        new_url = url['href']
        print('# URL: {} '.format(new_url))
        result = requests.get(new_url)
        doc = BeautifulSoup(result.text, 'html.parser')
        title = doc.select('h3.tit_view')[0].get_text()  # tag 제거
        contents = doc.select('section p')  # section tag 안에 있는 p tag
        contents.pop(-1)  # 마지막 이메일 정보 삭제 remove 는 인덱스가 아님
        content = ''  # 본문 총합
        for info in contents:
            content += info.get_text()

        print('################################################')
        print('# 뉴스 제목: {}'.format(title))
        print('################################################')
        print('# 뉴스 본문: {}'.format(content))


