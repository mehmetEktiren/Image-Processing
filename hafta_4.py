#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data_path = "C:/Users/hemeD/görüntü işleme/hafta_4/"
train_data = np.loadtxt(data_path + "mnist_train.csv", 
                        delimiter=",")
test_data = np.loadtxt(data_path + "mnist_test.csv", 
                       delimiter=",")


# In[3]:


image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size

test_data[:10]


# In[4]:


train_data.ndim,train_data.shape     #785 her bir resmin boyutu=28*28+1


# In[5]:


train_data[10,50] #10. satır 50. elemanı


# In[6]:


train_data[10,0] #10. satır 0. elemanı : eleman=3


# In[7]:


im_3=train_data[10,:] #10. satırdaki elemanları komple im_3'e atar
im_3.shape


# In[8]:


im_4=im_3[1:] 
im_4.shape


# In[9]:


im_5=im_4.reshape(28,28)


# In[10]:


plt.imshow(im_5,cmap='gray')
plt.show()


# In[11]:


m,n=train_data.shape
m,n 


# In[12]:


def my_count(k=0): #rakamlardan kaçar tane olduğunu bulan fonksiyon:
    s=0
    for i in range (m):
        if(train_data[i,0]==k):
            s=s+1
    return s #kaç tane k değeri olduğunu bastırır.
for i in range(10):
    c=my_count(i)
    print(i," ",c) # 0-10 sayılarından kaçar tane olduğunu yazdırır.


# In[13]:


#train_data[i,0]  #değeri söyler
#train_data[i,1]  #sol üstteki pixel
#train_data[i,784] #sağ alttaki değer


# In[14]:


import math
def my_pdf_1(x,mu=0.0,sigma=1.0):
    x=float(x-mu)/sigma
    return math.exp(-x*x/2.0)/math.sqrt(2.0*math.pi)/sigma
my_pdf_1(10,1,3)


# In[15]:


#değeri 0 olan resimlerin sol üstteki pixelin ortalama ve standart sapmasını bulan fonksiyon:
s,t,k=0,0,0
l=350 #lokasyon
for i in range (m):
    if(train_data[i,0]==k):
        s=s+1 #kaç tane var
        t=t+train_data[i,l+1] #instensity değerleri
mean_1=t/s #ortalama
s,t=0,0
for i in range (m):
    if(train_data[i,0]==k):
        s=s+1 #kaç tane var
        diff_1=train_data[i,l+1]-mean_1
        t=t+diff_1*diff_1
std_1=np.sqrt(t/(s-1))
print(mean_1,std_1)


# In[16]:


#yukarıdaki kodları fonksiyon haline getirdik: 
def get_my_mean_and_std(k=0,l=0):
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


# In[17]:


for i in range(m):
    digit_class=train_data[i,0]
    top_left=train_data[i,1]
    bottom_right=train_data[i,784]
    print(digit_class,end=" ")
    print(top_left,end=" ")
    print(bottom_right,end=" ")

