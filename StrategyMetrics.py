# Query the Reuters database
from numpy import *

def getSharpe(strategyResults):
  sharpe = average(strategyResults) * sqrt(260) / std(strategyResults)
  return sharpe
  
def getPercentageIn(strategyResults):
  countIn = 0
  for result in strategyResults:
    if result != 0:
      countIn += 1
  percentageIn = float(countIn)/float(len(strategyResults)) 
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
  return expectancy

# FIX. THIS IS MESSED UP.
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

def companySharpe(s_p_r_ma_pos):
  newdata = [(a, b) for a, b in s_p_r_ma_pos.iteritems()]
  r = []
  i = 0
  while i < len(newdata):
    r.append(newdata[i][1][2])
    i += 1
    
  print average(r)
  print std(r)
  cSharpe = average(r) * sqrt(260) / std(r)
  return cSharpe
    

class StrategyMetrics:
  def getStrategyMetrics(self, ticker, strategyResults, s_p_r_ma_pos):
    print '-> ' + __name__
    
    sharpe = getSharpe(strategyResults)
    countPercentageIn = getPercentageIn(strategyResults) # tuple
    winLoss = getWinLoss(strategyResults) # tuple
    aveWinLoss = getAveWinLoss(strategyResults) # tuple
    expectancy = getExpectancy(winLoss, aveWinLoss)
    maxDrawdown = getMaxDrawdown(strategyResults)
    cSharpe = companySharpe(s_p_r_ma_pos)
    
    metrics = [sharpe, countPercentageIn, winLoss, aveWinLoss, expectancy, maxDrawdown, strategyResults, s_p_r_ma_pos, cSharpe]
    return metrics