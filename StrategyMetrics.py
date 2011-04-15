# Query the Reuters database
from numpy import *

def getSharpe(strategyResults):
  sharpe = average(strategyResults) * sqrt(260) / std(strategyResults)
  #print 'Sharpe ratio: ' + str(round(sharpe, 2))
  return sharpe
  
def getPercentageIn(strategyResults):
  countIn = 0
  for result in strategyResults:
    if result != 0:
      countIn += 1
  percentageIn = float(countIn)/float(len(strategyResults)) 
  #print 'Percentage in: ' + str(round(percentageIn, 2)) + '%'
  return countIn, percentageIn

def getWinLoss(strategyResults):
  win = 0
  loss = 0
  for result in strategyResults:
    if result > 0:
      win += 1
    elif result < 0:
      loss += 1
  return win, loss

def getAveWinLoss(strategyResults):
  win = 0
  winResults = 0
  loss = 0
  lossResults = 0
  for result in strategyResults:
    if result > 0:
      win += 1
      winResults += result
    elif result < 0:
      loss += 1
      lossResults += result
  
  # In the weird chance you didn't win any.
  if win != 0:
    aveWin = float(winResults)/float(win)
  
  # In the weird chance you didn't lose any.
  if loss != 0:
    aveLoss = float(lossResults)/float(loss)
  return aveWin, aveLoss

def getExpectancy(winLoss, aveWinLoss):
  expectancy = (aveWinLoss[0]*winLoss[0]/(winLoss[0] + winLoss[1]) - aveWinLoss[1]*winLoss[1]/(winLoss[0] + winLoss[1]))
  print expectancy
  return expectancy

# FIX. THIS IS FUCKED UP.
def getMaxDrawdown(strategyResults):
  resultsCount = 0
  maxDrawdowns = []
  
  for result in strategyResults:
    if result < 0:
      resultsCount += result
    else:
      maxDrawdowns.append(resultsCount)
      resultsCount = 0
  return min(maxDrawdowns)

class StrategyMetrics:
  def getStrategyMetrics(self, ticker, strategyResults):
    print '-> ' + __name__
    
    sharpe = getSharpe(strategyResults)
    countPercentageIn = getPercentageIn(strategyResults) # tuple
    winLoss = getWinLoss(strategyResults) # tuple
    aveWinLoss = getAveWinLoss(strategyResults) # tuple
    expectancy = getExpectancy(winLoss, aveWinLoss)
    maxDrawdown = getMaxDrawdown(strategyResults)
    
    metrics = [sharpe, countPercentageIn, winLoss, aveWinLoss, expectancy, maxDrawdown]
    return metrics