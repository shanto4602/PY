
# coding: utf-8

# In[2]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Enter the number : "))
print(factorial(n))

