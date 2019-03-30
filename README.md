# Datawrangling
Project Report
Initial stage- Understanding the objective
In this stage I first did go through the project objective as to what the reviewer expects from me in this project. Here using Python and its libraries, I did gather data from a variety of sources and in a variety of formats, assessed its quality and tidiness, then cleaned it.

Data Overview
The dataset used for wrangling (and analyzing and visualizing) is the tweet archive of Twitter user @dog_rates, also known as WeRateDogs. WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog. These ratings almost always have a denominator of 10. The numerators,almost always greater than 10. 11/10, 12/10, 13/10, etc. WeRateDogs has over 4 million followers and has received international media coverage.

Gathering the data
Here data is available from three different sources each in a different format.

Enhanced twitter archive
The WeRateDogs Twitter archive contains basic tweet data for all 5000+ of their tweets, but not everything. One column the archive does contain though: each tweet's text, which was used to extract rating, dog name, and dog "stage" (i.e. doggo, floofer, pupper, and puppo) to make this Twitter archive "enhanced." Of the 5000+ tweets,having filtered for tweets with ratings only (there are 2356).

This file was available on hand,so I downloaded this file manually by clicking on the given download link.

The tweet image predictions
The tweet image predictions i.e. what breed of dog (or other object, animal, etc.) is present in each tweet according to a neural network. This file (image_predictions.tsv) was hosted on Udacity's servers and downloaded programmatically using the Requests library and the following URL: https://d17h27t6h515a5.cloudfront.net/topher/2017/August/599fd2ad_image-predictions/image-predictions.tsv

Each tweet's retweet count and favorite count
Each tweet's retweet count and favorite ("like") count at minimum, and any additional data I find interesting. Using the tweet IDs in the WeRateDogs Twitter archive, querying the Twitter API for each tweet's JSON data using Python's Tweepy library and store each tweet's entire set of JSON data in a file called tweet_json.txt file. Each tweet's JSON data being written to its own line. Then reading this .txt file line by line into a pandas DataFrame with (at minimum) tweet ID, retweet count, and favorite count.

The above procedure required setting up of a twitter developer account which requires approval from twitter legitimately so instead I chose the other method to gather this data without creating a developer account.

The resulting data from twitter_api.py, i.e. the text file was provided as a download link.Then I read this tweet_json.txt file line by line into a pandas DataFrame tweet ID, retweet count, and favorite count."

Assessing the data
Here first visually each of the three dataframes so as to look for issues which can be easily figured out thereafter descriptive statistics and and column info for eache table was assessed.`

Enhanced twitter archive
'None' as a dog name in names (which is a proper noun) column.
'None' present in all dog status columns for multiple records.
Erroneous data type of tweet id column.
Presence of retweet id's.
Erroneous datatype of timestamp column.
Different column for every dog status instead of a single column.
Tweet_image_pred table
Erroneous data type of tweet id column.
Api_data table
Characters in retweet count column.
Characters in favorite count column.
Erroneous data type of retweet count and favorite count column.
This table should be a part of Twitter archive table.
Cleaning the data
Here each and every issue stated above was resolved through the sequence of define,code and test i.e.

First the issue was clearly stated.
Error free code required to resolve the issue was written and executed.
After execution of the code the table was tested so as to ensure that the issue has been resolved and further no new is found.
This procedure has been followed for every issue.

Exploratory analysis
Here different visualisation of matplotlib library function has been used so as to draw insights from the given the dataset after it has been cleaned.

Firstly a pie chart depicting the proportion of dog status of the entire dataset is plotted using the pyplot function of matplotlib library. From the above pie chart it is clear that majority of the tweets does not contain the dog status information and among those who contain the information 'Pupper' forms the major proportion.

A scatter plot using the matplotlib library is plotted between retweet count and favorite count so as to see whether a relationship exists between them. The correlation coefficient between is also calculated which shows that a positive correlation exists. Also linear regression is performed and the regression is plotted on the scatter plot. The regression line aligns with data points in a particular direction and treats the points above it as outliers, thereby depicting that the correlation is not strongly positive i.e. there may be more underlying factors which need to be taken in account.

Three bar charts is plotted for comparing the prediction proportion of each attempt so as to figure out that are they independent of each other or not.It is clear that each prediction attempt is independent of each other as the proportion of correct prediction is almost same.

Conclusion
In this section conclusions have been drawn depending upon the visualisation in the exploratory analysis.
