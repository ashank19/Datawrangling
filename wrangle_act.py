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

        
