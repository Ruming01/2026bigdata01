import numpy as np
import pandas as pd


df = pd.DataFrame({'국':[1, 4, 7], '영':[2, 5, 8], '수':[3, 6, 9], '미세먼지':[10, 3, 11]}, index=[1, 2, 3])
print(df)
df.drop(columns=['수', '미세먼지'])

df_new = ((pd.melt(df)
          .rename(columns={'variable': 'var', 'value': 'val'})
          .query('val > 5'))
          .sort_values(by='val', ascending=False))
print(df_new)