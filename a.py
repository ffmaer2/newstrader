from urllib import urlopen
import nltk
from nltk import PorterStemmer
import re

url = "http://www.gutenberg.org/files/2554/2554.txt"
raw = urlopen(url).read()
tokens = nltk.word_tokenize(raw)
print tokens

stemmedTokens = []

stemmer = PorterStemmer()
for word in tokens:
  stemmedWord = stemmer.stem(word)
  stemmedTokens.append(stemmedWord.lower())
  
  

stemmedNegTokens = []

neg = open(r'neg.txt').read()
neg = re.sub("\d", "", neg)
negcount = 0
negWords = nltk.word_tokenize(neg)
for negWord in negWords:
  stemmedNegWord = stemmer.stem(negWord)
  stemmedNegTokens.append(stemmedNegWord.lower())

print stemmedNegTokens


for stemmed in stemmedNegTokens:
  if stemmed in stemmedTokens:
    negcount += 1

print negcount