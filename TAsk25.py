
# coding: utf-8

# In[2]:


Number = int(input("Please Enter the Range Number: "))
i = 0
First_Value = 0
Second_Value = 1
while(i < Number):
           if(i <= 1):
                      feb = i
           else:
                      feb = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = fib
           print(feb)
           i = i + 1

