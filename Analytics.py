# Query the Reuters database

from scipy.stats.stats import pearsonr
from numpy import *
from OrderedDict import OrderedDict


def correlateLagged(s, r, da):
  d = {}
  i = 0

  # ISSUE HERE? GETS SEEMINGLY RANDOM RESULTS?! Potential at merge though.
  # pearsonr(s[0:len(s)-dayLag], p[dayLag:len(s)])[0], can remove [0] to get p val
  for dayLag in range(int(len(s)*2/3)):
    d[da[i]] = pearsonr(s[0:len(s)-dayLag], r[dayLag:len(s)])[0]
    print da[i], d[da[i]]
    i += 1
    
  return d



class Analytics:
  def getAnalytics(self, ticker, finaldata):
    print '-> ' + __name__
    newdata = [(v, k) for v, k in finaldata.iteritems()]
    
    da = finaldata.keys()
    s = []
    r = []
    
    i = 0
    while i < len(newdata):
      s.append(newdata[i][1][0])
      r.append(newdata[i][1][1])
      i += 1
      
    lagged = correlateLagged(s, r, da)
    return lagged
    