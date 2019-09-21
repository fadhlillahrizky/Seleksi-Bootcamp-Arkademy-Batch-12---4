
# coding: utf-8

# In[222]:


def fibo_val(Input,memo):
    if memo == []:
        if Input == 0:
            return 0,[]
        if Input ==1:
            return 1,[0,1]
    else :
        result = memo[0]+memo[1] 
        return result,[memo[1],result]
    
def fibo(row,col):
    result=[]
    val=[0,[]]
    if col==1 and row ==2:
        return [[0,1]]
    if col==2 and row ==1:
        return [0],[1]
    else:
        n=0
        for i in range(col):
            result.append([])
            for j in range(row):
                val= fibo_val(n,val[1])
                result[i].append(val[0]) 
                n+=1
        return result
    
    


# In[223]:


fibo_val(0,[])


# In[224]:


fibo(4,3)

