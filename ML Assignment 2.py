#!/usr/bin/env python
# coding: utf-8

# # Numpy

# In[7]:


import numpy as np
import pandas as pd


# In[8]:


a= np.random.randint(20,size=(15))
a


# In[9]:


A=a.reshape(3,5)
A


# In[10]:


maxNum = np.amax(A, axis=1)
np.where(np.isin(A,maxNum), 0, A)


# # Pandas

# In[24]:


Csv_dataset=pd.read_csv("data.csv")


# In[25]:


Csv_dataset.describe()


# In[26]:


Csv_dataset.isnull().sum()


# In[27]:


Csv_dataset['Calories'].mean()


# In[28]:


new_calories = np.where(Csv_dataset['Calories'].isnull(),375.79,Csv_dataset['Calories'])
Csv_dataset['Calories']= new_calories
Csv_dataset


# In[29]:


Csv_dataset.Maxpulse.describe()


# In[30]:


Csv_dataset.Calories.describe()


# In[31]:


Csv_dataset[(Csv_dataset['Calories']>500) & (Csv_dataset['Calories']<1000)]
Csv_dataset


# In[32]:


Csv_dataset[(Csv_dataset['Calories']>500 & (Csv_dataset['Pulse']<100))]
Csv_dataset


# In[33]:


df_modified=Csv_dataset.drop("Maxpulse",axis=1)
df_modified


# In[34]:


Csv_dataset=Csv_dataset.drop("Maxpulse",axis=1)
Csv_dataset


# In[35]:


Csv_dataset["Calories"] = Csv_dataset["Calories"].astype(float).astype(int)
Csv_dataset


# In[36]:


Csv_dataset.plot.scatter(x = 'Duration', y = 'Calories')


# # Matplotlib

# In[37]:


Mat=pd.DataFrame({"popularity":[22.2, 17.6, 8.8, 8, 7.7, 6.7]},index=['Java','Python','PHP','JavaScript', 'C#', 'C++'] )
Mat


# In[38]:


Mat.plot.pie(y='popularity', autopct='%1.1f%%')


# In[ ]:




