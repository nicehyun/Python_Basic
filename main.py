import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv("salaries_by_college_major.csv")

# 결츨치 제거
clean_df = df.dropna()

# 초봉이 가장 높은 전공 찾기
highest_start_salary_index = clean_df["Starting Median Salary"].idxmax()
highest_start_salary_undergraduate_major = clean_df["Undergraduate Major"].loc[highest_start_salary_index]

# 초봉이 가장 낮은 전공과 해당 전공 졸업생의 연봉
lowest_start_salary_index = clean_df["Starting Median Salary"].idxmin()
lowest_start_salary_undergraduate_major = clean_df["Undergraduate Major"].loc[lowest_start_salary_index]
lowest_start_salary = clean_df["Starting Median Salary"].loc[lowest_start_salary_index]

# 중간 연봉이 가장 높은 전공 찾기
highest_mid_salary_index = clean_df["Mid-Career Median Salary"].idxmax()
highest_mid_salary_undergraduate_major = clean_df["Undergraduate Major"].loc[highest_mid_salary_index]

# 중간 연봉이 가장 낮은 전공과 해당 전공 졸업생의 연봉
lowest_mid_salary_index = clean_df["Mid-Career Median Salary"].idxmin()
lowest_mid_salary_undergraduate_major = clean_df["Undergraduate Major"].loc[lowest_mid_salary_index]
lowest_mid_salary = clean_df["Starting Median Salary"].loc[lowest_mid_salary_index]

# 위험도가 낮은 전공
mid_90_percent_salary = clean_df["Mid-Career 90th Percentile Salary"]
mid_10_percent_salary = clean_df["Mid-Career 10th Percentile Salary"]

spread_col = mid_90_percent_salary.subtract(mid_10_percent_salary)
clean_df.insert(1, 'Spread', spread_col)
low_risk = clean_df.sort_values("Spread")

# 90번째 백분위수에서 가장 높은 값을 가진 상위 5학위
low_risk_top_5 = low_risk["Undergraduate Major"].head()

highest_spread = clean_df.sort_values("Mid-Career Median Salary", ascending=False)
highest_spread_top_5 = highest_spread[["Undergraduate Major", "Mid-Career Median Salary"]].head()

# 'Group'의 각 범주에 몇 개의 전공이 있는지 계산
group_by_count = clean_df.groupby("Group").count()
# print(group_by_count["Undergraduate Major"])

# 그룹 별 평균 연봉 계산
group_by_mean_salary = clean_df.groupby("Group").mean(numeric_only=True)

print(group_by_mean_salary)
# 평균 봉급이 가장 높은 학위 범주
