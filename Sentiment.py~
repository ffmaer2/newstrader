# Calculate sentiment based on positive, negative, and uncertain word counts
# Remember: stem the words
# THIS WILL RESULT IN DIFFERENT SENTIMENTS EVERYTIME - NOT MY FAULT. IT'S THE DATABASE'S :(
import re

def getPosWords():
  pos = open(r'pos.txt').read()
  pattern = re.compile('\s\d*\s')
  posWords = re.split(pattern, pos)
  lowPosWords = []
  for posWord in posWords:
    posWord = posWord.lower()
    lowPosWords.append(posWord)
  return lowPosWords

def getNegWords():
  neg = open(r'neg.txt').read()
  pattern = re.compile('\s\d*\s')
  negWords = re.split(pattern, neg)
  lowNegWords = []
  for negWord in negWords:
    negWord = negWord.lower()
    lowNegWords.append(negWord)
  return lowNegWords

def getSentiment(reuterVector, lowNegWords, lowPosWords):
  count = 0
  sentiment = []

  for article in reuterVector:	
    sentsum = 0
    negcount = 1
    poscount = 1

    # word count
    wordsinarticle = article[1].split()
    wordcount = len(wordsinarticle)

    # count frequencies
    for negword in lowNegWords:
      if re.search(re.compile(negword), article[1]) != None:
	negcount += 1
    for posword in lowPosWords:
      if re.search(re.compile(posword), article[1]) != None:
	poscount += 1    

    # sentiment - 0% is neutral
    sentraw = (float(poscount) - float(negcount)) / (poscount)
    sentiment.append(sentraw)
    count += 1
    print '#' + str(count)
    
  print sentiment
  return sentiment


class Sentiment:  
  def sentimentVectorize(self, reuterVector):
    print 'Vectorizing sentiment..'
    print 'Generating sentiment for article:'
    posl = getPosWords()
    negl = getNegWords()
    sentiment = getSentiment(reuterVector, negl, posl)
    return sentiment
