# Query the Reuters database

from scipy.stats.stats import pearsonr
from numpy import *
from OrderedDict import OrderedDict

def correlateLagged(s, p, da):
  d = {}
  i = 0
  print '\tDay lags\tCorrelation\tTwo-tailed p-value'

  # Actually very useful - there should be an option to take the highest, most significant correlation.
  for dayLag in range(int(len(s)/4)):
    d[da[i]] = pearsonr(s[0:len(s)-dayLag], p[dayLag:len(s)])
    print '\t' + str(i) + '\t\t' + str(round(d[da[i]][0], 6)) + '\t\t' + str(round(d[da[i]][1], 6))
    i += 1


# Counter-trend
# Moving average

def strat(s, p, da):
  wma = OrderedDict()
  i = 0
  #lag = int(raw_input('Enter the amount of lag you want in days, son: '))
  filler = 0
  
  for date in da:
    if i == 0:
      wma[date] = s[i], p[i], 0, 0
    elif i == 1:
      wma[date] = s[i], p[i], returns(p, i), 0
      # Weighted average attached at the end, there.
    else:
      wma[date] = s[i], p[i], returns(p, i), (s[i]*1 + s[i-1]*0.50 + s[i-2]*0.25 + s[i-3]*.125)/1.875
    i += 1
  return wma
    

def returns(p, i):
  if i == 0:
    return 0
  else:
    return (p[i] - p[i-1]) / p[i-1]


class Analytics:
  def getAnalytics(self, ticker, merged):
    print '-> ' + __name__
    newdata = [(a, b) for a, b in merged.iteritems()]
    
    da = merged.keys()
    p = []
    s = []
    r = []
    
    i = 0
    while i < len(newdata):
      s.append(newdata[i][1][0])
      p.append(newdata[i][1][1])
      # Initialize with empty, then do returns later
      r.append(0)
      i += 1
      
    correlateLagged(s, p, da)
    added = strat(s, p, da)
    return added
    
    
    