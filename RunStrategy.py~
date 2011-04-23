# Run strategy

def getPerformance(r, pos): 
  perf = []
  
  i = 0
  while i < len(r) and i < len(pos):
    if i == 0:
      toAdd = float(0)
      perf.append(toAdd)
    else:
      perf.append(r[i]*pos[i-1])
    i += 1
    
  
  return perf



class RunStrategy:
  def getResults(self, ticker, s_p_r_ma_pos):
    print '-> ' + __name__
    
    newdata = [(a, b) for a, b in s_p_r_ma_pos.iteritems()]
    
    r = []
    pos = []
    
    i = 0
    for date in s_p_r_ma_pos:
      r.append(float(newdata[i][1][2]))
      pos.append(float(newdata[i][1][4]))
      i += 1
    
    return getPerformance(r, pos)
    