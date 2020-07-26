#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[ ]:


#seaborn library comes with some inbuilts dataset


# In[2]:


tips = sns.load_dataset("tips")


# In[3]:


tips


# In[5]:


type(tips)


# In[6]:


tips.head() # It tells about the top 5 rows


# In[7]:


tips.info()


# In[8]:


tips.isna().sum() # To check the null values


# In[ ]:


# Now we will study about the distribution plot


# In[9]:


sns.distplot()


# In[10]:


tips["total_bill"] # It is used to fetch a particular column


# In[11]:


sns.distplot(tips["total_bill"])


# In[ ]:


# Now we will study about bivariate distribution by using joint plot


# In[12]:


import matplotlib.pyplot as plt


# In[14]:


sns.distplot(tips["total_bill"],kde = False)


# In[ ]:


# For univariate analysis we use distplot but for multivariate analysis we use jpint plot


# In[16]:


sns.distplot(tips["size"],kde = "True")


# In[17]:


sns.jointplot("total_bill","tip",data = tips)


# In[18]:


tips.columns


# In[19]:


tips.corr()


# In[26]:


sns.jointplot("total_bill","tip", data = tips, kind = "hex", color = "g")


# In[27]:


sns.jointplot("total_bill", "tip", data = tips , kind = "reg")


# In[28]:


sns.jointplot("total_bill","tip",data = tips , kind = "resid" )


# In[29]:


sns.barplot(x= "sex", y= "total_bill", data =tips)


# In[30]:


sns.countplot("sex", data = tips)


# In[31]:


sns.countplot("smoker",data =tips )


# In[ ]:


# boxplot is used to check the outliers 


# In[33]:


sns.boxplot(x = "day",y ="total_bill",data = tips, hue = "sex")


# In[35]:


import seaborn as sns


# In[37]:


sns.violinplot("sex","total_bill",data = tips)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




