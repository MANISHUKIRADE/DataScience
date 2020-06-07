#%%
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns',60)
plt.rcParams['figure.figsize'] = (15,5)
#%%
complaint = pd.read_csv('/home/manish/dev/DataScience/service_Request.csv', nrows=10000)

# %%
complaint[['Complaint Type','Borough']][:10]

# %%
complaintCount = complaint['Complaint Type'].value_counts()
complaintCount[:10]
#%%
complaintCount[:10].plot(kind='bar')
#%%%