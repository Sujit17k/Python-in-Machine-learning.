#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
df=pd.DataFrame()
print(df)


# In[3]:


cmp=pd.Series(['parker','John','Smith','William'])
id=pd.Series([102,107,109,114])
frame={'Emp':cmp,'ID':id}
result = pd.DataFrame(frame)
print("\nSeries to Data Frame\n")
print(result)


# In[6]:


print("\nAdding new column:\n")
result['Age']=pd.Series([35,24,40,38])
print(result)


# In[8]:


print("\nDeleting one column:\n")
del result['Age']
print(result)


# In[9]:


print("\nExtracting the third row:\n")
print(result.loc[2])


# In[11]:


print("\nSlice rows:\n", result[1:3])


# In[18]:


d2=pd.DataFrame([['Munusaamy',123],['Margazhy',143]],columns=['Emp','ID'])
print("\nAdding new row values:\n",result.append(d2))


# In[19]:


print("\nDeleting particular row:\n" , result.drop(1))


# In[ ]:




