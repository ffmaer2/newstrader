# Run the freakin' strategy! Whoo!
from Analytics import Analytics
from Position import Position
from RunStrategy import RunStrategy
from StrategyMetrics import StrategyMetrics
import time

class Strategy:
  def runStrategy(self, ticker, merged):
    print '\nRunning strategy on ' + ticker + '..'  
    time.sleep(2)

    
    # First, do analytics to figure out how to execute the strategy.
    # Return lagged correlations and (10dayMA) of those lagged correlations.
    analyticsObj = Analytics()
    s_p_r_ma = analyticsObj.getAnalytics(ticker, merged)
    
    # Second, determine the position.
    positionObj = Position()
    s_p_r_ma_pos = positionObj.getPosition(ticker, s_p_r_ma)
    
    # Third, run the strategy!
    # Return a performance list (with dates?)
    strategyObj = RunStrategy()
    strategyResults = strategyObj.getResults(ticker, s_p_r_ma_pos)
    
    # Fourth, determine the metrics.
    metricsObj = StrategyMetrics()
    metrics = metricsObj.getStrategyMetrics(ticker, strategyResults, s_p_r_ma_pos)
    return metrics