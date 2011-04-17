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


def getSentiment(reuterVector, stemmedNegTokens, stemmedPosTokens):
  count = 0
  sentiment = []

  for article in reuterVector:	
    sentsum = 0
    negcount = 1
    poscount = 1

    # word count
    wordsInArticle = nltk.word_tokenize(article[1]) # list
    wordcount = len(wordsInArticle)

    stemmedTokens = []
    stemmer = PorterStemmer()

    for word in wordsInArticle:
      stemmedWord = stemmer.stem(word)
      stemmedTokens.append(stemmedWord.lower())
    
    for negStemmed in stemmedNegTokens:
      if negStemmed in stemmedTokens:
	negcount += 1
    for posStemmed in stemmedPosTokens:
      if posStemmed in stemmedTokens:
	poscount += 1
	
    print poscount, negcount
    # sentiment - 0% is neutral
    sentraw = (float(poscount) - float(negcount)) / float(wordcount + 1)
    sentiment.append(sentraw)
    count += 1
    
    print '#' + str(count)
    
  normalized = []
  sentstd = numpy.std(sentiment)
  sentave = numpy.average(sentiment)
  for sent in sentiment:
    normalized.append((float(sent) - float(sentave))/(float(sentstd)))
  
  return normalized


class Sentiment:  
  def sentimentVectorize(self, reuterVector):
    print 'Generating sentiment for article:'
    posl = getPosWords()
    negl = getNegWords()
    sentiment = getSentiment(reuterVector, negl, posl)
    return sentiment
