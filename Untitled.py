#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import matplotlib.pyplot as plt


# In[35]:


im_1=plt.imread('kus.jpeg')
im_1.ndim,type(im_1),im_1.shape


# In[36]:


im_1[100,100,:]


# In[38]:


m,n,p=im_1.shape
m,n,p


# In[39]:


plt.imshow(im_1)
plt.show()


# In[41]:


new_image=np.zeros((m,n),dtype=float)


# In[44]:


for i in range(m):
    for j in range (n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2])/3
        new_image[i,j]=s


# In[47]:


plt.imshow(new_image)
plt.show()


# In[43]:


plt.imshow(new_image)
plt.show()


# In[25]:


m,n,p=im_1.shape
m,n,p


# In[26]:


plt.imshow(im_1)
plt.show()


# In[27]:


new_image=np.zeros((m,n),dtype=float)
for i in range(m):
    for j in range (n):
        s=(im_1[i,j,0]+im_1[i,j,1]+im_1[i,j,2]/3)
        new_image[i,j]=s


# In[28]:


plt.imshow(new_image,cmap='gray')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[20]:


im_3=im_1+im_2
plt.imshow(im_3)
plt.show()


# In[ ]:




