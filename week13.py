import seaborn as sns
import matplotlib.pyplot as plt

# (데이터 측정) 년도, (대상) 국가, (1인당 연간 의료비) 지출액, (평균) 기대 수명
health = sns.load_dataset("healthexp")

# 가장 최근 년도인 2020년 데이터를 추출
health_2020 = health[health['Year'] == 2020]
# print(health_2020.sort_values('Life_Expectancy', ascending=False))

# 전체 데이터셋에서 의료비 지출이 5000달러 이상인 데이터 추출
# high_spending = health[health['Spending_USD'] >= 5000]
# print(high_spending["Country"].unique())

# 국가별 평균 의료비 지출과 평균 기대수명
# country_mean = health.groupby('Country')[['Spending_USD', 'Life_Expectancy']].mean()
# print(country_mean)

# 국가별로 데이터가 몇 개씩 있는지 개수 세기
# print(health['Country'].value_counts())

# 년도별 평균 의료비 지출과 평균 기대수명
# year_mean = health.groupby('Year')[['Spending_USD', 'Life_Expectancy']].mean()
# print(year_mean)

# 국가별 기대 수명 분포 확인
# sns.catplot(data=health, x = 'Year', y = 'Life_Expectancy', col = 'Country', kind = 'box', col_wrap = 3)
# plt.show()

# 최신 국가별 의료비 지출 비교
# sns.catplot(data=health_2020, x = 'Country', y = 'Spending_USD', kind = 'bar', palette = 'muted')
# plt.show()

# 국가별 의료비와 기대 수명의 상관관계 (산점도)
# sns.relplot(data = health,
#             x = 'Spending_USD',
#             y = 'Life_Expectancy',
#             col='Country',
#             kind = 'scatter',
#             hue = 'Year',
#             col_wrap = 3,
#             palette = 'tab20'
#             )
# plt.show()

#2가지 기준으로 정렬 (년도, 기대수명)
# print(health.sort_values(by=['Year', 'Life_Expectancy'], ascending=False).head(10))
