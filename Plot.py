# PLOT THE RESULTS!
import matplotlib.pyplot as plt

def getP(merged):
  newdata = [(a, b) for a, b in merged.iteritems()]
  p = []
  i = 0
  while i < len(newdata):
    p.append(newdata[i][1][1])
    i += 1
  return p


def equity(performance):
  start = 100
  e = []
  i = 0
  for a in performance:
    e.append(start)
    start += performance[i]*start
    i += 1
  return e


def sent(s_p_r_ma_pos):
  newdata = [(a, b) for a, b in s_p_r_ma_pos.iteritems()]
  ma = []
  i = 0
  while i < len(newdata):
    ma.append(newdata[i][1][3])
    i += 1
  return ma


class Plot:    
  def plotThis(self, ticker, merged, performance, s_p_r_ma_pos):
    p = getP(merged)
    e = equity(performance)
    ma = sent(s_p_r_ma_pos)

    
    fig = plt.figure()
    fig.suptitle('Equity, Closing Price, Sentiment vs. Days', fontsize=14)

    ax1 = fig.add_subplot(311)
    ax1.set_ylabel(r" Equity ($USD)", fontsize = 12)
    ax1.plot(e, 'g')
    ax1.grid(True)

    ax2 = fig.add_subplot(312)
    ax2.set_ylabel(ticker + r" Closing Price ($USD)", fontsize = 12)
    ax2.plot(p, 'r')
    ax2.grid(True)
 
    ax3 = fig.add_subplot(313)
    ax3.set_ylabel(r"Sentiment", fontsize = 12)
    ax3.set_xlabel(r"Days", fontsize = 12)
    ax3.plot(ma, 'b')
    ax3.grid(True)   
    
    plt.show()