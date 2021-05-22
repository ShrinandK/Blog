import spacy
import pandas as pd

# function to check the type of sentence
def checkForSentType(inputSentence):   
    # running the model on sentence
    getDocFile = nlp(inputSentence)
    
    # getting the syntactic dependency 
    getAllTags = [token.dep_ for token in getDocFile]
    
    # checking for 'agent' tag
    checkPassiveTest = any(['agent' in sublist for sublist in getAllTags])
    
    # checking for 'nsubjpass' tag
    checkPassiveTestTwo = any(['nsubjpass' in sublist for sublist in getAllTags])
    return checkPassiveTest or checkPassiveTestTwo

# Spacy model imported
nlp = spacy.load("en_core_web_md")

# reading the list of test sentences
dfs = pd.read_csv('Sentence_List.txt')
sentences = dfs.values.tolist()

finalResult = []

# checking each sentence for its type
for sentence in sentences:
    result = checkForSentType(str(sentence))
    if(result):
        finalResult.append('Passive Sentence')
    else:
        finalResult.append('Active Sentence')
        
# storing the result in a new file and converting to csv
newDf = pd.DataFrame({'Sentences':sentences,'Answers':finalResult})

newDf.to_csv('Sentence_Identified.csv')