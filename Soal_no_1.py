
# coding: utf-8

# In[19]:


import json
def biodata():
    school_name = ['SDN 5 Metro Timur', 'SMPN 2 Metro', 'SMAN 2 Metro', 'Universitas Lampung']
    year_in = [2001,2007,2010,2013]
    year_out = [2007,2010,2013,2019]
    level = ['beginner', 'advanced', 'expert']
    Data = {
    'name' : 'Rizky Fadhlillah',
    'age' : 23,
    'address' : 'Jln. Terong Gg. Teladan N0.1 Iringmulyo, Metro Timur Kota Metro provinsi Lampung',
    'hobbies' : ['Problem Solvom','Renang'],
    'is_married' : False,

    'list_school' : {'name': school_name, 'year_in':year_in, 'year_out': year_out, 'major' : 'Physics'},

    'skills' : {'skill_name' : level},
    'interest_in_coding' : True
    }
    return Data


# In[21]:


with open("data_file.json", "w") as write_file:
    json.dump(biodata(), write_file)

