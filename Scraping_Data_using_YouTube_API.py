# importing required libraries
import pandas as pd
from googleapiclient.discovery import build
import matplotlib.pyplot as plt

# API key
api_key = 'your_api'

# Construct a Resource for interacting with an API.
youtubeService = build('youtube', 'v3', developerKey=api_key)

# requesting the data
request = youtubeService.videos().list(part='snippet,contentDetails,statistics',
                                       chart='mostPopular', regionCode='IN',
                                       videoCategoryId='28', maxResults=50)

# initializing some basic data
getTopVideos = []
totalPages = 2
pageCounter = 0

# gathering the video data
while pageCounter != totalPages:
    response = request.execute()

    for resp in response['items']:
        getTopVideos.append(resp)

    # code to move to next page
    request = youtubeService.videos().list_next(request, response)
    pageCounter = pageCounter + 1

# get channel data for the videos
getTopChannelData = []
for topTech in getTopVideos:
    getResponse = youtubeService.channels().list(part='snippet,contentDetails,statistics',
                                                 id=topTech['snippet']['channelId']).execute()

    getTopChannelData.append(getResponse['items'][0])

youtubeService.close()

# extract subscriber count data from the received response
keyToCheck = 'subscriberCount'
for iCount in range(0, len(getTopChannelData)):
    tempData = getTopChannelData[iCount]['statistics']
    if keyToCheck not in tempData:
        getTopChannelData[iCount]['statistics']['subscriberCount'] = 0

finalList = []
# category of video
cats = ['', 'Film & Animation', 'Autos & Vehicles', '', '', '', '', '', '', '',
        'Music', '', '', '', '', 'Pets & Animals', '', 'Sports', 'Short Movies',
        'Travel & Events', 'Gaming', 'Videoblogging', 'People & Blogs',
        'Comedy', 'Entertainment', 'News & Politics', 'Howto & Style',
        'Education', 'Science & Technology', 'Nonprofits & Activism',
        'Movies', 'Anime/Animation', 'Action/Adventure', 'Classics',
        'Comedy', 'Documentary', 'Drama', 'Family', 'Foreign',
        'Horror', 'Sci-Fi/Fantasy', 'Thriller', 'Shorts',
        'Shows', 'Trailers']

# creating dataframe
for iCount in range(0, 100):
    tempDict = {}
    tempDict['Channel_Title'] = getTopChannelData[iCount]['snippet']['title']
    tempDict['Video_Title'] = getTopVideos[iCount]['snippet']['title']
    tempDict['Video_type'] = int(getTopVideos[iCount]['snippet']['categoryId'])
    tempDict['Video_type_name'] = cats[int(getTopVideos[iCount]['snippet']['categoryId'])]
    tempDict['Subscribers'] = int(getTopChannelData[iCount]['statistics']['subscriberCount'])
    tempDict['Video_Views'] = int(getTopVideos[iCount]['statistics']['viewCount'])
    tempDict['Like_Count'] = int(getTopVideos[iCount]['statistics']['likeCount'])
    # I found some of the videos not having this field. to prevent error this code
    try:
        tempDict['Comment_Count'] = int(getTopVideos[iCount]['statistics']['commentCount'])
    except:
        tempDict['Comment_Count'] = int(0)

    tempDict['Video_Count'] = int(getTopChannelData[iCount]['statistics']['videoCount'])
    finalList.append(tempDict)

createDataframe = pd.DataFrame(finalList)

createDataframe.to_excel('YouTube_data.xlsx')

# create pie diagram for the sum of all the video type and video type name
videoCount = createDataframe['Video_type_name'].value_counts()

fig = plt.figure(figsize=(10, 8))
plt.pie(videoCount, labels=videoCount.index,autopct='%1.1f%%')

# plot the number of video_views count by each category
videoViewCount = createDataframe.groupby('Video_type_name')['Video_Views'].sum()

fig = plt.figure(figsize=(10, 8))
plt.bar(videoViewCount.index,height=videoViewCount)
plt.xlabel('Video Type/Genre')
plt.ylabel('Video View Count')
plt.title('Video Type/Genre vs Video View Count')

# plot the number of like_views count by each category
likeCount = createDataframe.groupby('Video_type_name')['Like_Count'].sum()

fig = plt.figure(figsize=(10, 8))
plt.bar(likeCount.index,height=likeCount)
plt.xlabel('Video Type/Genre')
plt.ylabel('Like Count')
plt.title('Video Type/Genre vs Like Count')

# plot the number of comment_views count by each category
commentCount = createDataframe.groupby('Video_type_name')['Comment_Count'].sum()

fig = plt.figure(figsize=(10, 8))
plt.bar(commentCount.index,height=commentCount)
plt.xlabel('Video Type/Genre')
plt.ylabel('Comment Count')
plt.title('Video Type/Genre vs Comment Count')

# top 10 channels having highest number of subscribers
subCount = createDataframe.groupby(['Channel_Title','Video_type_name']).apply(lambda x:x['Subscribers']/1000000).nlargest(10).reset_index()
subCount = subCount.drop(columns='level_2')