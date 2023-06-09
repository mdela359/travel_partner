#libraries 
import numpy as np       
import pandas as pd
#functions
def combineDT(ltemp, ldate):            #combine hour with tempature 
    finalL =[]
    for x in range(23):
        finalL.append((ltemp[x],ldate[x]))
    return finalL

def anon(lis,lisTwo):                  # remove random stuff 
    finalL =[]
    finalTwoL=[]
    for x in lis:
        finalL.append(x.replace("]",""))
    for x in lisTwo:
        finalTwoL.append(x.replace("]}}",""))
    return finalL,finalTwoL

# call api
api_key=pd.read_csv('https://api.open-meteo.com/v1/forecast?latitude=18.00&longitude=-76.79&hourly=temperature_2m&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch&timeformat=iso8601&forecast_days=1&timezone=auto')
# get temp and hrs for weather
date=api_key.columns[10:33] 
# get current date
day= date[0][:10]
#get temps
tempF=api_key.columns[34:]

# create numpy array 
timeL=np.array
for elt in date:
    timeL=np.append(timeL,elt[11:])
#get hrs    
hrs= timeL[1:]

hrs,tempF=anon(hrs,tempF)
complete= combineDT (hrs,tempF)

# (hrs,temp)
complete






