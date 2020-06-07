#%%
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 5)
#fixed_df = pd.read_csv('files/bikes.csv')
# print(fixed_df[:3])
fixed_df = pd.read_csv('files/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# print(fixed_df[:3])  print first 3 rows 
# print(fixed_df['Berri 1']) print the column or select the specific column 
fixed_df[:3]
# %%
fixed_df['Berri 1'].plot(figsize=(15,10))

# %%
fixed_df.plot(figsize=(15,10))


# %%
