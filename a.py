import re
neg = open(r'neg.txt').read()
pattern = re.compile('\s\d*\s')
negWords = re.split(pattern, neg)
lowNegWords = []
for negWord in negWords:
  negWord = negWord.lower()
  lowNegWords.append(negWord)
  
file = open("negwords.txt", 'w')
for item in lowNegWords:
  file.write("%s " % item)
file.close