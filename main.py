# ValueError: Length of values does not match length of index

import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})


df['D'] = pd.Series([10, 11])

#    A  B  C     D
# 0  1  4  7  10.0
# 1  2  5  8  11.0
# 2  3  6  9   NaN
print(df)