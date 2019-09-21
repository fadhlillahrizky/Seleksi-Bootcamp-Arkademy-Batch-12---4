
# coding: utf-8

# In[41]:


def count_handshake(input):
    result=0
    if input is None:
        return None
    if input < 1:
        return 0
    else:
        for i in range(input):
            people= input-1
            for j in range(people-i):
                result +=1
        return result
            
        
    


# In[42]:


input=4
result =0
for i in range(input):
            result +=1
result


# In[43]:


count_handshake(6)

