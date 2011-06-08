# Calculates position
from OrderedDict import OrderedDict
import numpy

class Position:
  def getPosition(self, ticker, s_p_r_ma):
    print '-> ' + __name__
    newdata = [(a, b) for a, b in s_p_r_ma.iteritems()]
    
    s_p_r_ma_pos = OrderedDict()
    s = []
    p = [] 
    ma = []
    r = []
    pos = []#tc tc!
    
    i = 0
    for date in s_p_r_ma:
      s.append(newdata[i][1][0])
      p.append(newdata[i][1][1])
      r.append(newdata[i][1][2])
      ma.append(newdata[i][1][3])
      if i < 5:
	pos.append(0)
      else:
	change = ((ma[i]+1)-(ma[i-1]+1))/(ma[i-1]+1)
	thresh = numpy.std(ma[i-5:i])/(abs(numpy.average(ma[i-5:i]))+0.5)
	# Counter-trend. The threshold needs to change based on new data. std? WORKS
	# Dampening... ALSO NEEDS TO CHANGE.. AHH.
	# For WMT, /5, /2 works
	# For XOM, that's too sensitive
	#if change < numpy.std(ma)/5 and change > 0:
	  #pos.append(1)
	#elif change > -numpy.std(ma)/2 and change < 0:
	  #pos.append(-1)
	if change > thresh:
	  pos.append(-1)
	elif change < -thresh:
	  pos.append(1)
	else:
	  pos.append(0)
      s_p_r_ma_pos[date] = s[i], p[i], r[i], ma[i], pos[i]
      i += 1
    
    return s_p_r_ma_pos