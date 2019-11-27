#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
os.getcwd()
os.listdir()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
im_1=plt.imread('antep.jpeg')
im_1.ndim,type(im_1),im_1.shape


# In[4]:


im_1[100,100,0]


# In[5]:


im_1[100,100,1]


# In[6]:


im_1[100,100,2]


# In[7]:


im_1[100,100,:]


# In[8]:


im_1[:,:,:]


# In[9]:


m,n,p=im_1.shape
m,n,p


# In[10]:


plt.imshow(im_1)
plt.show()


# In[11]:


new_image=np.zeros((m,n),dtype=float)
new_image


# In[12]:


for i in range(m):
    for j in range (n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2]/3)
        new_image[i,j]=s


# In[13]:


plt.imshow(new_image, cmap='gray')
plt.show()
plt.imsave('antep_2siyahbeyaz.jpeg', new_image,cmap='gray')


# In[14]:


new_image2=np.zeros((n,m),dtype=float)
new_image2


# In[15]:


for i in range(m):
    for j in range (n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2]/3)
        new_image2[j,i]=s


# In[17]:


plt.imshow(new_image2, cmap='gray')
plt.show()
plt.imsave('antep_90derece.jpeg', new_image2,cmap='gray')


# In[ ]:




