
# coding: utf-8

# In[29]:


def is_odd(val):
    if val%2 is not 0:
        return True
    else :
        return False
def is_three(val):
    return int(val/3)
def is_four(val):
    return int(val/4)
def is_five(val):
    if val%5 is 0:
        return True
    else :
        return False
def noodle_count(money):
    return round(money/2500)

def buyNoodle(date,money):
    bonus = 0
    noodle = noodle_count(money)
    if is_odd(date) :
        bonus=bonus + is_three(noodle)
    if is_odd(date) is False : 
        bonus= bonus + is_four(noodle)
    if is_five(date):
        if is_odd(bonus)is False:
            bonus = bonus * 10
        else: 
            bonus = bonus * 5
    return noodle+bonus

