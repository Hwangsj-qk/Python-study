import matplotlib.pyplot as plt
import numpy as np

'''
데이터 가공 - 데이터 전처리
-> 분석에 적합하게 데이터를 가공하는 작업
'''

'''
- 데이터 가공 함수
1. query() : 행 추출
2. 데이터명[] : 열 추출
3. sort_values() : 정렬
4. groupby() : 집단별로 나누기
5. assign() : 변수 추가
6. agg() : 통계치 산출 - 평균, 최대값 ... 
7. merge() : 데이터 합치기 (열)
8. concat() : 데이터 합치기 (행)
'''

### 조건에 맞는 데이터 추출
import pandas as pd
path = 'C:/Python_Data/'
exam = pd.read_csv(path + 'exam.csv')
# print(exam)

''' query() 함수의 괄호 안에는 조건문이 들어가게 되는데 반드시 문자열로 써야 한다. '''
# print(exam.query('nclass == 1'))
result = exam.query('nclass == 1')
# print(result)

result2 = exam.query('nclass != 1') # 1반이 아닌 경우
# print(result2)

## 초과, 미만, 이상, 이하 조건 걸기
result3 = exam.query('math > 50')
# print(result3)

result4 = exam.query('english >= 80')
# print(result4)

## 여러 조건을 충족하는 행 추출
''' 그리고(and)를 의미하는 & 기호를 쓰면 여러 조건을 나열할 수 있다. 
    또는(or)을 의미하는 | 기호를 쓰면 어려 조건을 나열할 수 있다.'''
result5 = exam.query('nclass == 1 & math >= 50')
# print(result5)

## 여러 조건 중 하나 이상 충족하는 행 추출

# 수학 점수가 90점 이상이거나 영어 점수가 90점 이상인 경우
result6 = exam.query('math >= 90 | english >= 90')
# print(result6)

## 목록에 해당하는 행 추출

# 1, 3, 5 반에 속한 학생 데이터만 추출
result7 = exam.query('nclass == 1 | nclass == 3 | nclass == 5')
# print(result7)
result7 = exam.query('nclass in [1,3,5]') # in : 포함 연산자
# print(result7)

## 문자 변수를 사용해서 조건에 맞는 행 추출
df = pd.DataFrame({
    's' : ['F','M','F','M'],
    'country' : ['Korea', 'China', 'Japan', 'USA']
})
# print(df)

result8 = df.query('s == "F"')
# print(result8)
result8 = df.query('s == "M" & country ==0')
# print(result8)

'''
- 파이썬에서 사용하는 기호
1. 논리 연산자
    1)  <  : 작다
    2) <= : 작거나 같다
    3) == : 같다
    4) != : 같지 않다
    5) | : 또는
    6) & : 그리고
    7) in : 포함 연산자, 매칭 확인

2. 산술 연산자
    1) +
    2) -
    3) * : 곱하기
    4) ** : 제곱
    5) / : 나누기
    6) // : 나눗셈의 몫
    7) % : 나눗셈의 나머지
'''

# a = pd.read_csv(path + 'mpg.csv')
# print(a)

### 데이터 프레임 출력 제한 설정
# pd.set_option('display.max_rows', None) # 모든 행 출력하도록 설정
# pd.set_option('display.max_columns', None) # 모든 열 출력하도록 설정

# 되돌리기
# pd.reset_option('display.max_rows')
# pd.reset_option('display.max_columns')
# pd.reset_option('all') # 모든 설정 되돌리기

# -----------------------------------------------------------------------------
''' 필요한 변수만 추출 - 열 추출 '''
# print(exam['math'])
# print(exam)
result9 = exam[['math', 'english', 'science']]
# print(result9)

### 변수 제거하기
result10 = exam.drop(columns='math')
result10 = exam.drop(columns=['math', 'science'])
# print(result10)

### pandas 함수 조합
result11 = exam.query('nclass == 1')['english']
result11 = exam.query('math >= 50')[['id', 'math']].head(10)
# print(result11)
# -----------------------------------------------------------------------------
''' 순서대로 정렬 '''
result12 = exam.sort_values('math') # 오름차순
# print(result12)
result12 = exam.sort_values('math', ascending=False) # 내림차순
# print(result12)

