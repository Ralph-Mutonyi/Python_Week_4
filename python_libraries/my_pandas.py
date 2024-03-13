"""
    open source
    used in wide range of fields including academic and commercial domains

    inport pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn (4,3),columns = ['col1', 'col2', 'col3'])
    for row_index,row in df.iterrows():
        print(row_index,row)
"""

# iteration of a tuple

"""
df = pd.DataFrame(np.random.randn (4,3), colums = ['col1', 'col2', 'col3'] )
for row in df.itertuples():
print(row)
"""