
# coding: utf-8

# In[7]:


sen = 'I am Bangladeshi,I am proud of myself'
vowels = list("aeiou")
consonants = list("bcdfghjklmnpqrstvwxyz")
v = 0
c = 0
for i in sen:
    if i in vowels:
        v+=1
    elif i in consonants:
        c+=1
print("Number of vowel",v,"Number of comsonatant",c)


# In[8]:


len('I am Bangladeshi,I am proud of myself')