### 여러 정렬 기준 설정
result12 = exam.sort_values(['nclass', 'math'], ascending=False)
result12 = exam.sort_values(['nclass', 'math'], ascending=[False, True])
# print(result12)
# -----------------------------------------------------------------------------
''' 파생변수 추가 - 추가해서 출력 '''
a = exam.assign(total = exam['math'] + exam['english'] + exam['science'],
                mean = (exam['math'] + exam['english'] + exam['science'])/3 )
# print(a)

b = exam.assign(test = np.where(exam['science'] > 50,'pass','fail'))
# print(b)

### 추가한 변수를 pandas 함수에 바로 활용
c = exam.assign(total = exam['math'] + exam['english'] + exam['science']) \
    .sort_values('total')
# print(c)
# -----------------------------------------------------------------------------
''' 집단별로 나누기 - groupby(), agg() '''

## math 평균
a = exam.agg(mean_math = ('math', 'mean'))
# print(a)

## 반 별 평균
''' as_index = False 를 입력으로 주면 변수가 인덱스로 들어가지 않는다 . '''
b = exam.groupby('nclass', as_index=False) \
    .agg(mean_math = ('math', 'mean'))
# print(b)

### 여러개의 요약 통계량 한번에 생성
c = exam.groupby('nclass') \
    .agg(mean_math = ('math', 'mean'), # 평균
         sum_math = ('math', 'sum'), # 합계
         median_math = ('math', 'median'), # 중앙값
         n = ('nclass', 'count')) # 학생 수 (빈도)
# print(c)

'''
- agg() 함수에 자주 사용하는 요약 통계량 함수
1. mean()
2. std() : 표준편차
3. sum()
4. median()
5. max(), min() : 최대값, 최소값
6. count()
'''

### 모든 변수의 요약통계량 구하는 방법
d = exam.groupby('nclass').mean()
# print(d)

### 집단별로 다시 집단 나누는 방법
mpg = pd.read_csv(path+'mpg.csv')

a = mpg.groupby(['manufacturer', 'drv']) \
    .agg(mean_cty = ('cty', 'mean'))
# print(a)

### pandas 함수 조합

''' 
Q . 제조 회사별로 "suv" 자동차의 도시 및 고속도로 합산 연비 평균을 구해
        내림차순으로 정렬하고, 1-5위까지 출력하기 
'''

result = mpg.query('category == "suv"') \
    .assign(total=(mpg['cty'] + mpg['hwy'])/2) \
    .groupby('manufacturer') \
    .agg(mean_tot = ('total', 'mean')) \
    .sort_values('mean_tot', ascending=False) \
    .head(5)
# print(result)
# -----------------------------------------------------------------------------
''' 데이터 합치기 '''

### 가로로 합치기
test1 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'mid' : [60,90,70,90,65]
})

test2 = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'final' : [70,83,65,95,100]
})

total = pd.merge(test1, test2, how='left', on = 'id')
# print(total)

### 다른 데이터를 사용해서 변수 추가
name = pd.DataFrame({
    'nclass' : [1,2,3,4,5],
    'teacher' : ['kim','lee','park','choi','jung']
})

exam_new = pd.merge(exam, name, how='left', on='nclass')
# print(exam_new)

### 세로로 합치기
a = pd.DataFrame({
    'id' : [1,2,3,4,5],
    'score' : [6,8,7,9,8.5]
})

b = pd.DataFrame({
    'id' : [6,7,8,9,10],
    'score' : [7,8.8,6.5,9.5,10]
})
all = pd.concat([a, b])
# print(all)
# -----------------------------------------------------------------------------
''' 데이터 정제 - 데이터 오류를 찾아내는 과정 '''
'''
1 . 결측치 : 누락된 값, 비어 있는 값
-> 파이썬에서 결측치는 NaN 으로 표시가 된다.
'''

### 결측치 찾기
import numpy as np
import pandas as pd

