# Query the Reuters database
import pymssql

from datetime import datetime, timedelta
import time
from time import mktime

#num = raw_input("How many articles do you want to get? Keep it between 10 and 200: ")

print 'Querying..'
ticker = 'WMT'
results = []

print 'Enter start and end date, both in the format of YYYY-MM-DD'
#start = raw_input('start: ')
#end = raw_input('end: ')

start = '2005-01-01'
end = '2005-02-01'

print timedelta(days=5)

startStrip = time.strptime(start[:10], "%Y-%m-%d")
endStrip = time.strptime(end[:10], "%Y-%m-%d")
startObj = datetime.fromtimestamp(mktime(startStrip))
endObj = datetime.fromtimestamp(mktime(endStrip))
print endObj - startObj

#print datetime(*start[:6])

queryText = """select story_date_time, cast(take_text as text) from Reuters.dbo.news where related_rics like '%""" + ticker + """%' and language = 'en' and event_type = 'STORY_TAKE_OVERWRITE' and story_date_time >= '""" + start + """' and story_date_time <= '""" + end + """'"""

conn = pymssql.connect(host='vpanos.stern.nyu.edu:1433', user='devel', password='developer', database='Reuters')
cursor = conn.cursor()
cursor.execute(queryText)

row = cursor.fetchone()
while row:
  toAdd = (row[0], row[1][0:10])
  print toAdd
  results.append(toAdd)
  row = cursor.fetchone()

print results
conn.close()

print 'Query done!'

