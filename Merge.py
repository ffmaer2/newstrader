###################################################################################################
# Merge reuterVector and yahooVector to make a mergeObj, with which you can start running tests on.
###################################################################################################

from collections import *







# We're getting the sentiments matched up with the dates of the articles they correspond to.
def mergeDatesAndAverageSentiment(sentiments, dates):
  count = 1
  index = 0
  
  d = defaultdict(float)
  e = defaultdict(float)

  for date in dates:
    sentsum = sentiments[index]
    if date in d:
      count += 1
    else:
      count = 1
    e[date] = count
    d[date] += sentsum
    index += 1
  
  return dict( [ (n, d.get(n, 0) / e.get(n, 0)) for n in set(d)|set(e) ] )


def getPricesReady(yahooVector):
  n = defaultdict(float)
  for v, k in yahooVector:
    n[v] = float(k)
  return n


def mergeDatesSentimentsAndPrices(datesSentimentsR, pricesR):
  # Merge ONLY if keys are identical
  a = defaultdict(float)
  for key in datesSentimentsR:
    if key in pricesR.keys():
      a[key] = datesSentimentsR[key], pricesR[key]
  return a
  

def sort(merged):
  d = (sorted(merged.items()))
  return dict(sorted(merged.items()))
  

class Merge:
  def mergeEverything(self, sentiments, yahooVector, dates):
    print 'Merging sentiment and price vectors..'
    datesSentimentsR = mergeDatesAndAverageSentiment(sentiments, dates)
    pricesR = getPricesReady(yahooVector)
    merged = mergeDatesSentimentsAndPrices(datesSentimentsR, pricesR)
    return sort(merged)