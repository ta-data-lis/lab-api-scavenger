#!/usr/bin/env python
# coding: utf-8

# In[96]:


import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth
url = 'https://api.github.com/repos/ironhack-datalabs/datalis0819/forks'
response = requests.get(url ,auth = HTTPBasicAuth('user', 'password'))


# In[97]:


print(response.status_code)


# In[116]:


df = pd.DataFrame(response.json())
df1 = pd.DataFrame(df['language'])
df1.drop_duplicates()


# In[198]:


url = 'https://api.github.com/repos/ta-data-lis/lab-mysql-first-queries/commits'
res = requests.get(url ,auth = HTTPBasicAuth('user', 'password'))
df = pd.DataFrame(res.json())
df2 = pd.json_normalize(df['commit'])
date = '2020-11-7'

no_of_commits = (df2['committer.date'] > date).count()
print('There are', no_of_commits, 'commits')


# In[ ]:





# In[ ]:




