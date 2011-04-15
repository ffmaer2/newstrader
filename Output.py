# Query the Reuters database
from Plot import Plot
import pprint

#http://www.mindtwist.de/main/linux/3-linux-tipps/48-how-to-pretty-print-lists-in-python.html

class Output:
  def putOutput(self, ticker, metrics):
    print '\n---------- AND THE RESULTS ----------'
    print 'Sharpe ratio\t\t ==> ' + str(round(metrics[0], 2))
    print 'Number of trades\t ==> ' + str(metrics[1][0])
    print 'Percentage in\t\t ==> ' + str(round(metrics[1][1]*100, 2)) + '%'
    print 'Wins, losses\t\t ==> ' + str(metrics[2])
    print 'Average win, loss\t ==> ' + str(metrics[3])
    print 'Expectancy\t\t ==> ' + str(round(metrics[4], 2))
    print '\n-------------------------------------'


    print 'Plotting results..'
    we = Plot()
    we.plotThisFucker()
