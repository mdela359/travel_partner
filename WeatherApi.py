#!/usr/bin/env python
# coding: utf-8

# In[271]:


import numpy as np


# In[272]:


import pandas as pd


# In[273]:


def combineDT(ltemp, ldate):
    finalL =[]
    for x in range(23):
        finalL.append((ltemp[x],ldate[x]))
    return finalL
def anon(lis,lisTwo):
    finalL =[]
    finalTwoL=[]
    for x in lis:
        finalL.append(x.replace("]",""))
    for x in lisTwo:
        finalTwoL.append(x.replace("]}}",""))
    return finalL,finalTwoL


api=pd.read_csv('https://api.open-meteo.com/v1/forecast?latitude=18.00&longitude=-76.79&hourly=temperature_2m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timeformat=iso8601&forecast_days=1&timezone=auto')


# In[274]:


date=api.columns[10:33] 
day= date[0][:10]


# In[275]:


tempF=api.columns[34:]


# In[276]:


timeL=np.array
for elt in date:
    timeL=np.append(timeL,elt[11:])
    
hrs= timeL[1:]

hrs,tempF=anon(hrs,tempF)
complete= combineDT (hrs,tempF)



# In[277]:


complete


# In[ ]:




