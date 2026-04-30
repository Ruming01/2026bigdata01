import numpy as np
import pandas as pd


df = pd.DataFrame({'국':[1, 4, 7], '영':[2, 5, 8], '수':[3, 6, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)
# print(df.iat[1, 2])
# print(df.at[2, '수'])
#
# print(df.sample(frac=0.33))
# print(df.nlargest(2, '화'))
# print(df.nsmallest(2, '화'))
print(df.tail(2))