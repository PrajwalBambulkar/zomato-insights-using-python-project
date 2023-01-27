#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Analysis 
# 
# Zomato API Analysis is one of the most useful analysis for foodies who want to taste the best cuisines of every part of the world which lies in their budget. This analysis is also for those who want to find the value for money restaurants in various parts of the country for the cuisines. Additionally, this analysis caters the needs of people who are striving to get the best cuisine of the country and which locality of that country serves that cuisines with maximum number of restaurants

# In[61]:


import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns #data visualisation
get_ipython().run_line_magic('matplotlib', 'inline')


# # We will read the Dataset

# In[2]:


zomato_df=pd.read_csv("zomato.csv",encoding='latin-1')
zomato_df.head()


# # Understanding the Data

# In[3]:


zomato_df.columns


# # The columns mentioned in the dataset 
# * Restaurant Id: Unique id of every restaurant across various cities of the world
# * Restaurant Name: Name of the restaurant
# * Country Code: Country in which restaurant is located
# * City: City in which restaurant is located
# * Address: Address of the restaurant
# * Locality: Location in the city
# * Locality Verbose: Detailed description of the locality 
# * Longitude: Longitude coordinate of the restaurant's location
# * Latitude: Latitude coordinate of the restaurant's location
# * Cuisines: Cuisines offered by the restaurant
# * Average Cost for two: Cost for two people 👫
# * Currency: Currency of the country
# * Has Table booking: yes/no
# * Has Online delivery: yes/ no
# * Is delivering: yes/ no
# * Switch to order menu: yes/no
# * Price range: range of price of food
# * Aggregate Rating: Average rating out of 5
# * Rating color: depending upon the average rating color
# * Rating text: text on the basis of rating of rating
# * Votes: Number of ratings casted by people

# In[50]:


#zomato_df.info(show_counts=False) # The info() method does not return any value, it prints the information.
zomato_df.info()


# In[5]:


zomato_df.dtypes   #look at the data types for each column


# In[6]:


zomato_df.describe() # It will only describe the numeric data columns


# In[7]:


zomato_df['Aggregate rating'].describe()  #It will only describe the numeric data columns of the specific column


# In[8]:


zomato_df.shape
#To Display all the numbers of rows and columns


# Total No of Rows and columns

# ## Data Analysis 
#     Check Missing Values

# In[9]:


zomato_df.isnull()


# It will return True for missing components and False for non-missing cells. 
# However, when the dimension of a dataset is large, it could be difficult to figure out the existence of missing values.

# In[10]:


zomato_df.isnull().values.any()


# Df.isnull().values.any() returns True when there is at least one missing value occurring in the data.

# In[11]:


zomato_df.isnull().sum() 
#To Check the NAN vaues


# In[52]:


sns.heatmap(zomato_df.isnull(),cmap="tab20")
#sns.heatmap(zomato_df.isnull())
plt.show()         # We are not able to see the 9 records as the NAN value is very small


# # Reading an excel file which is attached with the dataset

# In[13]:


country_df=pd.read_excel("Country-Code.xlsx") 


# In[14]:


country_df.head()


# In[15]:


zomato_df.columns


# In[16]:


#merging the data of country code with main data
zomato_final=pd.merge(zomato_df,country_df, on="Country Code",how="left")


# In[18]:


#To check the data types
zomato_final.dtypes


# In[53]:


zomato_final.shape


# In[17]:


zomato_final.head()


# In[19]:


zomato_final.columns 
#For all the columns name 


# In[20]:


zomato_final['Country'].value_counts() #name of country with no of values


# Observation- 
# 
# 1. Zomato is mostly used in India
# 2. In USA, they just have a website, which they will recommend some kind of restaurants.
# 3. Main base of Zomato is in India
# 

# In[55]:


zomato_final['Country'].value_counts().index
#We will get all the country name with respect to the record


# In[22]:


a=zomato_final['Country'].value_counts().index
#we are storing this values in 'a' variable which we will use in Pie Plots


# In[24]:


# We will see top 3 countries that uses Zomato
plt.pie(zomato_final['Country'].value_counts()[:3].values,labels = a[:3])


# In[25]:


#We will add percentage in the Pie chart 
plt.pie(zomato_final['Country'].value_counts()[:3].values,labels = a[:3],autopct='%.2f%%')


# Observation-
# 1. Most Revenue is generated in India 
# 2. Max sales in India is approx is 94.32%
# 3. In United States max sales approx is 4.73%
# 4. In United Kingdom max sales approx is 0.87%
# 
# These are the top 3 countries, most of his business is in India

# ### The survey seems to have spread across15 countries. This shows that Zomato is a multinational company having actives business in all those countries.

# As Zomato is a startup from India hence it makes sense that it has maximum business spread across restaurants in India
# 

# # Understanding the Rating aggregate, color and text

# In[26]:


ratings=zomato_final.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index()
ratings
# Check the ratings


# In[27]:


#We have rename the columns ---wherever there is 0 in column it will rename it to Counts
final_ratings=ratings.rename(columns={0:'Counts'})


# In[28]:


final_ratings


# In[29]:


