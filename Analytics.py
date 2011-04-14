# Query the Reuters database

from scipy.stats.stats import pearsonr
from numpy import *
from OrderedDict import OrderedDict
from Returns import Returns
#NEED TO MAKE ^

def correlateLagged(s, p, da):
  d = {}
  i = 0

  # pearsonr(s[0:len(s)-dayLag], p[dayLag:len(s)])[0], can remove [0] to get p val
  for dayLag in range(int(len(s)*2/3)):
    d[da[i]] = pearsonr(s[0:len(s)-dayLag], p[dayLag:len(s)])[0]
    print da[i], s[i], d[da[i]]
    i += 1
  return d


def day3MaAndReturns(s, p, da):
  wma = OrderedDict()
  i = 0
  
  for date in da:
    if i == 0:
      wma[date] = s[i], p[i], 0, 0
    elif i == 1:
      wma[date] = s[i], p[i], returns(p, i), 0
    else:
      # Weighted average attached at the end, there.
      wma[date] = s[i], p[i], returns(p, i), (s[i]*1 + s[i-1]*0.75 + s[i-2]*0.25)/2
    print date, wma[date]
    i += 1
  return wma
    

def returns(p, i):
  if i == 0:
    return 0
  else:
    return (p[i] - p[i-1]) / p[i-1]
  

class Analytics:
  def getAnalytics(self, ticker, finaldata):
    print '-> ' + __name__
    newdata = [(a, b) for a, b in finaldata.iteritems()]
    
    da = finaldata.keys()
    s = []
    p = []
    r = []
    
    i = 0
    while i < len(newdata):
      s.append(newdata[i][1][0])
      p.append(newdata[i][1][1])
      # Initialize with empty, then do returns later
      r.append(0)
      i += 1
      
    added = day3MaAndReturns(s, p, da)
    #lagged = correlateLagged(s, p, da)
    return added
    