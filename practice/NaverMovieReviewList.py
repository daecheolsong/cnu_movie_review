# NaveMovieReviewList.py
# -> Naver 영화(1개 선택) 리뷰 정보 수집(review,score,writer,date)

import pprint
import requests
from bs4 import BeautifulSoup

url ='https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=206657&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
result = requests.get(url)
doc = BeautifulSoup(result.text,'html.parser')
review_list = doc.select('div.score_result ul li')

for i,one in enumerate (review_list):
    print('## USER  -> {} ####################################################'.format(i+1))

    # 평점 정보 수집
    score_list = one.select('div.star_score em')
    score_0 = score_list[0]
    score_text = score_0.get_text()

    review = one.select('div.score_reple p span')

    # review -> +관람객 list 길이 2  -> index[1]
    #        -> +관람객이 없는 경우 list길이 1 -> index[0]

    # if len(review) == 2:
    #  review_txt = review[1].get_text().strip()
    # elif len(review) == 1:
    #  review_txt = review[0].get_text().strip()


    j = 0 # 내용
    #pprint.pprint(review[0].get_text()) /r/n
    if len(review) == 2: #+ 관람객 내용
        j = 1
    elif len(review) == 3: #+ 관람객 스포 내용
        j = 2

    review_txt = review[j].get_text().strip()

    # 작성자(닉네임) 정보 수집
    original_writer = one.select('div.score_reple dt em')[0].get_text().strip()

    idx_end = original_writer.find('(') # (가 해당하는 idx위치 리턴
    # (xxx****) 제거
    writer = original_writer[0:idx_end]


    # 날짜 정보 수집
    original_date = one.select('div.score_reple dt em')[1].get_text()
    # yyyy.MM.dd 전처리 코드 작성
    idx_end = original_date.find(' ')
    date = original_date[0:idx_end]

    print(':: REVIEW -> {}'.format(review_txt))
    print(':: WRITER -> {}'.format(writer))
    print(':: SCORE-> {}'.format(score_text))
    print(':: DATE -> {}'.format(date))

    #review_list = one.select('div.score_reple span#_filtered_ment_{}'.format(i))
    # review_0 = review_list[0]
    # review_text= review_0.get_text()
    # review = review_text.strip()
    # print(':: REVIEW: {}'.format(review))
