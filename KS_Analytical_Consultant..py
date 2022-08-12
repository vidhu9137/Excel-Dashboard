#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:


pd.set_option('display.max_columns', None)


# In[3]:


from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))


# # Importing dataset

# In[4]:


df = pd.read_excel('Assignment.xlsx')


# In[5]:


df


# # Adding Days difference column

# In[10]:


df['Date difference'] = df['Ship Date'] - df['Order Date']


# In[11]:


diff = df['Date difference']
df = df.drop(columns=['Date difference'])
df.insert(loc=4, column='Date difference', value=diff)


# # Finding the ID of max/min sales

# In[12]:


df[['Sales']].idxmax()


# In[13]:


df[['Sales']].idxmin()


# # Creating sales buckets

# In[14]:


df['Sales'].max()


# In[15]:


bins = [0, 1000, 5000, 10000, 15000, 20000, 22700]

df['Sales Buckets'] = pd.cut(df['Sales'], bins)


# In[16]:


df['Sales Buckets'].unique()


# # Exporting the modified dataset

# In[ ]:


df.to_excel('Submission_KS.xlsx')


# In[ ]:




