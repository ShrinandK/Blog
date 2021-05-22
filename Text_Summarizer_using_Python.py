import fitz # PyMuPDF
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk import word_tokenize
import heapq

# read the pdf file
def readPdf(pdfPath):
    pdfFileObj = fitz.open(pdfPath)
    allPageDict = dict()
    
    pageNum = pdfFileObj.pageCount
    
    # extract the text from the pages into dictionary
    # with keys as page number
    for iCount in range(0,pageNum):
        pageObj = pdfFileObj.loadPage(iCount)
        allPageDict[iCount] = pageObj.getText()
        
    pdfFileObj.close()  
    return allPageDict

# extract summary for each page
def summEachPage(pageWiseList):
    pageWiseFreq = {}
    
    for iCount in range(0,len(pageWiseList)):
        # extract the word frequency for each page
        wordFrequencies = findWordFreq(pageWiseList[iCount])
        # get the sentence score for each page
        sentScore = findSentScore(wordFrequencies,pageWiseList[iCount])
        # get top 5 sentence 
        summary_sentences = heapq.nlargest(3, sentScore, key = sentScore.get)
        summary = ' '.join(summary_sentences)
        # insert into a dictionary
        pageWiseFreq[iCount] = summary
    return pageWiseFreq
      
# find the word frequencies  
def findWordFreq(pageWiseList): 
    # check for stopwords in english
    stopwordEng = stopwords.words('english')
    word_frequencies = {}
    # get the word frequency
    for word in word_tokenize(pageWiseList):
        if word not in stopwordEng:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
                
    # get the word with maximum number
    maximum_frequency = max(word_frequencies.values())
    
    # get the weighted word frequency for each word
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
    
    return word_frequencies

# find sentence score
def findSentScore(wordFrequencies,wholePage):
    sentence_scores = {}
    # sentence tokenize the page
    sentence_list = sent_tokenize(wholePage)
    # for each sentence
    for sent in sentence_list:
        # get all the words in the single sentence
        for word in word_tokenize(sent.lower()):
            # check if word is in the wordFreq dictionary
            if word in wordFrequencies.keys():
                # add the word freq in each sent 
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = wordFrequencies[word]
                else:
                    sentence_scores[sent] += wordFrequencies[word]
                    
    return sentence_scores

# path of pdf
pdfPath = 'Tiger.pdf'

pageDict = readPdf(pdfPath)

pageWiseSummary = summEachPage(pageDict)

# write the data into text if needed 
file1 = open("Summary.txt","a+", encoding='utf-8') 
    
for key,value in pageWiseSummary.items():
    file1.write("Page " + str(key + 1) + " \n")
    file1.writelines(value)
    file1.write("\n\n")
    
file1.close()