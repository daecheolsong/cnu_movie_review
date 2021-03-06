import math

import requests
from bs4 import BeautifulSoup

url ='https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=184311&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result =requests.get(url)
docs = BeautifulSoup(result.text,'html.parser')
page_number = docs.select('div.score_total em')[0].get_text()
page_number = page_number.replace(',','')
page = math.ceil(int(page_number)/10)
print(page)

count = 0

for page in range(1, page+1):

    new_url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=184311&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}'.format(page)
    result = requests.get(new_url)
    doc = BeautifulSoup(result.text, 'html.parser')
    review_list = doc.select('div.score_result ul li')

    for one in review_list:
        count += 1
        print('## USER  -> {} ####################################################'.format(count))

        # 평점 정보 수집
        score_list = one.select('div.star_score em')
        score_0 = score_list[0]
        score_text = score_0.get_text()

        # 리뷰 정보 수집
        review = one.select('div.score_reple p span')[-1].get_text().strip()

        # 작성자(닉네임) 정보 수집
        original_writer = one.select('div.score_reple dt em')[0].get_text().strip()

        idx_end = original_writer.find('(')  # (가 해당하는 idx위치 리턴
        # (xxx****) 제거
        writer = original_writer[0:idx_end]

        # 날짜 정보 수집
        original_date = one.select('div.score_reple dt em')[1].get_text()
        # yyyy.MM.dd 전처리 코드 작성
        idx_end = original_date.find(' ')
        date = original_date[0:idx_end]

        print(':: REVIEW -> {}'.format(review))
        print(':: WRITER -> {}'.format(writer))
        print(':: SCORE-> {}'.format(score_text))
        print(':: DATE -> {}'.format(date))

