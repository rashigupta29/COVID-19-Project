#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd


# In[21]:


#df=pd.read_html('https://tinyurl.com/wnqrr8f',header=1)


# In[22]:


#df[0].to_csv("Covid19.csv")


# In[23]:


df=pd.read_csv("Covid19.csv")


# In[24]:


df.columns


# In[25]:


df


# In[26]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[27]:


df[["Patient Number","Gender"]]


# # Here We can find that Male or Female which one is more affected by COVID-19 using Boxplot,Pie Chart and Bar.
# 

# 1. First we categorize Gender into parts then we can see that the female patient of Covid-19 is more than the male patient. 

# In[48]:


df.boxplot(column='Patient Number',by='Gender')


# # 2. Here also we check more patient using bar chart.

# In[50]:


height=['Male','Female']
left=[1,2]
tick_label=['Male','Female']
plt.bar(height,left,tick_label=tick_label,width=0.8)


# 3. Here we use pie chart to categorize the patient who are more affected by COVID-19 in Gender.
# and I use legend here to show which colour follow which column name.

# In[23]:


labels = 'Patient Number','Male','Female'
colors = ['gold',  'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0)# explode 1st slice
sizes=[200,250,300]
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.legend('PMF')
plt.axis('equal')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




