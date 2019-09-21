
# coding: utf-8

# In[102]:


def is_username_valid(username):
    import re
    if 5<=len(username) and len(username)<=9:
        return False
    else:
        result = re.match('[a-z]',username)
        if result:
            return True
        else:
            return False
def is_password_valid(password):
    import re
    if len(password) is not 10:
        return False
    else:
        result = re.match('[a-z0-9~!@#$%^&*]',password)
          
        if result:
            return True
        else:
            return False

