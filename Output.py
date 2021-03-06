# Output the results of the strategy! 
from Plot import Plot

#http://www.mindtwist.de/main/linux/3-linux-tipps/48-how-to-pretty-print-lists-in-python.html

class Output:
  def putOutput(self, ticker, metrics, yahooVector, merged):
    print '\n---------- '+ticker+' THE RESULTS ----------'
    print 'Sharpe ratio\t\t ==> ' + str(round(metrics[0], 2))
    print 'Company Sharpe ratio\t ==> ' + str(round(metrics[8], 2))
    print 'Number of trades\t ==> ' + str(metrics[1][0])
    print 'Total days\t\t ==> ' + str(len(metrics[6]))
    print 'Percentage in\t\t ==> ' + str(round(metrics[1][1]*100, 2)) + '%'
    print 'Wins, losses\t\t ==> ' + str(metrics[2])
    print 'Average win, loss\t ==> ' + str(metrics[3])
    print 'Expectancy\t\t ==> ' + str(round(metrics[4], 4))
    print '---------------------------------------\n'
    
    print 'Plotting results..'
    we = Plot()
    # We want to plot equity, stock performance, and sentiment.
    we.plotThis(ticker, merged, metrics[6], metrics[7])
