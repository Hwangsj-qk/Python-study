import matplotlib.pyplot as plt

# 변수명
a = 1
b = 2
c = 3
d = 3.5

# print(a+b)
# print(a+b+c)
# print(4/b)
# print(5*b)

# 문자열 변수
str1 = 'a'
str2 = '가을 하늘 "공활"한데'
# print(str2)

# 리스트
## 1. 숫자 리스트
var1 = [1,2,3]
# print(var1)
var2 = [4,5,6]
# print(var2)
# print(var1 + var2)

## 2. 문자열 리스트
str3 = ['a', 'b', 'c']
# print(str3)
str4 = ['Hello', 'World is', 'Good!']
# print(str4)
# print(str2 + str4)
## → 문자열 리스트와 문자열 변수는 더하기가 안됨

### 문자열 더하기 연산 = 문자열을 합한 결과
# print('15' + '50') #문자열 "15" 와 문자열 "50" 더하기 = 1550
# print(15+50) # 숫자 15 + 숫자 50 더하기 = 65

# print(str1 + 2) # 문자열 + 숫자는 에러 발생

### 리스트의 인덱싱과 슬라이싱
list1 = [1,2,3,4,55,66,77]
# print(list1[4]) # 55 출력 → 리스트는 제일 앞에서부터 0번지로 출발
a = list1[-2] # 인덱싱, 인덱스(index)는 값의 위치
# print(a) # 66 출력 → 리스트는 제일 뒤에서부터 -1번지로 출발

b = list1[3:6]
''' 슬라이싱 [시작 지점 인덱스:끝 지점 인덱스 -1]'''
# print(b) # 4(3),55(4),66(5) 출력 ※ 주의: 마지막 인덱스는 출력되지 않음
#-----------------------------------------------------------------------------
## 함수 사용
'''
함수 예시
sum() : 합계 함수
max() : 최댓값 구하는 함수
'''
x = [1,2,3]
# print(sum(x)) # 6

### ※ 일반적으로 함수의 결과물은 새 변수 생성 후 활용
x_sum = sum(x)
print(x_sum)
#---------------------------------------------------------------------------
'''패키지(Package) : 변수와 함수들의 꾸러미
패키지 설치 -> 패키지로드 -> 함수 사용
아나콘다에 주요 패키지가 대부분 들어있어 사용 가능함
'''

### 패키지 로드 : import 라는 구문 뒤에 패키지명을 써준다.
import seaborn
import matplotlib as plt # 관례적으로 matplotilb 이라는 라이브러리의 약어로 plt로 쓴다

### 패키지 함수 사용
# countplot() : 빈도 막대 그래프 함수
var = ['a', 'a', 'b', 'c']
# seaborn.countplot(x=var)
# plt.show()

import seaborn as sns

# sns.countplot(x=var)
# plt.show()

'''
seaborn 라이브러리의 예제 데이터 titanic 데이터 셋
-> 1912년 영국 출발 미국 뉴욕가던 배가 침몰 그때 당시의 승객 정보
'''
df = sns.load_dataset('titanic')
# print(df)

# sns.countplot(data=df, x='alive')
# plt.show()

### countplot의 여러기능
''' 주제 : 객실의 등급에 따라 생존여부가 다를까 ? '''
# sns.countplot(data=df, x='class')
# sns.countplot(data=df, x='class', hue='alive') # hue : 변수 항목별로 막대의 색을 다르게 표현
# sns.countplot(data=df, y='class', hue='alive') # 막대그래프 눕히기
# plt.show()
# --------------------------------------------------------------------------------------------
'''
모듈(Module) : 변수와 함수들의 모음, 어떤 패키지는 함수가 너무 많아서 비슷한 함수끼리
                묶어서 몇개의 모듈로 나뉘어 있다, 모듈은 .py로 끝나는 파일을 말한다.
'''
# ### sklearn 의 metrics 모듈 로드
# import sklearn.metrics
#
# ### 모듈 함수 사용법
# sklearn.metrics.accuracy_score()
#
# ## 모듈명.함수명() 으로 사용하기
# from sklearn import metrics
# metrics.accuracy_score()
#
# ## 함수명() 으로 사용하기 - 단일 함수를 쓸 때
# from sklearn.metrics import accuracy_score, precision_score
# accuracy_score() # 모델 정확도 함수
# precision_score()
#
# ## 약어 지정
# import sklearn.metrics as met
# met.accuracy_score()

### 패키지 설치
''' 
Command Prompt (본인 아나콘다 가상환경) -> pip install 패키지명 

- pip : 파이썬 설치 명령어 (모듈)
'''

import pydataset

# print(pydataset.data()) # 데이터셋 목록

df = pydataset.data('HairEyeColor')  # 헤어아이컬러 데이터를 변수에 저장
# print(df) # 출력
# --------------------------------------------------------------------------------------------
### 데이터 프레임 생성
''' pandas : 파이썬의 데이터 가공 패키지 '''
import pandas as pd

'''
딕셔너리(dict) : 사전, 키와 값의 쌍으로 구성된 자료형

    dict1 = { Key1 : Value1,
              Key2 : Value2 }

'''

df = pd.DataFrame({'name': ['김지훈', '이유진', '박동현', '마동석'],
                   'english': [90, 80, 60, 70],
                   'math': [50, 60, 100, 20]})
# print(df)

### 만든 데이터로 간단하게 분석

## 1. 특정 변수의 값 추출 - 데이터 프레임 명[문자형태로 변수명을 입력]
# print(df['english'])

## 2. 변수의 값으로 합계 구하기 - 영어 점수를 구하는 코드를 sum 함수에 넣으면 된다.
# result = sum(df['english'])
# print(result)

## 3. 변수의 값으로 평균 구하기
# print(sum(df['english']) / 4)
# print(sum(df['english']) / len(df['english'])

'''
len() : 괄호안의 값이나 변수의 길이를 구해주는 함수
'''
# y = [1,2,3,4,5]
# print('y 리스트의 길이:' , len(y)) # print 함수 안에 여러개의 값을 나열하거나 문자열을 쓰는게 가능하다.

# --------------------------------------------------------------------------------------------
### 엑셀 파일 로드
path = 'C:/Python_Data/'
# print(path + 'excel_exam.xlsx')

df_exam = pd.read_excel(path + 'excel_exam.xlsx') # 엑셀 파일 불러와서 df_exam 변수에 저장
# print(df_exam)

## 영어 점수와 과학 점수의 전체 평균 비교
result1 = sum(df_exam['english']) / len(df_exam) # 데이터 프레임의 길이 = 행의 개수
# print('영어 점수 평균 :',result1)

result2 = sum(df_exam['science']) / len(df_exam)
# print('과학 점수 평균 :',result2)

## 엑셀 파일의 첫 번째 행이 변수명이 아닌 경우
df_exam_novar = pd.read_excel(path + 'excel_exam_novar.xlsx', header=None)
# print(df_exam_novar)

## 엑셀 파일에 시트가 여러개인 경우
# 1. sheet2 시트의 데이터 불러오기
df_exam = pd.read_excel(path + 'excel_exam.xlsx', sheet_name='sheet2') # sheet2 라는 제목을 가진 시트
# df_exam = pd.read_excel(path + 'excel_exam.xlsx', sheet_name=2) # 두번째 시트

### CSV 파일 로드
df_csv_exam = pd.read_csv(path + 'exam.csv')
# print(df_csv_exam)

### 데이터 프레임을 CSV로 저장
df_mid = pd.DataFrame({
     'english' : [90,80,70,60],
     'math' : [50,60,100,20],
     'class' : [1,2,2,1]
 })
# print(df_mid)

df_mid.to_csv('output_new.csv', index=False) # 인덱스 번호 저장 여부
# --------------------------------------------------------------------------------------------
'''
- 데이터 파악 함수
1. head() : 윗 부분 출력
2. tail() : 뒷 부분 출력
3. shape : 행, 열의 개수 출력
4. info() : 변수 속성 출력
5. describe() : 요약 통계량 출력
'''
import pandas as pd

path = 'C:/Python_Data/'
exam = pd.read_csv(path + 'exam.csv')

### exam 데이터 파악

# print(exam.head())
# print(exam.head(10)) # 앞에서부터 10행까지 출력

# print(exam.tail())
# print(exam.tail(10)) # 뒤에서부터 10행까지 출력

# print(exam.shape)

# print(exam.info())

# print(exam.describe())

### mpg 데이터 파악
'''
mpg 데이터 : 미국 환경 보호국에서 공개한 데이터로, 1999-2008년 미국에서 출시된 자동차 정보 데이터
'''
mpg = pd.read_csv(path + 'mpg.csv')

# print(mpg.head(15))
# print(mpg.info())
'''
object : 문자열
float64 : 실수
int64 : 정수
'''
# print(mpg.describe(include='all')) # 문자로 된 변수의 통계도 보고싶을 때
# print(mpg.describe())

### 변수명 바꾸기 - rename() 함수 사용

df_raw = pd.DataFrame({
    'var1': [1, 2, 1],
    'var2': [2, 3, 2]
})

# print(df_raw)

df_new = df_raw.copy()  # 복사본 만들기 - 원본 데이터의 손실을 막기 위함

df_new = df_new.rename(columns={'var2': 'vaaaaaaa2',
                                'var1': 'v1'})  # 수정
# print(df_new)

### 파생변수 생성
'''
파생변수 : 기존의 변수를 변형시켜서 추가해주는 변수
'''

## 1. 변수를 조합해서 파생변수 만들기
df = pd.DataFrame({
    'var1': [4, 3, 8],
    'var2': [2, 6, 1]
})
# print(df)

df['var_sum'] = df['var1'] + df['var2']
df['var_mean'] = (df['var1'] + df['var2']) / 2
# print(df)

### mpg 통합 연비 변수 만들기
mpg = pd.read_csv(path + 'mpg.csv')
mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2
# print(mpg.head())

# result2 = sum(mpg['total']/len(mpg)) # total 합계를 행의 개수로 나누기
# print('당시 미국차 전체 평균 연비 :', result2)
# print('통합 연비 변수 평균 :', mpg['total'].mean()) # 간단하게 평균 함수 활용

### 조건문을 활용해서 파생변수 만들기

# 1. 기준값 정하기
# print(mpg.describe()) # 평균, 중앙값 확인
# mpg['total'].plot.hist() # 히스토그램 - 분포 확인
# plt.show()

# 2. 합격 판정 변수 생성 - 20이 넘는 차에 고연비 합격 판정
'''
조건문 함수 : 조건에 따라 서로 다른 값을 반환하는 함수

 - numpy 패키지 : 파이썬에서 수학이나 연산 관련 함수를 지원하는 패키지

 mpg['test'] = np.where(mpg['total'] > 20,'pass'        ,'fail')
                            조건          조건이 맞을때     조건에 부합하지 않을때
'''
import numpy as np

mpg['test'] = np.where(mpg['total'] > 20, 'pass', 'fail')
# print(mpg.head(30))

# 3. 빈도표로 합격 판정 자동차 수 확인
v = mpg['test'].value_counts()  # 빈도표 생성 함수
# print(v)

# 4. 막대 그래프로 빈도 표현
count_test = mpg['test'].value_counts()
# bar(rot = 0) -> 축 이름을 수평으로 만들어주는 입력값
# count_test.plot.bar(rot=0) # 막대그래프 생성
# plt.show() # 그래프 출력

### 중첩 조건문 활용
'''
A 등급 : 연비 30 이상
B 등급 : 20~29 
C 등급 : 연비 20 미만
'''

# 1. 연비 등급 변수 만들기
mpg['grade'] = np.where(mpg['total'] >= 30, 'A',
                        np.where(mpg['total'] >= 20, 'B', 'C'))
# print(mpg.head(20))

# 2. 빈도표와 막대 그래프로 연비 등급 확인
count_grade = mpg['grade'].value_counts()
print(count_grade)
# count_grade.plot.bar(rot=0)
# plt.show()

# 3. 알파벳 순 정렬
count_grade = mpg['grade'].value_counts().sort_index()  # 메서드 체이닝

# df = mpg['grade']
# df = df.value_counts()
# df = df.sort_index()
# print(df)
# print(count_grade)
# count_grade.plot.bar(rot=0)
# plt.show()

### 필요한 만큼 중접 조건 활용
mpg['grade2'] = np.where(mpg['total'] >= 30, 'A',
                         np.where(mpg['total'] >= 25, 'B',
                                  np.where(mpg['total'] >= 20, 'C', 'D')))
# print(mpg.head())

### 목록에 해당하는 행으로 변수 만들기
mpg['size'] = np.where((mpg['category'] == 'compact') |
                       (mpg['category'] == '2seater') |
                       (mpg['category'] == 'subcompact'), 'small', 'large')
# print(mpg['size'].value_counts()

small_list = ['compact', '2seater', 'subcompact']

mpg['size'] = np.where(mpg['category'].isin(small_list),
                       'small',  # 조건이 참일 때
                       'large')  # 조건이 거짓일 때
a = mpg['size'].value_counts()
print(a)
