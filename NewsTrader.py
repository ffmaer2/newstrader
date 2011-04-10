# VIVEK PATEL
# TRADING STRATEGIES AND SYSTEMS, SPRING 2011
# PROFESSOR DHAR

""" 
Main class.
Here we control everything:
1. We first create a query object, and query the database, returning a tuple with dates altered to compare with yahoo's stock dates.
2. Go through each line of the query, each article, and check the positive, negative, and uncertain words. Then calculate the sentiment.
3. Create a query object, and get the historical prices - start and last day is the date of the first and last article, respectively.
4. Merge reuterVector and yahooVector to make a mergeObj, with which you can start running tests on.
5. Run the strategy - get lagged correlations, get a 10 day MA of those lagged correlations to get a more accurate feeling of sentiment.
    Get signals from day10MA, take a position.
    Realize the returns the day after.
    Run strategy metrics.
6. Print output of results.
  Plot results.
  
"""

from ReutersQuery import ReutersQuery
from Sentiment import Sentiment
from YahooQuery import YahooQuery
from Merge import Merge
from Strategy import Strategy
from Output import Output

def main():
  ticker = raw_input("Welcome. Ready to trade? Pick a stock ticker: ")
  reuterObj = ReutersQuery()
  reuterVector = reuterObj.getQuery(ticker)
  
  sentimentObj = Sentiment()
  sentiment = sentimentObj.sentimentVectorize()

  yahooObj = YahooQuery()
  yahooVector = yahooObj.doYahooQuery()

  mergeObj = Merge()
  finaldata = mergeObj.mergeSentimentsAndPrices()

  strategyObj = Strategy()
  strategyObj.runStrategy(ticker)

  outputObj = Output()
  outputObj.getQuery(ticker)




if __name__ == "__main__":
  main()

  
  
  

  

  