#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data_path = "C:/Users/hemeD/görüntü işleme/hafta_4/"
train_data = np.loadtxt(data_path + "mnist_train.csv",delimiter=",") 
test_data = np.loadtxt(data_path + "mnist_test.csv", delimiter=",")


# In[3]:


train_data.ndim,train_data.shape  


# In[4]:


def get_my_mean_and_std(k=0,l=0,m=10000):
        s=0
        t=0
        for i in range(m):
            if(train_data[i,0]==k):
                s=s+1
                t=t+train_data[i,l+1]
        mean_1=t/s

        s,t=0,0
        for i in range(m):
            if(train_data[i,0]==k):
                s=s+1
                diff_1=train_data[i,l+1]-mean_1
                t=t+diff_1*diff_1
        std_1=np.sqrt(t/(s-1))
        return mean_1,std_1


# In[5]:


import math
def my_pdf_1(x,mu=0.0,sigma=1.0):
    eps=np.finfo(float).eps
    x=float(x-mu)/(sigma+eps)
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/(sigma+eps)


# In[6]:


test_data.shape


# In[7]:


c=1
l=100
get_my_mean_and_std(c,l)


# In[8]:


#test_data[100,:] #0-255 arasında değerleri var 
test_value=45
my_pdf_1(test_value,4.0,2.0)


# In[9]:


my_test_im=plt.imread('deneme.jpeg')
plt.imshow(my_test_im,cmap='gray')
plt.show()


# In[10]:


my_test_im.shape
im2=my_test_im[:,:,0]
im2.shape #3 boyutlu olmaması için


# In[11]:


im3=im2.reshape(1,784)
im3.shape


# In[12]:


for i in range (10): 
    pdf_t=0
    for j in range (784):
        x=im3[0,j] #x=j'nin gösterdiği pixel değeri
        m1,std1=get_my_mean_and_std(i,j) #i.satırdaki ortalama ve varyans'ı yazar
        pdf_deger=my_pdf_1(x,m1,std1)
        pdf_t=pdf_t+pdf_deger
    print(pdf_t)


# In[13]:


list_1=[]
for i in range (10): 
    pdf_t=0
    for j in range (784):
        x=im3[0,j] #x=j'nin gösterdiği pixel değeri
        m1,std1=get_my_mean_and_std(i,j) #i.satırdaki ortalama ve varyans'ı yazar
        pdf_deger=my_pdf_1(x,m1,std1)
        pdf_t=pdf_t+pdf_deger
    #print(pdf_t)
    list_1.append(pdf_t)
print(max(list_1))

