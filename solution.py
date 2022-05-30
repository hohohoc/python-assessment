#!/usr/bin/env python
# coding: utf-8

# In[1]:


from websites.resources.data import WEBSITES
print(WEBSITES)


# Task One: Find Data
# Find and return a new list of data where each item's value key is equal to or greater than four.

# In[2]:


temp = []
for i in range(len(WEBSITES)):
    if WEBSITES[i].get('value') >= 4:
        temp.append(WEBSITES[i])
        
temp


# Task Two: Amend Data
# Amend the list so each domain key value is prepended with the string www.

# In[3]:


for i in range(len(WEBSITES)):
    y = 'www.' + WEBSITES[i].get('domain')
    WEBSITES[i]['domain'] = y
    
WEBSITES


# Task Three: Cleanse Data
# Some of the data is inaccurate, the secure key is set to False when the url key contains a URL beginning with https://. The opposite is also true in some cases.
# 
# The list should be cleansed and returned so the secure keys are accurate.

# In[8]:


search_key = 'https'

for x in range(len(WEBSITES)):
    if search_key in WEBSITES[x]['url']:
        WEBSITES[x]['secure'] = 'True'
    else:
        WEBSITES[x]['secure'] = 'False'

WEBSITES


# Task Four: Data Calculation
# Add up all the value keys in the list and return an integer.

# In[11]:


sum = 0

for i in range(len(WEBSITES)):
    sum += WEBSITES[i]['value']
    
sum

