import urllib.request  # 웹에 요청
from bs4 import BeautifulSoup  # HTML 파싱
from selenium import webdriver  # 브라우저 제어
from selenium.webdriver.chrome.service import Service  # 드라이버 관리
from selenium.webdriver.common.by import By  # 요소 탐색
import time  # 대기시간

def sp_detail_url(keyword, num):

    # 키워드 검색
    text1 = urllib.parse.quote(keyword)

    # 크롬 드라이버 경로 지정
    service = Service("c:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")

    driver = webdriver.Chrome(service=service)
    params = []  # 상세 url 저장할 리스트

    for i in range(1, num+1):

        # 웹 페이지 url 형식 정의
        list_url = f"http://www.sjpost.co.kr/news/articleList.html?page={i}&total=146&box_idxno=&sc_area=A&view_type=sm&sc_word={text1}"
        # 페이지 접속
        driver.get(list_url)  # 크롬 브라우저를 통해 위에 url로 접속
        time.sleep(5)  # 페이지가 완전히 로드 될 때까지 대기

        # 크롬 로봇이 직접 인공지능으로 검색한 페이지의 html 코드를 BS로 파싱한다.
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # 기사 상세 URL을 params 리스트에 추가한다.
        for i in soup.select('div.list-titles > a'):
            url = i.get("href")
            if url not in params:
                params.append('http://www.sjpost.co.kr/' + url)

    driver.quit()  # 작업이 끝나면 브라우저를 종료한다.

    return params


# 본문 기사 추출하는 코드
def sejong(keyword, num):

    # 조선일보 본문 저장할 텍스트 파일 생성
    f_cs = open("c:\\data\\sejong_article.txt", "w", encoding="utf8")

    # 상세 URL 가져오는 코드
    result = sp_detail_url(keyword, num)

    # 크롬 드라이버 위치 지정
    service = Service("c:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    for i in result:
        driver.get(i)  # 상세 기사 url을 하나씩 연다.
        time.sleep(5)

        # 본문 기사의 html 코드를 뽑아낸다.
        soup = BeautifulSoup(driver.page_source, "html.parser")

        for i in soup.find('div', id='article-view-content-div').find_all('p'):
            f_cs.write(i.get_text() + '\n\n')
            print(i.get_text())

    driver.quit()
    f_cs.close()


sejong("교통량", 1)
