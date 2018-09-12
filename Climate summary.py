
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd


# In[2]:


df = pd.read_excel('cities_CLIMATE_lat_lgn.xlsx')


# In[3]:


# df['range1'] = df.iloc[[1880,1880+20]].sum(axis='columns')
# df

#all rows, columns 5:26
df['1880-1910'] = df.iloc[:, 5:36].sum(axis='columns')
df['1911-1940'] = df.iloc[:, 36:66].sum(axis='columns')
df['1941-1970'] = df.iloc[:, 66:96].sum(axis='columns')
df['1971-2000'] = df.iloc[:, 96:126].sum(axis='columns')
df['2001-2017'] = df.iloc[:, 126:143].sum(axis='columns')

df


# In[ ]:


# df.filter(regex='^(1880)$').sum(axis=1)


# In[ ]:


for x in range(0,20):
   
    # for each part calculate the obs/spend after each unit consumes inventory    
    for index, row in useUp_df.iterrows():
        

