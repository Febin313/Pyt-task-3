#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup
import requests


# In[12]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html')


# In[13]:


print(soup)


# In[14]:


soup.find_all('table')


# In[15]:


soup.find('table', class_="wikitable sortable sticky-header-multi sort-under")


# In[19]:


wt=soup.find_all('th')
wt


# In[21]:


wtt=[titles.text.strip() for titles in wt]
print(wtt)


# In[22]:


import pandas as pd
df= pd.DataFrame(columns=wtt)
df


# In[24]:


col_data=soup.find_all('tr')
                       


# In[27]:


for row in col_data[2:]:
     rdata=row.find_all('td')
     indrdata=[data.text.strip() for data in rdata]
     print(indrdata)


# In[28]:


df=pd.DataFrame(wtt)
df


# In[ ]:




