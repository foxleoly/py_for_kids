#!/usr/bin/env python
# coding: utf-8

# 数据类型(Data types)

# #### number

# In[1]:


1 + 1


# In[5]:


number1 = 100
number2 = 200
number3 = number1 + number2
print(type(number3))


# In[6]:


number1 = -1
number2 = number1 * 0
print(number2)
print(type(number2))


# In[11]:


import sys
-sys.maxsize
start = -sys.maxsize
end = sys.maxsize
print(f"python3 int range {start} - {end}")


# #### string

# In[17]:


text0 = 'Messi'
text1 = "Edison"
text2 = """ Messi and Edison"""
text_format = "{name1} and {name2}"

me_and_ed = text_format.format(name1=text0,name2=text1)
print(f"text formated ==> : {me_and_ed}")

me_and_ed = "%s and %s" % (text0, text1)
print(f"text formated2 ==> : {me_and_ed}")


# #### bool

# In[21]:


print('Result: ==>', 1 == 2)
print('Result: ==>', 2 == 2)

