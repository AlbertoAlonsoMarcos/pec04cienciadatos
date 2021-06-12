import pandas as pd

approval = pd.read_csv('../data/covid_approval_polls.csv')
ratings = pd.read_excel('../data/pollster_ratings.xlsx', engine = 'openpyxl')
ratings.rename(columns={'Pollster':'pollster'}, inplace=True)

approvals = pd.merge(approval, ratings, on='pollster')
x = approvals['tracking'].count()