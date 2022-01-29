import os
import wordcloud as wd
from nltk.tokenize import word_tokenize 
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import spacy

# extract the data from text file and save in a list
def extract_file(pathname):
    fileList = [os.path.join(pathname, f) for f in os.listdir(pathname)]
    tempList = []
    for file in fileList:
        with open(file) as reader:
            tempRead = reader.readlines()
            tempList.append(tempRead[0])
    return tempList

# removing stopwords and extracting adjectives
def removeStopwords(movieReviews):
    uneeded_words = ['<','>','br','/']
    endResult = []    
    for movieReview in movieReviews:
        tokenizeSent = word_tokenize(movieReview)
        temperRead = [w for w in tokenizeSent if not w in uneeded_words]
        endResult.extend(temperRead)
        
    nlp = spacy.load('en_core_web_sm')
    
    adjectiveWords = []
    for movieReview in movieReviews:
        doc = nlp(movieReview)
        for word in doc:
            if word.pos_ == 'ADJ':
                adjectiveWords.extend([word.text])
        
    return (endResult,adjectiveWords)

positiveRev = extract_file('Path where the positive review folder is kept')
negativeRev = extract_file('Path where the negative review folder is kept')

posRevWoStpWrds,posWordsAdj = removeStopwords(positiveRev)
negRevWoStpWrds,negWordsAdj = removeStopwords(negativeRev)

#filtering and taking words having frequency greater than 3
dataPosAnalysis = FreqDist(posWordsAdj)
filterPosWords = dict([(m, n) for m, n in dataPosAnalysis.items() if n > 3])
dataNegAnalysis = FreqDist(negWordsAdj)
filterNegWords = dict([(m, n) for m, n in dataNegAnalysis.items() if n > 3])

# joining all words
allPosString = " ".join(filterPosWords)
allNegString = " ".join(filterNegWords)

stopwords = set(wd.STOPWORDS)

# setting the wordcloud attributes
wordcloudPos = wd.WordCloud(width = 400, height = 400,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(allPosString)

# setting the wordcloud attributes
wordcloudNeg = wd.WordCloud(width = 400, height = 400,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(allNegString)

# plotting the clouds
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloudPos)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

# plotting the clouds
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloudNeg)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()