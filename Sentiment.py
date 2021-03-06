# Calculate sentiment based on positive, negative, and uncertain word counts
# THIS WILL RESULT IN DIFFERENT SENTIMENTS EVERYTIME - NOT MY FAULT. IT'S THE DATABASE'S :(
import re
import numpy
import nltk
from nltk import PorterStemmer


def getPosWords():
  stemmer = PorterStemmer()
  stemmedPosTokens = []
  pos = open(r'pos.txt').read()
  pos = re.sub("\d", "", pos)
  posWords = nltk.word_tokenize(pos)
  for posWord in posWords:
    stemmedPosWord = stemmer.stem(posWord)
    stemmedPosTokens.append(stemmedPosWord.lower())
  return stemmedPosTokens


def getNegWords():  
  stemmer = PorterStemmer()
  stemmedNegTokens = []

  neg = open(r'neg.txt').read()
  neg = re.sub("\d", "", neg)
  negWords = nltk.word_tokenize(neg)
  for negWord in negWords:
    stemmedNegWord = stemmer.stem(negWord)
    stemmedNegTokens.append(stemmedNegWord.lower())
  return stemmedNegTokens


def getUncertainWords():  
  stemmer = PorterStemmer()
  stemmedUnTokens = []

  un = open(r'uncertain.txt').read()
  un = re.sub("\d", "", un)
  unWords = nltk.word_tokenize(un)
  for unWord in unWords:
    stemmedUnWord = stemmer.stem(unWord)
    stemmedUnTokens.append(stemmedUnWord.lower())
  return stemmedUnTokens


def getSentiment(reuterVector, stemmedNegTokens, stemmedPosTokens, stemmedUnTokens):
  count = 0
  sentiment = []
  normalized = []

  for article in reuterVector:	
    sentSum = 0
    negCount = 1
    posCount = 1
    unCount = 1
    sentStd = 1
    sentAve = 0

    # word count
    wordsInArticle = nltk.word_tokenize(article[1]) # list
    wordCount = len(wordsInArticle)

    stemmedTokens = []
    stemmer = PorterStemmer()

    for word in wordsInArticle:
      stemmedWord = stemmer.stem(word)
      stemmedTokens.append(stemmedWord.lower())
    
    for negStemmed in stemmedNegTokens:
      if negStemmed in stemmedTokens:
	negCount += 1
    for posStemmed in stemmedPosTokens:
      if posStemmed in stemmedTokens:
	posCount += 1
    for unStemmed in stemmedUnTokens:
      if unStemmed in stemmedTokens:
	unCount += 1	
	
	
    # sentiment - 0% is neutral
    #sentraw = (float(poscount) - float(negcount)) / float(wordcount + 1)
    if count < 5:
      sentRaw = (float(posCount)-float(negCount))*(float(unCount)/float(wordCount+1))/float(posCount)
      sentiment.append(sentRaw)
    else:
      sentRaw = (posCount - negCount) / ((wordCount+1) * unCount)
      sentiment.append(sentRaw)
      
    count += 1
    
    # Progress
    print str(round(float(count) * 100 / float(len(reuterVector)), 2)) + "%"
    
    if count < 10:
      sentStd = 1.0
      sentAve = 0.0
    else:
      sentStd = numpy.std(sentiment[count-10:count])
      sentAve = numpy.average(sentiment[count-10:count])
    
    if sentStd != 0:
      normalized.append((float(sentRaw) - float(sentAve))/(float(sentStd)))
    else:
      normalized.append((float(sentRaw) - float(sentAve))/(1.0))
  return normalized


class Sentiment:  
  def sentimentVectorize(self, reuterVector):
    print 'Generating sentiment for article:'
    posT = getPosWords()
    negT = getNegWords()
    unT = getUncertainWords()
    sentiment = getSentiment(reuterVector, negT, posT, unT)
    return sentiment
