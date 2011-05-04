# Query the Reuters database
import pymssql
from datetime import datetime, timedelta
import time
from time import mktime

class ReutersQuery:  
  def getQuery(self, ticker):
    print 'Querying..\n'
    conn = pymssql.connect(host='vpanos.stern.nyu.edu:1433', user='devel', password='developer', database='Reuters')
    cursor = conn.cursor()
    results = []

    print 'Enter start and end date, both in the format of YYYY-MM-DD'
    start = raw_input('start: ')
    end = raw_input('end: ')

    startStrip = time.strptime(start[:10], "%Y-%m-%d")
    endStrip = time.strptime(end[:10], "%Y-%m-%d")
    startObj = datetime.fromtimestamp(mktime(startStrip))
    endObj = datetime.fromtimestamp(mktime(endStrip))

    startSeg = startObj

    while startSeg < endObj:
      startSegStr = str(startSeg)[:10]
      startSeg += timedelta(days=3)
      endSegStr = str(startSeg)[:10]

      queryText = """select story_date_time, cast(take_text as text) from Reuters.dbo.news where related_rics like '%""" + ticker + """%' and language = 'en' and event_type = 'STORY_TAKE_OVERWRITE' and story_date_time >= '""" + startSegStr + """' and story_date_time <= '""" + endSegStr + """'"""
      
      print 'FETCHING ARTICLES BETWEEN ' + startSegStr + ' AND ' + endSegStr

      cursor.execute(queryText)
      
      row = cursor.fetchone()
      while row:
        toAdd = (row[0], row[1])
        results.append(toAdd)
        row = cursor.fetchone()

    conn.close()

    print 'Query done!'
    return results