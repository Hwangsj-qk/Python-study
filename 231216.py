''' 23 - 12 - 16 강의 자료 '''
import time

import pandas as pd

'''
웹 크롤링 : 웹에서 필요한 정보를 긁어오는 행위

BeautifulSoup 라이브러리 : 인터넷 문서 구조에서 명확한 데이터를 추출하고 처리하는 가장 쉬운 라이브러리
'''

### 1. find() 로 태그 추출
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

a = urlopen('https://www.naver.com/')
# a 를 호출해서 html 을 parser
soup = BeautifulSoup(a.read(), 'html.parser')
# soup 에서 h1 태그 하나를 가져온다.
# print(soup.find('h1'))

### 2. find_all() : 기준에 맞는 태그를 모두 가져오기 때문에 리스트 타입으로 결과를 내준다.
# print(soup.find_all('div'))
#
# for i in soup.find_all('div'):
#     print(i)
#     time.sleep(3)

## 2-1 해당 태그의 class 기준으로 가져오기
# soup에서 div 태그의 class가 corp_area인 태그를 가져온다.
# b = soup.find_all("ul", '클래스명')
# print(b)

## 2-2 해당 태그의 id 기준으로 가져오기
# c = soup.find_all('div', {'id':'account'})
# print(c)

### 3. select() 함수 : 옵션을 사용해서 원하는 데이터 추출
# d = soup.select('h1')
# print(d)

## 3-1 select('.클래스명')
b = urlopen('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%B0%ED%9B%84%EC%A1%B0%EB%A6%AC').read()
soup = BeautifulSoup(b, 'html.parser')

# for tag in soup.select('.news_tit'):
#     print(tag.get_text())

## 3-2 select('상위태그 > 하위태그 > 하위태그')
# for tag in soup.select('div > a'):
#     print(tag)

## 3-3 select('상위태그 > 하위태그.클래스명')
# for tag in soup.select('div > a.api_txt_lines.dsc_txt_wrap'):
#     print(tag.get_text())

## 3-4 select('#아이디명')
# for tag in soup.select('#snb'):
#     print(tag.get_text())

## 3-5 select('#아이디명 > 태그명.클래스명')
# for tag in soup.select('#sp_nws1 > div.news_area'):
#     print(tag)

## 3-6 select('태그명[속성=값]')
# for tag in soup.select('a[href="/p/crd/rd?m=1&amp;px=413&amp;py=710&amp;sx=413&amp;sy=510&amp;p=iU0DCwqo1LVssTi4uLRssssstDK-357572&amp;q=%EC%82%B0%ED%9B%84%EC%A1%B0%EB%A6%AC&amp;ie=utf8&amp;rev=1&amp;ssc=tab.news.all&amp;f=news&amp;w=news&amp;s=LiYdNxFVSVdqd%2B%2Bom8Y2senw&amp;time=1702701000642&amp;abt=%5B%7B%22eid%22%3A%222%22%2C%22vid%22%3A%2210%22%7D%2C%7B%22eid%22%3A%22SBR1%22%2C%22vid%22%3A%221656%22%7D%2C%7B%22eid%22%3A%22SFR-EXP%22%2C%22vid%22%3A%224%22%7D%5D&amp;a=nws*f.body&amp;r=1&amp;i=88184457_000000000000000000101228&amp;g=5652.0000101228&amp;u=https%3A%2F%2Fwww.businesskorea.co.kr%2Fnews%2FarticleView.html%3Fidxno%3D207922"]'):
#     print(tag)

'''
HTML : 웹 페이지의 모습을 표현하기 위한 마크업 언어

CSS : HTML로 작성한 문서를 웹 브라우저에 표현할 때,
    서식을 지정해주는 언어

CSS 선택자 : 요소 선택자, ID 선택자, class 선택자

CSS 결합자 : 선택자들을 다양하게 조합
'''

''' yes24 월별 베스트셀러 웹 크롤링 '''
html = urlopen('https://www.yes24.com/Product/Category/MonthWeekBestSeller?categoryNumber=001')
book = BeautifulSoup(html, 'html.parser')

title = book.find_all('a', {'class':'gd_name'})
# print(title)

writer = book.find_all('span', {'class':'authPub info_auth'})
# print(writer)

price = book.find_all('strong', {'class':'txt_num'})

title_list = []
writer_list = []
new_writer_list = []
price_list = []

for i in title:
    # print(i.get_text()) # 텍스트만 가져오기
    title_list.append(i.get_text()) # append() : 리스트 요소 추가함수

# print(title_list)

for w in writer:
    writer_list.append(w.get_text())

# print(writer_list)

for p in price:
    price_list.append(p.get_text())

# print(price_list)

# print(len(title_list))
# print(len(writer_list))
# print(len(price_list))

## -------저자리스트 요소에서 줄바꿈, 공백, 필요없는 문자 제거-------
for wt in writer_list:
    # print(wt)
    # print('-'*30, len(wt))
    if len(wt) > 100: # 정보 더 보기를 포함하는 wt 의 조건
        a = wt.split('감추기')[-1] # 뒤에 요소만 가져와서 a 저장
        # print(a)
        a = a.lstrip() # 왼쪽의 모든 공백, 줄바꿈 제거해주는 함수
        a = a.rstrip() # 오른쪽의 모든 공백, 줄바꿈 제거해주는 함수
        # print(a)
        a = a.replace('\n',',')
        # print(a)
        new_writer_list.append(a)

    else: # 위의 if 가 아닌 모든 경우
        new_wt = wt.lstrip()
        new_wt = new_wt.rstrip()
        # print(new_wt)
        new_wt = new_wt.replace('저','') # 저 제거
        new_wt = new_wt.replace('역','') # 역 제거
        new_wt = new_wt.replace('감수','') # 감수 제거
        # print(new_wt)
        new_wt = new_wt.replace('벤민 하디 /최은아','벤저민 하디/최은아')
        # print(new_wt)
        new_wt = new_wt.replace('\r','')
        new_wt = new_wt.replace('\n', '')
        # print(new_wt)
        new_writer_list.append(new_wt)

# -------------------- 리스트 확인 --------------------------
# print(title_list)
# print(len(title_list))
#
# print(new_writer_list)
# print(len(new_writer_list))
#
# print(price_list)
# print(len(price_list))

# -------------------- 데이터 생성 --------------------------
df = pd.DataFrame({
    '책 제목':title_list,
    '저자':new_writer_list,
    '책 가격':price_list
})
# print(df)

# -------------------- 엑셀로 저장 --------------------------
df.to_excel('yes24.xlsx')
