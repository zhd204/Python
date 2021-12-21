import pandas as pd
a_list = [['dog', 1], ['cat', 2], ['fish', 3]]

df = pd.DataFrame(a_list, columns=['animal', 'amount'])
print(df)