final_ratings.head()


# Observation: 
#     
# The above information helps us to understand the realation between Aggregate rating, color and text. We conclude the following color assigned to the ratings:
# 1. Rating 0 - White - Not rated
# 2. Rating 1.8 to 2.4 - Red - Poor
# 3. Rating 2.5 to 3.4 - Orange - Average
# 4. Rating 3.5 to 3.9 - Yellow - Good
# 5. Rating 4.0 to 4.4 - Green - Very Good
# 6. Rating 4.5 to 4.9 - Dark Green - Excellent
# 

# # We will plot these ratings in a better way so that we can understand in a visualized form

# In[58]:


plt.figure(figsize=(12,6))
plt.xticks(rotation=30)
plt.title('Rating Color')
sns.barplot(x=final_ratings['Rating color'], y=final_ratings['Counts']);
#sns.barplot(x=final_ratings['Rating color'], color=['black', 'red', 'green', 'blue', 'cyan']);
plt.show()


# In[31]:


#We will see the relationship b/w Aggregate rating and 0 i.e counts
#plotting the count of rating with the color assigned to them in the dataset 
plt.figure(figsize=(12,6))
sns.barplot(x="Aggregate rating",y="Counts",data=final_ratings,hue="Rating color",palette=["Black","red","orange","yellow","green","green"])


# Observation:
# 1. 0 rating is more than 2000
# 2. Top rated is 4.9 rating
# 2. it looks like a Guasian curve i.e Normal distribution

# In[33]:


#Let us check who gave the most no. of zero rating country
zero_rating=zomato_final[zomato_final["Aggregate rating"]==0].groupby("Country").size().sort_values(ascending=False).reset_index().rename(columns={0:"Counts"})
zero_rating

Observation:
India seems to have maximum unrated restaurants.
# # Let us try to understand the coverage of city

# In[34]:


#city which has placed the most no. of orders on zomato
zomato_final["City"].value_counts()


# # From which New Delhi Locality maximum restaurants are listed in Zomato

# In[41]:


Delhi = zomato_final[(zomato_final.City == 'New Delhi')]
plt.figure(figsize=(12,6))
sns.barplot(x=Delhi.Locality.value_counts().head(21), y=Delhi.Locality.value_counts().head(21).index)

#plt.ylabel(None);
plt.xlabel('Number of Resturants')
plt.title('Resturants Listing on Zomato from New Delhi');

Observation:
Connaught place seems to have a high no of restaurants registered with Zomato, 
Now,Let us understand the cuisines the top-rated restaurants have to offer.
# # What kind of Cuisine these highly rates resturants offer

# In[45]:


# Achieve this by the following steps

## Fetching the resturants having 'Excellent' and 'Very Good' rating
ConnaughtPlace = Delhi[(Delhi.Locality.isin(['Connaught Place'])) & (Delhi['Rating text'].isin(['Excellent','Very Good']))]

ConnaughtPlace = ConnaughtPlace.Cuisines.value_counts().reset_index()

Cuisine


# In[37]:


zomato_final["Cuisines"].value_counts()[:20].sort_values(ascending=False)


# Observation: 
# 
# Top rated resturants seems to be doing well in the following cuisene
# 1. North Indian
# 2. Chinese
# 3. Fast Food
# 4. Mughlai

# # How many of such resturants accept online delivery

# In[48]:


top_locality = Delhi.Locality.value_counts().head(10) #Top 10 localities
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12,6))
#Show the counts of observations in each categorical bin using bars.
online_delivery= sns.countplot(y= "Locality", hue="Has Online delivery", data=Delhi[Delhi.Locality.isin(top_locality.index)])
plt.title('Resturants Online Delivery');

Observation:

Apart from Shahdara locality, restaurants in other localities accept online delivery.


Online Delivery seems to be on the higher side in Defence colony and Connaught Place.
# # Rating VS Cost of dinning

# In[39]:


plt.figure(figsize=(12,6))
sns.scatterplot(x="Average Cost for two", y="Aggregate rating", hue='Price range', data=Delhi)

plt.xlabel("Average Cost for two")
plt.ylabel("Aggregate rating")
plt.title('Rating vs Cost of Two');

Observation:
I observe there is no linear relation between price and rating. 
For instance, Resturants with good rating (like 4-5) have resturants with all the price range and spread across the entire X axis
# # Conclusion of the survey:
We've drawn many inferences from the survey. Here's a summary of a few of them:

1. The dataset is skewed towards India and doesnt represent the complete data of resturants worldwide.

2. Resturants rating is categorised in six categories
Not Rated
Average
Good
Very Good
Excellent
3. ConnaughtPlace have maximum resturants listed on Zomato but in terms of online delivery accpetance maliva nagar seems to be doing better.
4. The top rated resturants seems to be getting better rating on the following cuisines:
North Indian
Chinese
Fast Food
Mughlai
5. There is no relation between cost and rating. Some of the best rated resturants are low on cost and vice versa.
 The analysis is simple. The more exotic the cuisine gets the more rating it has.
# In[62]:


data=pd.read_csv("employees.csv")


# In[ ]:




