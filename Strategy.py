# Run the freakin' strategy! Whoo!
from Analytics import Analytics
from Position import Position
from RunStrategy import RunStrategy
from StrategyMetrics import StrategyMetrics

class Strategy:
  def runStrategy(self, ticker, finaldata):
    print 'Running strategy on ' + ticker + '..'  
    
    # First, do analytics to figure out how to execute the strategy.
    # Return lagged correlations and 10dayMA of those lagged correlations.
    analyticsObj = Analytics()
    correlations = analyticsObj.getAnalytics(ticker, finaldata)
    
    # Second, determine the position.
    # Take 10dayMA and take a position.
    # Short thresh = ; long thresh = 
    positionObj = Position()
    positions = positionObj.getPosition(ticker)
    
    # Third, run the strategy!
    # Return a performance list (with dates?)
    strategyObj = RunStrategy()
    strategyResults = strategyObj.getResults(ticker)
    
    # Fourth, determine the metrics.
    metricsObj = StrategyMetrics()
    metrics = metricsObj.getStrategyMetrics(ticker)