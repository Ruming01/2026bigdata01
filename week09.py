import numpy as np
import pandas as pd

arr2d = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)

df_2Dlist = pd.DataFrame(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    columns=['국', '영', '수'], index=['1', '2', '3'])
df_dict = pd.DataFrame(
    [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    , index=['국', '영', '수'])


print(arr2d)
print(df_2Dlist)
print(df_dict)