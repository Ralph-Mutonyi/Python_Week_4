#import pandas as pd
#import numpy as np

#df=pd.DataFrame(np.random.randn(4,3),columns=['col1','col2', 'col3'])

#for row_index,row in df.iterrows():
 #   print(row_index,row)

"""
df=pd.DataFrame(np.random.randn(4,3),columns=['col1','col2', 'col3']): 
This line creates a DataFrame (df) with 4 rows and 3 columns filled with random numbers drawn from a standard normal distribution (mean=0, standard deviation=1). The column names are specified as 'col1', 'col2', and 'col3'.

for row_index,row in df.iterrows():: 
    
This line initiates a loop that iterates over each row in the DataFrame df. df.iterrows() is a method that returns an iterator yielding index and row data for each row in the DataFrame.

print(row_index,row): 
This line prints the index of the current row (row_index) and the content of the row (row). Inside the loop, row represents each row of the DataFrame as a Series object, where the index labels correspond to the column names and the values represent the data in each column.
"""
# the result

"""
    The output of this code will be the index of each row followed by the content of each row printed as Series objects

    Each row is printed as a Series object, where the index corresponds to the column names ('col1', 'col2', 'col3') and the values are the randomly generated numbers. 
    The index printed alongside each row indicates the row number (0, 1, 2, 3) in the DataFrame.
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3),columns= ['col1','col2', 'col3'])
for row in df.itertuples():
    print(row)

