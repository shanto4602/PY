
# coding: utf-8

# In[12]:


alphabet = ['a','b','c','r','i','u','k','i','k','l','a','d','g','l','u','i','o']
char = []
for i in alphabet:
    if i not in char:
        char.append(i)
char.sort()
print(char)

