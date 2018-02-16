
# coding: utf-8

# In[6]:


pronoun_list=['we','she','he','we','us','me','we','us'] 

from collections import Counter
c = Counter(pronoun_list)

c.most_frequent(1)

