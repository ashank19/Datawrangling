# Project: Data Wrangling

#Table of Contents
#Introduction
#Gathering Data
#Assessing Data
#Cleaning Data
#Conclusion


#Introduction

# The dataset is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs.

# WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost always have a denominator of 10.

# WeRateDogs has over 4 million followers and has received international media coverage.

# wrangling and analysis further

# Importing packages planned to use for data wrangling and analysis further.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Gathering data

# Twitter archive file available at hand.

twitter_archive=pd.read_csv('twitter-archive-enhanced.csv')

# The tweet image predictions, i.e., what breed of dog (or other object, animal, etc.) is present in each tweet according to a neural network.

url='https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
tweet_image_pred=pd.read_table(url,sep='\t')

# This is the resulting data from twitter_api.py.

# Downloading it from the link on the Project Details page.

lines=[]
with open('tweet_json.txt','rt') as file:
    for line in file:
        lines.append(line)

# Extracting required data from each line.
f=[]
for line in lines:
    g=[]
    k=line.find('id_str')
    s=line[k+10:k+28]
    g.append(s)
    k=line.find("retweet_count")
    s=line[k+16:k+20]
    g.append(s)
    k=line.find('favorite_count')
    s=line[k+17:k+22]
    g.append(s)
    f.append(g)

# Converting the above extracted data into a pandas dataframe.
api_data=pd.DataFrame(f,columns=['tweet_id','retweet_count','favorite_count'])


# Assessing data

twitter_archive

tweet_image_pred

api_data

# Column info of each table

twitter_archive.info()

tweet_image_pred.info()

api_data.info()

# Assessing columns of twitter_archive Table

list(twitter_archive)

# Descriptive analysis of each table.

twitter_archive.describe()

api_data.describe()

tweet_image_pred.describe()

tweet_image_pred.sample(5)

# Quality issues

# Api_data table

# Characters in retweet count column.
# Characters in favorite count column.
# Erroneous data type of retweet count and favorite count column.

# Twitter_archive table
# Erroneous data type of tweet id column.
# 'None' as a dog name in names (which is a proper noun) column.
# 'None' present in all dog status columns for multiple records.
# Presence of retweet id's.
# Erroneous datatype of timestamp column.

# Tweet_image_pred table
# Erroneous data type of tweet id column.

# Tidiness issues

# Different columns for every dog status.
# Api_data table should be a part of twitter_archive table.


# Cleaning data


# Creating a copy of dataset before cleaning.
twitter_archive_clean=twitter_archive.copy()
tweet_image_pred_clean=tweet_image_pred.copy()
api_data_clean=api_data.copy()

# Define:

# Retweet Count column should only contain integers and no characters.

# Code

for i in range(len(api_data_clean)):
    if((',') in (api_data_clean.loc[i,'retweet_count'])):
        k=api_data_clean.loc[i,'retweet_count'].index(',')
        api_data_clean.loc[i,'retweet_count']=api_data_clean.loc[i,'retweet_count'][:-(len(api_data_clean.loc[i,'retweet_count'])-k)]

# Test

api_data_clean['retweet_count']

# Define:

# Favorite count column should only contain integers and no characters.

# Code

for i in range(len(api_data_clean)):
    if((',') in (api_data_clean.loc[i,'favorite_count'])):
        k=api_data_clean.loc[i,'favorite_count'].index(',')
        api_data_clean.loc[i,'favorite_count']=api_data_clean.loc[i,'favorite_count'][:-(len(api_data_clean.loc[i,'favorite_count'])-k)]

# Test

api_data_clean['favorite_count']

# Define

# Erroneous datatype of count columns, count column should be of integer type.

# Code

api_data_clean['retweet_count']=api_data_clean['retweet_count'].astype(int)
api_data_clean['favorite_count']=api_data_clean['favorite_count'].astype(int)

# Test

api_data_clean.info()

# Define

# Tweet id column should be of str type.in archive table.

# Code

twitter_archive_clean['tweet_id']=twitter_archive_clean['tweet_id'].astype(str)

#Test

twitter_archive_clean.info()

# Define

# Replacing dog names with unknown from none which clearly specifies that the name is not available.

# Code

twitter_archive_clean.name=twitter_archive_clean.name.replace('None','Unknown')

# Test

twitter_archive_clean.name.value_counts()

# Define

# Different columns for every dog status all of them can be combined into a single column(dog_status).

# Code

# Converting the columns into str type and also adding a new column 'dog_status'.
​
twitter_archive_clean['doggo']=twitter_archive_clean['doggo'].astype(str)
twitter_archive_clean['floofer']=twitter_archive_clean['floofer'].astype(str)
twitter_archive_clean['pupper']=twitter_archive_clean['pupper'].astype(str)
twitter_archive_clean['puppo']=twitter_archive_clean['puppo'].astype(str)
twitter_archive_clean.loc[:,'dog_status']=' '
​
# Filling values in the newly defined column as per originally filled value
​
for i in range(len(twitter_archive_clean)):
    if(twitter_archive_clean.loc[i,'doggo'] == 'None' and twitter_archive_clean.loc[i,'floofer'] == 'None' and twitter_archive_clean.loc[i,'pupper'] == 'None' and twitter_archive_clean.loc[i,'puppo'] == 'None'):
        twitter_archive_clean.loc[i,'dog_status']= 'None'
    elif(twitter_archive_clean.loc[i,'doggo'] == 'doggo' and twitter_archive_clean.loc[i,'floofer'] == 'None' and twitter_archive_clean.loc[i,'pupper'] == 'None' and twitter_archive_clean.loc[i,'puppo'] == 'None'):
        twitter_archive_clean.loc[i,'dog_status'] = 'Doggo'
    elif(twitter_archive_clean.loc[i,'doggo'] == 'None'and twitter_archive_clean.loc[i,'floofer'] == 'floofer' and twitter_archive_clean.loc[i,'pupper'] == 'None' and twitter_archive_clean.loc[i,'puppo'] == 'None' ):
        twitter_archive_clean.loc[i,'dog_status'] = 'Floofer'
    elif(twitter_archive_clean.loc[i,'doggo'] == 'None' and twitter_archive_clean.loc[i,'floofer'] == 'None' and twitter_archive_clean.loc[i,'pupper'] == 'pupper' and twitter_archive_clean.loc[i,'puppo'] == 'None'):
        twitter_archive_clean.loc[i,'dog_status'] = 'Pupper'
    else:
        twitter_archive_clean.loc[i,'dog_status'] = 'Puppo'
​
# Dropping the rest columns
​
twitter_archive_clean=twitter_archive_clean.drop(['doggo','floofer','pupper','puppo'],axis=1)


# Test

twitter_archive_clean

# Define

# Replacing 'None' value in dog status column with 'Unknown' as it specifies clearly that dog status is not mentioned for that particular tweet id.

# Code

twitter_archive_clean.dog_status=twitter_archive_clean.dog_status.replace('None','Unknown')

# Test

twitter_archive_clean

# Define

# Api_data table can be merged to twitter_archive table on the basis of tweet id and two more columns can be added to the twitter archive table.

# As it also contains retweets so having a separate table for retweets and favorite count is not worth it.

# Code

twitter_archive_clean=pd.merge(twitter_archive_clean,api_data_clean,on='tweet_id',how='left')

# Test

twitter_archive_clean.info()

# Define

# Removing retweets from twitter archive table,for a tweet id being a retweet,retweet_status_user_id should not be null.

# Code

# Removing all retweets

twitter_archive_clean=twitter_archive_clean[pd.isnull(twitter_archive_clean['retweeted_status_user_id'])]

# As the remaining columns 'retweeted_status_user_id','retweeted_status_id' and'retweeted_status_timestamp' contains all null values

# so dropping them off.

twitter_archive_clean=twitter_archive_clean.drop(['retweeted_status_user_id','retweeted_status_id','retweeted_status_timestamp'],axis=1)
twitter_archive_clean=twitter_archive_clean.reset_index(drop=True)

# Test

twitter_archive_clean

# Define

# Changing the datatype of timestamp column in twitter archive table to date time format

# Code

twitter_archive_clean['timestamp']=pd.to_datetime(twitter_archive_clean['timestamp'])

# Test
twitter_archive_clean.info()

# Define

