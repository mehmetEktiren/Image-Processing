#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os 
os.getcwd()


# In[2]:


my_list=[9,3,5,6,2,3,6]
my_list


# In[3]:


for i in my_list:  #listemizi tek tek dolaşır.
    print(i)


# In[4]:


for i in range(len(my_list)): #listeyi eleman sayısı kadar dolaşır, kaçıncı olduğunu bulmamız gerektiğinde kullanıır.
    print(i,my_list[i])


# In[5]:


import numpy as np


# In[6]:


def my_function_1(my_list=[9,3,5,6,2,3,6]):
    for i in range (len(my_list)):
       # print (i,my_list[i])
        my_list[i]=my_list[i]+1
    print (my_list)
my_function_1([5,5,5,5,5,5,5,5])
#my_function_1(['bir',2,3,4,54,5,56,6])  #String+1 olamayacağı için hata verir
my_function_1() #default olarak [9,3,5,6,2,3,6] listesini kullanır.


# In[7]:


my_list_1=np.array([9,3,5,6,2,3,6]) ##ndarray
my_list_1


# In[8]:


my_list_1+1


# In[9]:


def my_function_2(my_array=np.array([9,3,5,6,2,3,6])):
    return my_array+10
#my_function_1(['bir',2,3,4,54,5,56,6])
my_function_2()


# In[10]:


import numpy as np
import matplotlib.pyplot as plt 


# In[11]:


im_1=plt.imread('suleymaniye.jpeg')
plt.imshow(im_1)   
plt.show()


# In[12]:


m,n,p=im_1.shape
im_2=np.zeros((m,n,3),dtype=int)
for m in range(im_1.shape[0]): #shape olduğu için 'range' olmalı
    for n in range(im_1.shape[1]):
        im_2[m,n,0]=im_1[m,n,0]+100
        im_2[m,n,1]=im_1[m,n,0]
        im_2[m,n,2]=im_1[m,n,0]
        #pixel pixel gezip her pixel'i im_2 ye atarken işlem yapar
        
plt.imshow(im_2)
plt.show()


# In[13]:


im_1.ndim, im_1.shape


# In[14]:


def red_deger(im_3,s=5):
    #gönderilen resmin kırmızı değerini gönderilen s değerine göre arttıran/azaltan fonksiyon
    im_1=im_3
    m,n,p=im_1.shape
    im_2=np.zeros((m,n,3),dtype=int)
    m,n,p=im_2.shape
    for m in range(im_1.shape[0]): #shape olduğu için 'range' eklenmeli
        for n in range(im_1.shape[1]):
            im_2[m,n,0]=im_1[m,n,0]-s
            im_2[m,n,1]=im_1[m,n,0]
            im_2[m,n,2]=im_1[m,n,0]
            #pixel pixel gezip her pixel'i im_2 ye atarken işlem yapar
    return im_3
im_ret=red_deger(im_1,100)
plt.imshow(im_ret)
plt.show()


# In[15]:


m,n,p=im_1.shape
im_2=np.zeros((m,n,3),dtype=int)
m,n,im_2.shape
for m in range(im_1.shape[0]):
    for n in range(im_1.shape[1]):
        im_2[m,n,0]=im_1[m,n,0]-50  #R bantını 25 eksiltiyor 
        im_2[m,n,1]=im_1[m,n,1]
        im_2[m,n,2]=im_1[m,n,2]
plt.imshow(im_2)
plt.show()


# In[16]:


def my_function_3(im_100,s=5):
    im_1=im_100
    m,n,p=im_1.shape
    im_2=np.zeros((m,n,3), dtype=int)
    m,n,im_2.shape
    for m in  range (im_1.shape[0]):     
        for n in range(im_1.shape[1]):   
            im_2[m,n,0]=im_1[m,n,0]-s  #R bantını 25 eksiltiyor
            im_2[m,n,1]=im_1[m,n,1]
            im_2[m,n,2]=im_1[m,n,2]  
    return im_100


# In[17]:


def my_function_4(im_500): #boyutlandırma
    #gönderilen mxn lik resmi m/2 x n/2 lik yapan fonksiyon
    m,n,p=im_500.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_600=np.zeros((new_m,new_n),dtype=int)
    for m in range(new_m):
        for n in range(new_n):
            s0=(im_500[m*2,n*2,0]+im_500[m*2,n*2,1]+im_500[m*2,n*2,2])/3 #bulunulan piksel
            im_600[m,n]=int(s0)
    return im_600


# In[18]:


plt.imshow(im_1)
plt.show()
im_600=my_function_4(im_1)
plt.imshow(im_600,cmap='gray')
plt.show()
plt.imsave('suleymaniyeGray.jpg',im_600,cmap='gray')


# In[19]:


im_1.shape


# In[20]:


im_600.shape


# In[21]:


def my_scale(im_7):  #bozulmadan boyutlandırıyor
    m,n,p=im_7.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_8=np.zeros((new_m,new_n,3),dtype=int)
    for m in range(new_m):
        for n in range(new_n):
            im_8[m,n,0]=int(im_7[m*2,n*2,0])
            im_8[m,n,1]=int(im_7[m*2,n*2,1])
            im_8[m,n,2]=int(im_7[m*2,n*2,2])
    return im_8


# In[22]:


plt.imshow(im_1)


# In[23]:


im_10=my_scale(im_1)
plt.imshow(im_10)


# In[24]:


im_100=my_scale(im_10)
plt.imshow(im_100)


# In[25]:


im_1000=my_scale(im_100)
plt.imshow(im_1000)


# In[26]:


im_10000=my_scale(im_1000)
plt.imshow(im_10000)


# In[27]:


im_100000=my_scale(im_10000)
plt.imshow(im_100000)

