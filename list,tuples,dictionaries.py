#!/usr/bin/env python
# coding: utf-8

# In[33]:


#assigning elements to list
a=["1","2","3","4"]
a.append("5")
print(a)
a.extend(["e","w"])
print(a)
del(a[2])
print(a)

#acessing elements for tuples
a=("toy","1","race")
print(a[2])
print(a[-1])
print(a[0])

#deleting different dictionary elements
dictionary={"a":"apple","b":"banana","c":"cat","d":"dog"}
print(dictionary)
dictionary.pop("a")
print(dictionary)
del dictionary["c"]
print(dictionary)
dictionary.popitem()
print(dictionary)


# In[ ]:




