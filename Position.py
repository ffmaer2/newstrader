# Calculates position
class Position:
  def getPosition(self, ticker, correlations):
    print '-> ' + __name__
    
    positions = []
    for value in correlations:
      if correlations[value] > .1:
	positions.append(1)
      elif correlations[value] < -.2:
	positions.append(-1)
      else:
	positions.append(0)

    print positions