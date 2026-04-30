import numpy as np
import pandas as pd


df = pd.DataFrame({'국':[1, 4, 7], '영':[2, 5, 8], '수':[3, 6, 9], '화':[10, 3, 11]}, index=[1, 2, 3])
print(df)

# df_new = df.iloc[1:]
# df_new = df.iloc[1:, 2:]
# df_new = df.iloc[:, [1, 3]]
# df_new =df.loc[:, '영':'화']
df_new = df.loc[df['국']>5, ['영', '화']]
print(df_new)