# Changing the datatype of retweet count and favorite count column to integer type as count is always a whole number not a float.

# Code

# Filling the null values with count 0.
​
twitter_archive_clean.retweet_count=twitter_archive_clean.retweet_count.fillna(0)
twitter_archive_clean.favorite_count=twitter_archive_clean.favorite_count.fillna(0)
​
# Changing their datatypes
​
twitter_archive_clean['retweet_count']=twitter_archive_clean['retweet_count'].astype(int)
twitter_archive_clean['favorite_count']=twitter_archive_clean['favorite_count'].astype(int)


# Test

twitter_archive_clean.info()

# Saving the twitter_archive_clean file to csv format

twitter_archive_clean.to_csv('twitter_archive_master',index=False)

# Define

# Changing the datatype of tweet id column in tweet_image_pred table i.e. it should be of str type rather than int type.

# Code

tweet_image_pred_clean['tweet_id']=tweet_image_pred_clean['tweet_id'].astype(str)

# Test

tweet_image_pred_clean.info()


# Exploratory data analysis


# Distribution of dog status depicted through pie chart

dog_status=twitter_archive_clean['dog_status'].value_counts()
dog_status.plot(kind='pie',figsize=(20,10));

# From the above pie chart it is clear that majority of the tweets does not contain the dog status information and among those who contain the information 'Pupper' forms the major proportion.


# Correlation between retweet count and favorite count depicted through scatter plot also line of best fit plotted through linear reegression.

# Correlation between retweet count and favorite count
# depicted through scatter plot also line of best fit plotted through linear reegression.

twitter_archive_clean.plot.scatter(y='favorite_count',x='retweet_count')


# Correlaion coefficient between favorite count and retweet count.

twitter_archive_clean['retweet_count'].corr(twitter_archive_clean['favorite_count'])


# Importing relevant libraries for linear regression.

import statsmodels.api as sm
import seaborn as sb

x=twitter_archive_clean['retweet_count']
y=twitter_archive_clean['favorite_count']

# Performing linear regression and depicting the summary.

x1=sm.add_constant(x)
results=sm.OLS(y,x1).fit()
results.summary()

# Plotting the regression line on the scatter plot

sb.set()
plt.scatter(x,y)
y1=3.4138*x+1658.0587
fig=plt.plot(x,y1,lw=4,c='red',label='regression line')
plt.show()

# The correlation coefficient obtained between the two quantities show that there is a positive correlation between them.

# The regression line aligns with data points in a particular direction and treats the points above it as outliers, thereby depicting that the correlation is not strongly positive i.e. there may be more underlying factors which need to be taken in account.

#Comparing the prediction proportion of all the three attempts.

# Prediction proportion of 1st attempt.

c=tweet_image_pred_clean.p1_dog.mean()
k=['True','False']
plt.bar(k,[c,(1-c)])
plt.title("Proportion of correct prediction in 1st attempt")
plt.ylabel("Proportion");

# Prediction proportion of 2nd attempt.

c=tweet_image_pred_clean.p2_dog.mean()
k=['True','False']
plt.bar(k,[c,(1-c)])
plt.title("Proportion of correct prediction in 2nd attempt")
plt.ylabel("Proportion");

# Prediction proportion of 3rd attempt.

c=tweet_image_pred_clean.p3_dog.mean()
k=['True','False']
plt.bar(k,[c,(1-c)])
plt.title("Proportion of correct prediction in 3rd attempt")
plt.ylabel("Proportion");

# From the above three bar graphs it is clear that each prediction attempt is independent of each other as the proportion of correct prediction is almost same.

# Conclusion

# From the pie hart it is clear that majority of the tweets does not contain the dog status information and among those who contain the information 'Pupper' forms the major proportion.

# The correlation coefficient obtained between the two quantities show that there is a positive correlation between them.

# The regression line aligns with data points in a particular direction and treats the points above it as outliers, thereby depicting that the correlation is not strongly positive i.e. there may be more underlying factors which need to be taken in account.

# From the three bar graphs of prediction proportion it is clear that each prediction attempt is independent of each other as the proportion of correct prediction does not vary much.

# Websites referred

https://stackoverflow.com/

https://pandas.pydata.org/
