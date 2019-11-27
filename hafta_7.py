#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x=[180,170,170,175,181,175,177,185,179,160]
y=[95,70,60,79,60,63,83,80,75,50]
x,y,len(x),len(y)


# In[3]:


z=np.stack((x, y), axis=0)
z


# In[4]:


sigma=np.cov(z)
sigma


# In[5]:


x_test=np.stack((x,x),axis=0)
x_test


# In[6]:


sigma2=np.cov(x_test)
sigma2


# In[7]:


def generate_data():
    x=[180,170,170,175,181,175,177,185,179,160]
    y=[95,70,60,79,60,63,83,80,75,50]
    z=np.stack((x, y), axis=0)
    return z
def get_cov_matrix(z):
    sigma=np.cov(z)
    return sigma


# In[8]:


data_1=generate_data()
get_cov_matrix(data_1)


# In[9]:


def multivariate_normal(x, d, mean, covariance):
    """pdf of the multivariate normal distribution."""
    x_m = x - mean
    return (1. / (np.sqrt((2 * np.pi)**d * np.linalg.det(covariance))) * 
            np.exp(-(np.linalg.solve(covariance, x_m).T.dot(x_m)) / 2))


# In[10]:


x=generate_data()
np.mean(x[0,:]),np.mean(x[1,:]) #test amaçlı ortalama boy ve kilo sonuçları


# In[11]:


x_1=[175,72]
d_1=2
data=generate_data()
mean_1=np.array([np.mean(x[0,:]),np.mean(x[1,:])])
covariance_1=get_cov_matrix(data)


# In[12]:


multivariate_normal(x_1,d_1,mean_1,covariance_1)


# In[13]:


for i in range (10):
    v=167+i
    x_1=[v,72]
    s=multivariate_normal(x_1,d_1,mean_1,covariance_1)
    print(v,"   ",s)

