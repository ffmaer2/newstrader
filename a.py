import matplotlib.pyplot as plt
import ystockquote

# Get Quotes 01/01/2006 - 01/01/2009
GOOG = ystockquote.get_historical_prices('GOOG', '20060101', '20090101')

# Create empty lists, quick and dirty
GOOGOpen = [ ]
GOOGClose = [ ]
GOOGDate = [ ]
GOOGHigh = [ ]
GOOGLow = [ ]
GOOGAdj = [ ]
GOOGVolume = [ ]

# Populate lists from downloaded data
for i in range(1, 755):
	GOOGDate.append(GOOG[i][0])
	GOOGOpen.append(GOOG[i][1])
	GOOGHigh.append(GOOG[i][2])
	GOOGLow.append(GOOG[i][3])
	GOOGClose.append(GOOG[i][4])
	GOOGVolume.append(GOOG[i][5])
 	GOOGAdj.append(GOOG[i][6])

plt.plot(GOOGClose)
plt.title("Google Adjusted Close")
plt.ylabel(r"GOOG Closing Price ($USD)", fontsize = 12)
plt.xlabel(r"Days", fontsize = 12)
plt.grid(True)
plt.show()