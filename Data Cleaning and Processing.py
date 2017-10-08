
# coding: utf-8

# In[70]:

import numpy as np
import pandas as pd
import scipy
import seaborn as sns
sns.set_style('whitegrid')
import matplotlib.pyplot as plt

get_ipython().magic('matplotlib inline')
plt.rcParams["patch.force_edgecolor"] = True


# In[71]:

digital = pd.read_csv('WB_Data_Digital.csv')


countries = pd.read_csv('List of countries.csv', )
countries = countries[['Economy', 'Code', 'Region']]
countries.head()


# In[38]:

#read in dataframe of country groups
groups = pd.read_csv('WB_Group.csv')
groups.rename(columns={'variable' : 'year'}, inplace = True )
groups.drop('Unnamed: 0', axis = 1, inplace = True)

# Therefore, I will first do an inner join with countries and then an outer join with groups

# In[79]:

between = pd.merge(left = digital, right = countries, left_on='country', right_on ='Economy').drop('Economy', axis = 1)
finaldf = pd.merge(left = between, right = groups, left_on = ['country', 'date'], right_on = ['country', 'year'], how = 'left')


#for the sake of uniformity, exchange .. for np as missing data container
finaldf['cgroup' == '..'] = np.nan



# In[104]:

finaldf.drop(False, axis =1, inplace = True)

# In[107]:

digital= finaldf.copy()


# ## Dealing with Missing Values

from Function_impute import clean_all_na


# In[ ]:

##

for x in list(digital.columns)[2:9]:
    digital = clean_all_na(digital, 'country', x)

# ### Zooming in On the missing values for all variables: 
# Is time or country a better predictor?

# In[ ]:

digital['Fixed broadband %'] *= 100



# In[ ]:

#now we can try to impute the missing valuesimpute the missing values everywhere but Access Electricity


# In[ ]:
digital_1996 = digital[digital['date'] >= 1996]


#first, transform data to multi-index
test = digital_1996[(digital_1996['country'] == 'Germany') | (digital_1996['country'] == 'Greece')]
mi = test.set_index(['date', 'country'])


# Strategy for filling in missing values:
# First, if there are no values before, and it makes sense: 0
# Second, if I have the value before and after, take the mean
# (Third) Access Electricity could be interpolated

# In[ ]:

new_df = mi.copy()


# In[ ]:

mi.loc[(1996, "Germany"), "Access Electricity"]


# In[ ]:

import clean_nan_testing as cln

new_df = mi.copy()
new_df = cln.clean_nan(new_df, new_df.columns[2:3])



# In[ ]:


# In[ ]:

#Nauru and Palau have to be left out


# In[ ]:




