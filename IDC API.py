
# coding: utf-8

# In[80]:


import base64
import json
import requests

encoded = base64.b64encode(b'd4capiq1:Spring18')

api_token='ZDRjYXBpcTE6U3ByaW5nMTg='

# api_url_base='https://apex.interactivedata.com/public/apex-api/' 

headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic {}'.format(api_token)}


def get_account_info():

    api_url = r'https://apex.interactivedata.com/public/apex/ws/v1?entities=ISIN:JP3633400001&items=instrument_id,organization_master.primary_name,equity.equity_details.ADR_depository_bank,equity.equity_details.nominal_value,instrument_id,master_information,global_information,debt,equity'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


# In[81]:


result=get_account_info()


# In[8]:


type(result[0])


# In[82]:


values=[]
for k,v in result[0].items():
    values.append(v)


# In[83]:


values


# In[70]:


eps_val=[]
for j in range(2,len(values)):
    val1=values[j].get("equity_EPS").get("EPS_date")
    eps_val.append(val1)
    val2=values[j].get("equity_EPS").get('EPS_diluted')
    eps_val.append(val2)
    val3=values[j].get("equity_EPS").get('EPS_diluted_date')
    eps_val.append(val3)
    val4=values[j].get("equity_EPS").get('EPS_update_date')
    eps_val.append(val4)
    val5=values[j].get("equity_EPS").get('EPS_year')
    eps_val.append(val5)


# In[71]:


eps_val


# In[52]:


values[2].get("equity_EPS")


# In[53]:


values[2].get("equity_EPS").get("EPS_date")
values[2].get("equity_EPS").get('EPS_diluted')
values[2].get("equity_EPS").get('EPS_diluted_date')
values[2].get("equity_EPS").get('EPS_update_date')
values[2].get("equity_EPS").get('EPS_year')


# In[66]:


for j in range(1,len(values)):
    print(j)


# In[67]:


values[2]

