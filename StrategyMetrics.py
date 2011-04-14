# Query the Reuters database
from numpy import *

class StrategyMetrics:
  def getStrategyMetrics(self, ticker, strategyResults):
    print '-> ' + __name__
    
    sharpe = average(strategyResults) * sqrt(260) / std(strategyResults)
    print 'Sharpe ratio: ' + str(round(sharpe, 2))
    
    countIn = 0
    for result in strategyResults:
      if result == 0.0 or result == -0.0:
	countIn += 1
    percentageIn = float(countIn)/float(len(strategyResults)) * 100
    print 'Percentage in: ' + str(round(percentageIn, 2)) + '%'