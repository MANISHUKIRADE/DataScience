#%%
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('files/whoDataset.csv', parse_dates=['date'], index_col='date')
#print(data[:3])
data['new_cases'].plot()


# %%
data = pd.read_csv('files/whoDataset.csv', parse_dates=['date'])
data[:10]
# %%
data = pd.read_csv('files/whoDataset.csv', parse_dates=['date'])
data[:10][['date','location']]

# %%
location=data['location'].value_counts()
location[:20].plot(kind='bar')