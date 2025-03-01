#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Univariate import Univariate


# In[2]:


#Obj = Univariate()


# In[3]:


import pandas as pd


# In[4]:


dataset = pd.read_csv("placement.csv")


# In[5]:


dataset


# In[6]:


quan,qual=Univariate.quanQual(dataset)


# In[7]:


quan


# In[8]:


qual


# In[ ]:




