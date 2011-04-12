# Change all dates in tuple object from YYYY-MM-DD 00:00:00:000 to YYYY-MM-DD
# Return updated tuple of columns, article

class DateFormat:  
	def fixDates(self, reuterVector):
		print 'Fixing reuter dates..'
		index = 0
		newReuterVector = []
		for result in reuterVector:
			reuterDate = str(reuterVector[index][0])
			reuterFixedDate = reuterDate[0:10]
			toAdd = reuterFixedDate, reuterVector[0][1][0:len(reuterVector[0][1])]
			newReuterVector.append(toAdd)
			index += 1
		return newReuterVector
