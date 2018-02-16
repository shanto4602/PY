
# coding: utf-8

# In[2]:


num = input('Enter a number ')
num = int(num)
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# In[4]:


num = input('Enter a number ')
num = int(num)
if (num%10==0) and (num%50==0) and (num%30==0):
    print ('This number is divisible by 10, 50 and 30')
else:
    print ('This number divisible by 10 and 50 but not 30')

