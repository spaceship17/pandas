#!/usr/bin/env python
# coding: utf-8

# # let's import pandas
# 

# In[ ]:


import pandas as pd


# let's read a file from uforeports

# In[2]:


df = pd.read_csv('http://bit.ly/uforeports')


# let's see first five rows data frame

# In[3]:


df.head(5)


# let's use loc method to see first 3 rows and all column

# In[6]:


df.loc[[0,1,2], :]


# let's see first row with all column data frame using loc method

# In[7]:


df.loc[0, :]


# let's see first 6 rows with all column using loc method

# In[9]:


df.loc[0:5,:]


# let's see first 6 rows with all column using loc method, similar to Out[9]

# In[11]:


df.loc[0:5]


# let's see all the rows for City column alone

# In[12]:


df.loc[:,'City']


# let's see all the rows for City and State columns using loc method

# In[13]:


df.loc[:,['City','State']]


# let's see first 3 rows for City through State column using loc method

# In[16]:


df.loc[0:2,'City':'State']


# let's use first 3 rows using head method where drop Time column from the data frame

# In[17]:


df.head(3).drop('Time', axis = 1)


# In[24]:


df[df.City=='Oakland'].State


# In[21]:


df.loc[df.City=='Oakland', 'State']


# let's use iloc method to investigate all rows and 1st and 3rd columns only

# In[27]:


df.iloc[:, [0,2]]


# let's use iloc method to investigate all rows for column from City through State

# In[28]:


df.iloc[:,0:4]


# let's check the list of range 0 to 4 in order to validate the above result

# In[30]:


list(range(0,4))


# let's use iloc method to see through first 3 rows and all of its column

# In[31]:


df.iloc[0:3, :]


# let's use list method to check through the City and State Column

# In[34]:


df[['City', 'State']]


# let's use loc method to see through all the rows for City and State column, as we can see it gives the same result as above line, however this method seems more explicit

# In[35]:


df.loc[:,['City','State']]


# let's run through first three rows using the below method, which looks as good as df.head(3) method

# In[36]:


df[0:3]


# let's use iloc method to run through first 2 rows and all columns

# In[37]:


df.iloc[0:2, :]