df = pd.DataFrame({
    's' : ['M','F',np.nan,'M','F'],
    'score' : [5,4,3,2,np.nan]
})
# print(df)

### 결측치 확인 - pd.isna()
# print(pd.isna(df)) # True : 결측치가 존재하는 부분

# print(pd.isna(df).sum()) # 결측치 빈도로 확인

### 결측치 제거 - df.dropna()
a = df.dropna(subset=['score']) # score 변수에서 결측치가 존재하는 행을 제거
# print(a)

b = a['score'] + 1
# print(b)

## 여러 변수에 결측치 없는 데이터 추출
df_nomiss = df.dropna(subset=['s','score'])
# print(df_nomiss)

## 결측치가 하나라도 있으면 제거 <- 데이터의 손실이 클 때는 사용하지 x
df_nomiss = df.dropna() # 모든 변수에 결측치가 없는 데이터 추출
# print(df_nomiss)

### 결측치 대체하기

# 1. 평균값으로 대체
exam = pd.read_csv(path + 'exam.csv')
exam.loc[[2,7,14], ['math']] = np.nan # 데이터의 2,7,14행에 결측치 할당
# print(exam)

# print(exam['math'].mean())

exam['math'] = exam['math'].fillna(55) # NaN 값을 55로 채워준다.
# print(exam)

search = exam['math'].isna().sum()
# print(search)
# -----------------------------------------------------------------------------
''' 이상치 : 이상한 수치, 정상범위에서 크게 벗어난 값 '''

### 이상치 제거 - 존재할 수 없는 값
''' 5점 척도 설문조사 '''
df = pd.DataFrame({
    's' : [1,2,1,3,1,2],
    'score' : [5,4,3,4,2,6]
})
# print(df)

# 1. 이상치 확인
a = df['s'].value_counts().sort_index()
# print(a)
b = df['score'].value_counts().sort_index()
# print(b)

# 2. 확인했으면 결측 처리
df['s'] = np.where(df['s'] == 3, np.nan, df['s'])
# print(df)
df['score'] = np.where(df['score'] > 5, np.nan, df['score'])
# print(df)

# 3. 결측치 제외 분석
result = df.dropna(subset=['s','score']) \
    .groupby('s') \
    .agg(mean_score = ('score', 'mean'))
# print(result)

### 이상치 제거 - 극단적인 값

# 상자 그림으로 극단치 기준을 정하기
'''
상자 그림 : 데이터의 분포를 직사각형의 상자 모양으로 표현한 그래프
'''

# 1. 상자그림 생성
# print(mpg)

import seaborn as sns
# sns.boxplot(data=mpg, y='hwy')
# plt.show()

# 2. 극단치 기준값 구하기
pct25 = mpg['hwy'].quantile(.25)
# print('1사분위수 :', pct25)
pct75 = mpg['hwy'].quantile(.75)
# print('3사분위수 :', pct75)

# IQR 구하기 - 1사분위수와 3사분위수의 거리
iqr = pct75 - pct25
# print('IQR :', iqr)

# 하한, 상한 구하기 - 극단치의 경계가 되는 하한, 상한
'''
하한 : 1사분위수보다 iqr의 1.5배만큼 더 작은 값
상한 : 3사분위수보다 iqr의 1.5배만큼 더 큰 값
'''
# print('하한 :', pct25 - 1.5 * iqr)
# print('상한 :', pct75 + 1.5 * iqr)

# 3. 극단치를 결측 처리 - 4.5 ~ 40.5 벗어나면 NaN 값 부여
''' np.where() 에 여러 조건을 입력할 때는 각 조건을 괄호로 감싸줘야한다. '''
mpg['hwy'] = np.where((mpg['hwy'] < 4.5) | (mpg['hwy'] > 40.5),
                      np.nan,
                      mpg['hwy'])
# print(mpg['hwy'].isna().sum())

# 4. 결측치를 제외하고 분석
result = mpg.dropna(subset=['hwy']) \
    .groupby('drv') \
    .agg(mean_hwy = ('hwy', 'mean'))
# print(result)
# -----------------------------------------------------------------------------
'''
그래프 : 데이터를 보기 쉽게 그림으로 표현한 것
'''
### 산점도 : 데이터를 x축과 y축에 점으로 표현한 그래프 , 두 변수의 관계 표현
# print(mpg)

# sns.scatterplot(data=mpg, x='displ', y='hwy')
# plt.show()

# 축 범위 설정
# sns.scatterplot(data=mpg, x='displ', y='hwy')\
#     .set(xlim = (3, 6), ylim = (10,30))
# plt.show()

# 종류별로 표시 색깔 바꾸기
# sns.scatterplot(data=mpg, x='displ', y='hwy', hue='drv')
# plt.show()

''' 그래프 설정 '''
import matplotlib.pyplot as plt

plt.rcParams.update({'figure.dpi' : '150'}) # 해상도 (기본값 72)
plt.rcParams.update({'figure.figsize' : [8, 6]}) # 가로, 세로 크기 (기본값 [6,4])
plt.rcParams.update({'font.size' : '15'}) # 글자 크기 (기본값 10)
plt.rcParams.update({'font.family' : 'Malgun Gothic'}) # 글꼴 지정 (기본값 sans-serif)
 # 맥 사용자는 'AppleGothic' 입력
plt.rcParams.update({'figure.dpi' : '150',
                     'figure.figsize' : [8, 6],
                     'font.size' : '15',
                     'font.family' : 'Malgun Gothic'})

## 설정 되돌리기
plt.rcParams.update(plt.rcParamsDefault)

''' 막대 그래프 - 집단 간 차이 표현 '''

### 평균 막대 그래프

# 1. 집단별 평균표 만들기 - 구동 방식별(drv) 도심 연비 평균

df_mpg = mpg.groupby('drv', as_index=False) \
    .agg(mean_cty = ('cty', 'mean'))
# print(df_mpg)

# sns.barplot(data=df_mpg, x='drv', y='mean_cty')
# plt.show()

## 크기순으로 정렬
df_mpg = df_mpg.sort_values('mean_cty', ascending=False)

# sns.barplot(data=df_mpg, x='drv',y='mean_cty')
# plt.show()

### 빈도 막대 그래프

# 1. 집단별 빈도표 생성
df_mpg = mpg.groupby('drv', as_index=False) \
    .agg(n = ('cty', 'count'))
# print(df_mpg)

# sns.barplot(data=df_mpg, x='drv', y='n')
# plt.show()

# sns.countplot(data=mpg, x='drv')
# plt.show()

''' 선 그래프 - 시간에 따라 달라지는 데이터 표현 '''
'''
시계열 데이터 : 일정 시간 간격을 두고 나열된 데이터
'''

economics = pd.read_csv(path + 'economics.csv')
# print(economics)

# sns.lineplot(data=economics, x='date', y='unemploy')
# plt.show()

## x 축에 연도 표시하기

# 1. 날짜 시간 타입 변수 생성 - pd.to_datetime()
economics['date2'] = pd.to_datetime(economics['date'])
# print(economics.info())


# 2. 각 추출

# print(economics['date2'].dt.year)
# print(economics['date2'].dt.month)
# print(economics['date2'].dt.day)

# 3. 연도 변수 생성
economics['year'] = economics['date2'].dt.year
# print(economics.head())

# 4. x축에 연도 표시
# sns.lineplot(data=economics, x='year', y='unemploy', ci=None)
# plt.show()

''' 상자 그림 - 집단 간 분포 차이 확인 '''
# sns.boxplot(data=mpg, x='drv', y='hwy')
# plt.show()
# -----------------------------------------------------------------------------
''' 한국 복지 패널 데이터 분석 
-> 한국보건사회연구원에서 우리나라 가구의 경제활동을 연구해서 복지 정책에 반영할 목적으로 
    발간되는 조사 자료. 전국에서 7000여 가구를 선정해서 2006년부터 매년 추적 조사한 데이터 
'''

### 패키지 설치 데이터 로드
''' 터미널 -> pip install pyreadstat '''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

raw_welfare = pd.read_spss(path + 'Koweps_hpwc14_2019_beta2.sav')

