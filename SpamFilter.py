# Naive Bayes Spam Filter - Kamil Sacha

# Imports needed to process Kaggle data
# Link to Kaggle data: https://www.kaggle.com/karthickveerakumar/spam-filter
# Refrence: https://www.youtube.com/watch?v=7-97jlHAKqk&ab_channel=AladdinPersson

import pandas as pd
import numpy as np
import nltk
from nltk.corpus import words

# Reading in the data
path = "emails.csv"
data = pd.read_csv(path)

# Get a set of words in the engilish language
nltk.download('words')
words = set(words.words())

# Calculate Probability of Spam and Proabability of Ham
spamCount = 0
hamCount = 0
totalCount = data.shape[0]

for i in range(totalCount):
    if data.iloc[i, 1] == 1:
        spamCount += 1
    else:
        hamCount += 1

probSpam = spamCount / totalCount
probHam = hamCount / totalCount

# Calculate the probability a word is Spam or Ham
wordDictionary = {}

for i in range(data.shape[0]):
    email = data.iloc[i, 0].split()
    for word in email:
        word = word.lower()
        if word in words:
            if word in wordDictionary:
                if data.iloc[i, 1] == 1:
                    # Spam Update
                    spamNum = wordDictionary[word][0]
                    hamNum = wordDictionary[word][2]
                    wordDictionary[word] = (
                        spamNum + 1, spamCount + 2, hamNum, hamCount + 2)
                else:
                    # Ham Update
                    spamNum = wordDictionary[word][0]
                    hamNum = wordDictionary[word][2]
                    wordDictionary[word] = (
                        spamNum, spamCount + 2, hamNum + 1, hamCount + 2)
            else:
                # Not in dictionary yet
                if data.iloc[i, 1] == 1:
                    wordDictionary[word] = (2, spamCount + 2, 1, hamCount+2)
                else:
                    wordDictionary[word] = (1, spamCount + 2, 2, hamCount + 2)

                    # Parses an email to calculate the % chance it is spam


def findSpam(email):

    num = 0.0
    denom = 0.0
    numProd = 1.0
    denomLProd = 1.0
    denomRProd = 1.0

    for word in email.split():
        word.lower()
        if(word in wordDictionary):
            numProd = numProd * \
                (wordDictionary[word][0] / wordDictionary[word][1])
            denomLProd = denomLProd * \
                (wordDictionary[word][0] / wordDictionary[word][1])
            denomRProd = denomRProd * \
                (wordDictionary[word][2] / wordDictionary[word][3])

    num = probSpam * numProd
    denom = (probSpam * denomLProd) + (probHam * denomRProd)

    if num / denom > 0.5:
        print("This message is spam", num / denom)
    else:
        print("This message is ham", num / denom)
