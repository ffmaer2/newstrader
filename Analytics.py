# Query the Reuters database

from scipy.stats.stats import pearsonr
from numpy import *

def correlateLagged(s, p, da):
  correlation = []
  d = {}
  i = 0
  
  # -2 could be refined. This means towards the end there are little datapoints for correlation.
  for dayLag in range(int(len(s)/2)):
    d[da[i]] = pearsonr(s[0:len(s)-dayLag], p[dayLag:len(s)])[0]
    correlation.append(pearsonr(s[0:len(s)-dayLag], p[dayLag:len(s)]))
    i += 1
  print d
  return correlation


class Analytics:
  def getAnalytics(self, ticker, finaldata):
    newdata = [(v, k) for v, k in finaldata.iteritems()]
    
    da = finaldata.keys()
    s = []
    p = []
    
    i = 0
    while i < len(newdata):
      s.append(newdata[i][1][0])
      p.append(newdata[i][1][1])
      
      i += 1
      
    correlateLagged(s, p, da)
    print '-> ' + __name__
    
    