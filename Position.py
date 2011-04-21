# Calculates position
from OrderedDict import OrderedDict

class Position:
  def getPosition(self, ticker, s_p_r_ma):
    print '-> ' + __name__
    newdata = [(a, b) for a, b in s_p_r_ma.iteritems()]
    
    s_p_r_ma_pos = OrderedDict()
    s = []
    p = []
    ma = []
    r = []
    pos = []
    
    i = 0
    for date in s_p_r_ma:
      s.append(newdata[i][1][0])
      p.append(newdata[i][1][1])
      r.append(newdata[i][1][2])
      ma.append(newdata[i][1][3])
      if ma[i] > 0.1:
	pos.append(-1)
      elif ma[i] < -0.1:
	pos.append(1)
      else:
	pos.append(0)
      s_p_r_ma_pos[date] = s[i], p[i], r[i], ma[i], pos[i]
      #print s_p_r_ma_pos[date]
      i += 1
    
    return s_p_r_ma_pos