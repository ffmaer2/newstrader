###################################################################################################
# Merge reuterVector and yahooVector to make a mergeObj, with which you can start running tests on.
###################################################################################################

from collections import *
from OrderedDict import OrderedDict

# We're getting the sentiments matched up with the dates of the articles they correspond to.
def mergeDatesAndAverageSentiment(sentiments, dates):
  count = 1
  index = 0
  totalcount = 0
  
  # dict of sentiments
  d = defaultdict(float)
  # dict of counts
  e = defaultdict(float)

  # Fixed
  for date in dates:
    if date not in d and len(d) == 0:
      count = 1
    elif date in d:
      count += 1
      if index == len(dates)-1:
	totalcount += count
    else:
      totalcount += count
      count = 1
    e[date] = count
    d[date] += sentiments[index]
    #print date, d[date], sentiments[index]
    index += 1
  
  return dict( (n, d.get(n, 0) / e.get(n, 0)) for n in set(d)|set(e) )


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
  e = OrderedDict(sorted(merged.items()))
  return e
  

class Merge:
  def mergeEverything(self, sentiments, yahooVector, dates):
    print 'Merging sentiment and price vectors..'
    datesSentimentsR = mergeDatesAndAverageSentiment(sentiments, dates)
    pricesR = getPricesReady(yahooVector) # We're all good here
    merged = mergeDatesSentimentsAndPrices(datesSentimentsR, pricesR)
    #print len(merged)
    return sort(merged)