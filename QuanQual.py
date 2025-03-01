#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset=pd.read_csv("placement.csv")


# In[3]:


dataset


# In[4]:


dataset.info()


# In[5]:


#Quan=["ssc_p","hsc_p","etest_p","degree_p","mba_p","salarye"]
#Qual=["gender","ssc_b","degree_t"]


# In[6]:


dataset.columns


# In[7]:


dataset.dtypes


# In[8]:


dataset["ssc_p"].dtypes


# In[9]:


for columnName in dataset.columns:
    print(columnName)


# In[10]:


if(dataset["ssc_p"].dtype=='O'):
    print("qual")
else:
    print("quan")


# In[11]:


quan=[]
qual=[]
for columnName in dataset.columns:
    print(columnName)
    
    if(dataset['ssc_p'].dtype=='O'):
       # print("qual")
        qual.append(columnName)
    else:
       # print("quan")
        quan.append(columnName)
    



# In[12]:


quan


# In[13]:


qual


# In[14]:


def quanQual(dataset):
    quan=[]
    qual=[]
    for columnName in dataset.columns:
        #print(columnName)
        if(dataset[columnName].dtype=='O'):
            #print("qual")
            qual.append(columnName)
        else:
            #print("quan")
            quan.append(columnName)
    return quan,qual
    


# In[15]:


quanQual(dataset)


# In[16]:


quan,qual=quanQual(dataset)


# In[17]:


qual


# In[18]:


quan


# In[ ]:




