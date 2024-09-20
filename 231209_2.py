''' 23 - 12 - 09 2번째 강의 자료 '''
import time

import matplotlib.pyplot as plt

''' 
통계적 가설 검정 : 유의확률을 사용해서 가설을 검정하는 방법

- 기술 통계 : 데이터를 요약해서 설명하는 통계 분석 기법 
- 추론 통계 : 단순히 요약하는 것을 넘어서 어떤 값이 발생할 확률을 계산하는 분석 기법

    1) 이런 차이가 우연히 나타날 확률이 작다면 -> 성별 월급차이가 통계적으로 유의하다.
    2) 이런 차이가 우연히 나타날 확률이 크다면 -> 성별 월급차이가 통계적으로 유의하지 않다. 

- 유의 확률 : 실제로는 집단 간에 차이가 없는데 우연히 차이가 있는 데이터가 추출될 확률
    -> 유의 확률의 기준은 0.05 로 정한다.
'''

### compact 자동차와 suv 자동차의 도시 연비 t 검정
'''
t-검정 : 두 집단의 평균에 통계적으로 유의한 차이가 있는지 알아볼 때 사용하는 분석 기법
'''

import pandas as pd

path = 'C:/Python_Data/'

mpg = pd.read_csv(path + 'mpg.csv')

# 1. 기술 통계 분석
result = mpg.query('category in ["compact", "suv"]') \
    .groupby('category', as_index=False) \
    .agg(n=('category', 'count'),
         mean=('cty', 'mean'))
# print(result)

compact = mpg.query('category == "compact"')['cty']
suv = mpg.query('category == "suv"')['cty']

# t-검정
from scipy import stats

result = stats.ttest_ind(compact, suv, equal_var=True)
# print(result)
'''
TtestResult(statistic=11.917282584324107, pvalue=2.3909550904711282e-21, df=107.0)

p-value가 0.05 미만이면 '집단 간 차이가 통계적으로 유의하다.'
실제로는 차이가 없는데 이런 정도의 차이가 우연히 관찰될 확률이 5% 보다 작다면,
이 차이는 우연이라고 보기 힘들다.

pvalue=2.3909550904711282e-21
-> 유의 확률이 2.3909550904711282e-21 앞에 0이 21개 더 있는 값으로,
    0.05보다 작은 값이기 때문에 이 분석 결과는
    'compact 와 suv 간 평균 도시 연비 차이가 통계적으로 유의하다.'
'''
# --------------------------------------------------------------------------------------
'''
상관분석 - 두 연속 변수가 서로 관련이 있는지 검정하는 통계 분석 기법

- 상관계수 : 상관분석으로 도출되는 값
 -> 관련성의 정도를 0~1 사이의 값으로 표현
 -> 1에 가까울 수록 관련성이 크다.
 -> 상관계수가 양수면 정비례, 음수면 반비례 
'''

### 실업자 수와 개인 소비 지출의 상관관계
''' 가설 : 실업자 수가 증가하면 개인 소비 지출이 줄어들 것이다. '''
economics = pd.read_csv(path + 'economics.csv')

# 1. 상관 행렬
a = economics[['unemploy', 'pce']].corr()
# print(a)
# print('-'*100)
# 2. 유의 확률 구하기
b = stats.pearsonr(economics['unemploy'], economics['pce'])
# print(b)
'''
PearsonRResult(statistic=0.6145176141932082, pvalue=6.773527303289964e-61)

statistic=0.6145176141932082 : 상관계수

pvalue=6.773527303289964e-61 
-> 유의확률이 6.773527303289964e-61 로 0.05보다 작은 값을 가진다.
    그러므로, 개인 소비 지출과 실업자 수의 정비례 관계는 통계적으로 유의하다.
'''
### 상관분석 히트맵 생성

mtcars = pd.read_csv(path + 'mtcars.csv')
# print(mtcars.head())

# 1. 상관 행렬
car_cor = mtcars.corr()
# print(car_cor)
car_cor = round(car_cor, 2)
# print(car_cor)

# 2. 히트맵 생성
plt.rcParams.update({'figure.dpi': '120',
                     'figure.figsize': [7.5, 5.5]})

# 히트맵
import seaborn as sns
# sns.heatmap(car_cor,
#             annot=True, # 상관계수 표시 여부
#             cmap='RdBu') # 컬러맵
# plt.show()

# 3. 대각 행렬 제거

# 1) mask 만들기
import numpy as np

mask = np.zeros_like(car_cor)
# print(mask)

mask[np.triu_indices_from(mask)] = 1  # 오른쪽 위 대각 행렬을 1로 바꿔주는 함수
# print(mask)

# 2) 히트맵에 mask 적용
# sns.heatmap(car_cor,
#             annot=True,
#             cmap= 'RdBu',
#             mask=mask)
# plt.show()

# 3) 빈 행과 열 제거
mask_new = mask[1:, :-1]  # mask 첫 번째 행, 마지막 열 제거
cor_new = car_cor.iloc[1:, :-1]  # 상관행렬 첫 번째 행, 마지막 열 제거
# sns.heatmap(data=cor_new,
#             annot=True,
#             cmap='RdBu',
#             mask=mask_new,
#             linewidths=.5, # 경계 구분선을 추가
#             vmax=1, # 가장 진한 파란색으로 표현할 최대값
#             vmin=-1, # 가장 진한 빨간색으로 표현할 최대값
#             cbar_kws={'shrink': .5}) # 범례 크기 줄이기
# plt.show()

# ------------------------------------------------------------------------------------
''' 웹 크롤링 (Web Crawring) : 특정 사이트에서 원하는 정보를 긁어오는 행위 '''

import requests

'''
HTML :  웹 페이지의 표시를 위해 개발된 지배적인
        마크업 언어

<!DOCTYPE html>
<html>
<head>
    <title>페이지 제목</title>
</head>
<body>
    <h1> 제목 </h1>
    <p> 들어갈 문장 </p>
</body>
</html> 

- tag : 열린태그 <> 와 닫힌태그 </> 사이의 콘텐츠를 위치하여 문서의
        구조로 표현한 것
    1) h1 태그 : 문서의 제목 h1 ~ h6
    2) p 태그 : 단락을 지정할 수 있는 태그
    3) img 태그 : 이미지를 표시할 수 있는 태그, 닫힌 태그 필요 x
    4) input, button 태그 : 사용자의 입력이 필요할 때 input,
                            사용자가 클릭할 수 있는 버튼
    5)ul, ol, il 태그 : 리스트를 표현할 때 쓰는 태그
    6) div, span 태그 : 사용 시 요소가 즉각적으로 나타나는 것과는 별개로
                        화면 내에서 아무런 역할은 없지만,
                        문서 영역을 분리하거 인라인 요소를 감쌀 때
'''

### 당근 마켓 인기 매물 긁어오기
url = 'https://www.daangn.com/hot_articles'
web = requests.get(url)
# print(web.text)

'''
BeautifulSoup 라이브러리 : HTML 문서에서 원하는 부분만 추출하게 해주는 기능
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(web.content, 'html.parser')
''' 파싱 : 컴퓨터에서 번역기가 원시 부호를 기계어로 번역하는 과정의 한 단계 '''

## ul 태그의 하위 항목을 모두 뽑아오고 싶을 때
# for child in soup.ul.children:
#     time.sleep(3) # 코드를 괄호안의 초 만큼 멈추게 해주는 기능
#     print(child)

## 1. 정규식 활용하는 방법 - <ol> 이든 <ul> 이든 다 포함된 리스트를 긁어오고 싶을 때
import re

# for f in soup.find_all(re.compile('[ou]')):
#     print(f)

## 2. 리스트 활용 - 원하는 태그를 직접 지정해서 뽑는 경우 (h1, p 만 보고싶다.)
# for f in soup.find_all(['h1','p']):
#     print(f)

## 3. HTML 속성 활용 - 속성을 지정해서 뽑고 싶을 때
# a = soup.find_all(attrs={'class':'card-title'})
# # print(a)
#
# for i in a :
#     print(i)

## 4. 텍스트만 가지고 오고 싶을 때
'''
range(처음 , 끝 , 단위) : 범위 생성 함수
'''
# print(range(1, 10001, 2))
# for i in range(1, 100000000, 2):
#     print(i)

# print(soup.select('.card-title'))

for x in range(0, 10):  # 0 부터 9까지 자동 생성
    print('현재 x 값 :', x)
    print(soup.select('.card-title')[x].get_text())
    # time.sleep(5)