# Importing various packages

import pandas as pd
import numpy as np
import requests
import os

#Reading the WeRateDogs Twitter archive

df_1=pd.read_csv('twitter-archive-enhanced.csv')

# The tweet image predictions, i.e., what breed of dog (or other object, animal, etc.)
# is present in each tweet according to a neural network.
# This file (image_predictions.tsv) is hosted on Udacity's servers and
# has been downloaded programmatically using the Requests library and the following URL:
# https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv

url='https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv'
df1=pd.read_table(url,sep='\t')