welfare = raw_welfare.copy() # 복사본 생성

### 데이터 검토
# print(welfare)
# print(welfare.info())
# print(welfare.describe())

### 변수명 수정
welfare = welfare.rename(
    columns={'h14_g3' : 's', # 성별
             'h14_g4' : 'birth', # 태어난 연도
             'h14_g10' : 'marriage_type', # 혼인 상태
             'h14_g11' : 'religion', # 종교
             'p1402_8aq1' : 'income', # 월급
             'h14_eco9' : 'code_job', # 직종 코드
             'h14_reg7' : 'code_region'} # 지역 코드
)
'''
- 데이터 분석 절차
1. 변수 검토 및 전처리
2. 변수 간 관계 분석 
'''

# -----------------------------------------------------------------------------------
''' 성별에 따른 월급 차이 - 남녀가 월급이 다를까 ? '''

# 1. 성별변수 검토
# print(welfare['s'].dtypes)
# print(welfare['s'].value_counts()) # 이상치가 없다.

# 2. 성별 전처리
welfare['s'] = np.where(welfare['s'] == 1, 'male', 'female')
# print(welfare['s'].value_counts())

# 3. 월급 변수 검토 및 전처리
# print(welfare['income'].dtypes)
# print(welfare['income'].describe())
# sns.histplot(data=welfare, x='income') # 히스토그램 : 분포 확인
# plt.show()

a = welfare['income'].isna().sum() # 결측치 확인
# print(a)
welfare['income'] = np.where(welfare['income'] == 9999, np.nan,
                             welfare['income'])
# print(welfare['income'].isna().sum())

# 4. 성별 월급 평균표 생성
s_income = welfare.dropna(subset=['income']) \
    .groupby('s', as_index=False) \
    .agg(mean_income = ('income', 'mean'))
# print(s_income)
# sns.barplot(data=s_income, x='s', y='mean_income')
# plt.show()

''' 나이와 월급의 관계 - 몇 살때 월급을 가장 많이 받을까 ? '''

### 나이 변수 검토 및 전처리
# print(welfare['birth'].dtypes)
# print(welfare['birth'].describe())
# sns.histplot(data=welfare, x='birth')
# plt.show()

# print(welfare['birth'].isna().sum()) # 결측치 확인

# 1. '나이' 파생변수 생성
welfare = welfare.assign(age = 2019 - welfare['birth'] + 1)
# print(welfare['age'].describe())
# sns.histplot(data=welfare, x='age')
# plt.show()

# 2. 나이와 월급 관계 분석

# 나이에 따른 월급 평균표
age_income = welfare.dropna(subset=['income']) \
    .groupby('age') \
    .agg(mean_income = ('income', 'mean'))
# print(age_income.head(10))
# sns.lineplot(data=age_income, x='age', y='mean_income')
# plt.show()

''' 연령대에 따른 월급 차이 - 어느 연령대의 월급이 가장 많을까 ? '''

### 연령대 변수 검토 및 전처리
'''
초년층 - 30살 미만
중년층 - 30 ~ 59 세 
노년층 - 60세 이상
'''
welfare = welfare.assign(ageg = np.where(welfare['age'] < 30, 'young',
                                         np.where(welfare['age'] <= 59, 'middle','old')))
# print(welfare['ageg'].value_counts())

# 1. 연령대에 따른 월급 차이 분석
ageg_income = welfare.dropna(subset=['income'])\
    .groupby('ageg', as_index=False)\
    .agg(mean_income = ('income', 'mean'))
# print(ageg_income)
# sns.barplot(data=ageg_income, x='ageg', y='mean_income',
#             order = ['young','middle','old'])
# plt.show()

''' 직업별 월급 차이 - 어느 직업이 돈을 가장 많이 벌까 ? '''

### 직업 변수 검토 및 전처리
# print(welfare['code_job'].dtypes)
# print(welfare['code_job'].value_counts())

list_job = pd.read_excel(path + 'Koweps_Codebook_2019.xlsx', sheet_name='직종코드')
# print(list_job)

### welfare 에 list_job 합치기
welfare = welfare.merge(list_job, how='left', on='code_job')

a = welfare.dropna(subset=['code_job'])[['code_job', 'job']].head()
# print(a)

### 직업별 월급 차이 분석

# 1. 직업별 월급 평균표
job_income = welfare.dropna(subset=['job','income']) \
    .groupby('job', as_index=False) \
    .agg(mean_income = ('income','mean'))
# print(job_income.head(10))

# 2. 그래프 생성
top10 = job_income.sort_values('mean_income', ascending=False).head(10)
# print(top10)

plt.rcParams.update({'font.family' : 'Malgun Gothic'}) # 한글을 지원하는 폰트 지정

# sns.barplot(data=top10, y='job', x='mean_income')
# plt.show()

bottom10 = job_income.sort_values('mean_income').head(10)
# sns.barplot(data=bottom10, y='job', x='mean_income')\
#     .set(xlim=(0,800))
# plt.show()

''' 지역별 연령대 비율 - 어느 지역에 노년층이 가장 많을까 ? '''

### 지역 변수 검토 및 전처리
# print(welfare['code_region'].dtypes)
# print(welfare['code_region'].value_counts())

# 1. 지역 코드 목록 생성
list_region = pd.DataFrame({'code_region' : [1,2,3,4,5,6,7],
                            'region' : ['서울',
                                        '수도권(인천/경기)',
                                        '부산/경남/울산',
                                        '대구/경북',
                                        '대전/충남',
                                        '강원/충북',
                                        '광주/전남/전북/제주도']})

# 2. 지역명 변수 추가
welfare = welfare.merge(list_region, how='left', on='code_region')
# print(welfare[['code_region', 'region']].head())

### 지역별 연령대 비율 분석

# 1. 지역별 연령대 비율표 생성
region_ageg = welfare.groupby('region', as_index=False) \
    ['ageg'] \
    .value_counts(normalize=True) # 비율 구하기
# print(region_ageg)

# 2. 그래프 생성
region_ageg = \
region_ageg.assign(proportion = region_ageg['proportion'] * 100) \
    .round(1) # 소수점 첫째 자리까지 반올림
# print(region_ageg)

# sns.barplot(data=region_ageg, y='region', x='proportion', hue='ageg')
''' barplot 에서 hue 에 변수를 입력하면 변수안의 내용마다 색을 다르게 표현해준다.'''
# plt.show()

# --------------------------------------------------------------------------------
''' 
텍스트 마이닝 : 문자로 된 데이터에서 가치 있는 정보를 얻어 내는 분석 기법

1. 형태소 분석 : 문장을 구성하는 어절들이 어떤 품사인지 파악하는 작업

2. 운영 체제 버전에 맞는 JAVA 설치 

3. 의존성 패키지 설치 = pip install jpype1

4. pip install konlpy
'''

### 연설문 로드
''' 
파이썬에서 텍스트 파일을 읽어올때 open() 함수를 쓰면 된다. 
인코딩 : 컴퓨터가 문자를 표현하는 방식, 문서마다 인코딩 방식이 다르기 떄문에 문서 파일과
        프로그램의 인코딩이 맞지 않으면 문자가 깨지게 된다.
'''
moon = open(path+'speech_moon.txt', encoding='UTF-8').read()
# print(moon)

### 불필요한 문자 제거
import re
moon = re.sub('[^가-힣]', ' ', moon)
'''
[^가-힣] : 한글이 아닌 모든 문자라는 뜻을 가진 정규 표현식
정규 표현식 : 특정한 규칙을 가진 문자열을 표현하는 언어, 이메일 주소, 전화번호 처럼
            특정한 규칙으로 되어있는 문자를 찾거나 수정할 때 정규 표현식을 쓴다.
'''
# print(moon)

### 명사 추출 - konlpy.tag.Hannanum() 의 nouns() 를 이용한다.
import konlpy
hannanum = konlpy.tag.Hannanum()

a = hannanum.nouns('대한민국의 영토는 한반도와 그 부속 도서로 한다.')
print(a)
