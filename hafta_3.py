#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list_1=[2,4,3,4,5,6,3,3,2,1]
def my_function_1(my_list_1=[2,4,3,4,5,6,3,3,2,1]):
    t=0
    s=0
    for i in my_list_1:
        s=s+1
        t=t+i
    mean_1=t/s #ortalama
    
    t=0       
    s=0
    for i in my_list_1:
        s=s+1
        t=t+(i-mean_1)*(i-mean_1)
    var_1=t/(s-1)   #varyans
    
    return mean_1,var_1
my_function_1()


# In[2]:


#histogram bilgisini elde etme:
my_histogram={}   #erişimin hızlı olması için
for i in my_list_1:
    if i in my_histogram.keys():
        my_histogram[i]=my_histogram[i]+1    #listede bu eleman varsa sayıyı 1 arttır
    else:
        my_histogram[i]=1     #eğer o eleman daha önce bulunmadıysa 1 yazdır
my_histogram   #çıktı -> 2 sayısı 2 tane var, 4 sayısı 1 tane var


# In[3]:


for i in my_histogram.keys():
    print(i,my_histogram[i])
#my_histogram.keys() hangi elemandan kaç tane olduğunu listeler


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
image_1=plt.imread('truva.jpeg')
image_1.ndim,image_1.shape


# In[5]:


#histogramı bulan fonksiyon:
def my_function_2(image_1=plt.imread('truva.jpeg')):
    m,n,p=image_1.shape
    my_histogram={}
    for i in range(m):
        for j in range(n):
            if image_1[i,j,0] in my_histogram.keys():
                my_histogram[image_1[i,j,0]]=my_histogram[image_1[i,j,0]]+1
            else:
                my_histogram[image_1[i,j,0]]=1
    return my_histogram


# In[6]:


def my_function_3(my_histogram=my_function_2()):
    x=[]  #soldaki değerler
    y=[]   #sağdaki değerler
    for key in  my_histogram.keys():
        x.append(key)
        y.append(my_histogram[key])
    return x,y


# In[7]:


x,y=my_function_3()
plt.bar(x,y)  #grafiğe aktarma
plt.show()

