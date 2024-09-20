''' 23 - 12 - 09 강의 자료 '''

''' - Review 

1. 데이터 가공
    1) query() : 행 추출
    2) df['변수명'] : 열 추출
    3) sort_values() : 정렬
    4) groupby() : 집단별로 나누기
    5) assign() : 파생 변수 추가
    6) agg() : 통계치 산출 - 평균, 최대값....
    7) merge() : 데이터 합치기(열), 매칭
    8) concat() : 데이터 합치기(행)

2. 데이터 정제
    1) 결측치 : 누락된 값, 비어있는 값 - 파이썬에서 NaN 
        - 확인 : pd.isna()
        - 제거 : df.dropna(subset=['변수명'])
    2) 이상치 : 이상한 수치, 정상범위에서 크게 벗어난 값
        - 상자 그림 sns.boxplot

3. 그래프
    1) sns.scatterplot() : 산점도
    2) sns.barplot() : 막대 그래프 - 요약표 활용
    3) sns.countplot() : 빈도 막대 그래프 - 원래 자료 활용
    4) sns.lineplot() : 선 그래프
    5) sns.boxplot() : 상자 그림
'''

# ------------------------------------------------------------------
''' 아나콘다 가상환경 다루는 명령어 '''
'''
- 가상환경이 필요한 이유
: 독립적인 작업환경에서 작업을 할 수 있다.

1. 가상환경 리스트 확인
conda env list

2. 가상환경 생성
conda create -n 가상환경이름

3. 가상환경 활성화
conda activate 가상환경이름

4. 가상환경에 존재하는 패키지 확인
conda list
conda install 패키지명 ( python, pip 가 자동으로 설치된다.)

5. 가상환경 삭제
conda env remove -n 가상환경이름
'''
# -----------------------------------------------------------------
''' 텍스트 마이닝 : 문자 데이터에서 가치 있는 정보를 얻어 내는 분석 기법 '''
'''
- 초기 세팅
1. command prompt -> python --version

2. 1.7버전 이상의 자바 필요
https://www.oracle.com/java/technologies/downloads/

아래로 스크롤 -> windows -> x64 installer 설치

3. 패키지 설치
pip install jpype1
pip install konlpy
'''

# from konlpy.tag import Komoran
# komoran = Komoran()
# print(komoran.morphs('한글형태소분석기 코모란 테스트 중 입니다.'))

### 가장 많이 사용된 단어 알아보기
# path = 'C:/Python_Data/'
# moon = open(path + 'speech_moon.txt', encoding='UTF-8').read()
# print(moon)

# 1. 불필요한 문자 제거
# import re
# moon = re.sub('[^가-힣]', ' ', moon)
# print(moon)

# 2. 명사만 추출
# import konlpy
# hannanum = konlpy.tag.Hannanum()
# a = hannanum.nouns('대한민국의 영토는 한반도와 그 부속 도서로 한다.')
# print(a)

# 연설문에서 명사 추출
# nouns = hannanum.nouns(moon)
# print(nouns)

# 데이터 프레임으로 변환
# import pandas as pd
# df_word = pd.DataFrame({'word':nouns})
# print(df_word)

# 3. 단어 빈도표 생성
# df_word['count'] = df_word['word'].str.len()
# print(df_word)

# 두 글자 이상 단어만 남기기
# df_word = df_word.query('count >= 2')
# print(df_word.sort_values('count'))

# 단어의 빈도 구하기
# df_word = df_word.groupby('word', as_index=False) \
#     .agg(n = ('word', 'count')) \
#     .sort_values('n', ascending=False) # 내림차순
# print(df_word)

# 4. 단어 빈도 막대 그래프 생성
# top20 = df_word.head(20)
# print(top20)

import seaborn as sns
import matplotlib.pyplot as plt

# plt.rcParams.update({'font.family' : 'Malgun Gothic'})

# 막대 생성
# sns.barplot(data=top20, y='word', x='n')
# plt.show()

### 워드 클라우드

# 1. 한글 폰트 설정
# font = 'C:/Windows/Fonts/HMKMMAG.ttf'

# 2. 단어와 빈도를 담은 딕셔너리 생성
# dic_word = df_word.set_index('word').to_dict()['n']
# print(dic_word)

# 3. 워드클라우드 생성
# from wordcloud import WordCloud
# wc = WordCloud(random_state=1234,
#                font_path=font,
#                width=400,
#                height=400,
#                background_color='white')
#
# img_wordcloud = wc.generate_from_frequencies(dic_word) # 워드클라우드 생성

# 출력
# plt.figure(figsize=(10,10))  # 가로 세로 크기
# plt.axis('off') # 축 표시안하는 옵션
# plt.imshow(img_wordcloud) # 워드 클라우드 출력
# plt.show()

### 워드 클라우드 모양 바꾸기

# 1. mask 만들기
# import PIL # 이미지 처리 패키지
# icon = PIL.Image.open(path + 'cloud.png')

# import numpy as np
# img = PIL.Image.new('RGB', icon.size, (255,255,255))
# img.paste(icon, icon)
# img = np.array(img)
# print(img)

# 2. 워드 클라우드 만들기
# wc = WordCloud(random_state=1234,  # 난수 고정
#                font_path=font, # 폰트 설정
#                width=400, # 가로
#                height=400, # 세로
#                background_color='white', # 배경색
#                mask=img, # 마스킹 이미지 선택
#                colormap='inferno') # 컬러맵 설정
'''https://seaborn.pydata.org/generated/seaborn.color_palette.html '''
# img_wordcloud = wc.generate_from_frequencies(dic_word)

# 출력
# plt.figure(figsize=(10,10))
# plt.axis('off')
# plt.imshow(img_wordcloud)
# plt.show()

### 기사 댓글 텍스트 마이닝
import pandas as pd
path = 'C:/Python_Data/'
df = pd.read_csv(path + 'news_comment_BTS.csv', encoding='UTF-8')

# print(df.info())
# print(df[['reply','title']])

# 2. 불필요한 문자 제거
df['reply'] = df['reply'].str.replace('[^가-힣]', '', regex = True)
# print(df['reply'].head())

# 3. 명사 추출
import konlpy
kkma = konlpy.tag.Kkma()

# nouns = df['reply'].apply(kkma.nouns)
''' 
.apply() : 함수가 각 행을 따로따로 처리할 수 있게 도와주는 함수
'''
# print(nouns)

# 4. 단어 빈도표 생성
# nouns = nouns.explode() # 한 행에 한 단어만 들어가게 설정
# print(nouns)

# 데이터 프레임 생성
# df_word = pd.DataFrame({'word':nouns})

# 글자 수 추가
# df_word['count'] = df_word['word'].str.len()

# 두 글자 이상 단어만 남기기
# df_word = df_word.query('count >= 2')
# print(df_word)

# 빈도표 생성
# df_word = df_word.groupby('word', as_index=False) \
#     .agg(n = ('word', 'count')) \
#     .sort_values('n', ascending=False)
# print(df_word)

# 5. 단어 빈도 막대 그래프 생성
# top20 = df_word.head(20)
# print(top20)

# 막대 그래프 가로 세로 크기 설정
# plt.rcParams.update({'figure.figsize' : [6.5, 6]})
# plt.rcParams.update({'font.family' : 'Malgun Gothic'})

# 막대 그래프 생성
# sns.barplot(data=top20, y='word', x='n')
# plt.show()

### 워드 클라우드 생성 (방탄)
# dic_word_bts = df_word.set_index('word').to_dict()['n']

# wc 생성
from wordcloud import WordCloud
# 한글 폰트 설정
# font = 'C:/Windows/Fonts/HMKMMAG.ttf'

# mask 만들기
# import PIL # 이미지 처리 패키지
# icon = PIL.Image.open(path + 'cloud.png')
#
# import numpy as np
# img = PIL.Image.new('RGB', icon.size, (255,255,255))
# img.paste(icon, icon)
# img = np.array(img)
#
# wc = WordCloud(random_state=1234,  # 난수 고정
#                font_path=font, # 폰트 설정
#                width=400, # 가로
#                height=400, # 세로
#                background_color='white', # 배경색
#                mask=img, # 마스킹 이미지 선택
#                colormap='inferno') # 컬러맵 설정

# 방탄 워드 클라우드 생성
# img_wordcloud = wc.generate_from_frequencies(dic_word_bts)

# 출력
# plt.figure(figsize=(10,10))
# plt.axis('off')
# plt.imshow(img_wordcloud)
# plt.show()