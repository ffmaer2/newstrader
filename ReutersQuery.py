# Query the Reuters database
import pymssql

class ReutersQuery:  
  def getQuery(self, ticker):
    #num = raw_input("How many articles do you want to get? Keep it between 10 and 200: ")

    print 'Querying..'
    
    # It would be nice to let the user enter in how many stories to query.
    queryText = """select top 100 story_date_time, cast(take_text as text) from Reuters.dbo.news where related_rics like '%""" + ticker + """%' and language = 'en' and event_type = 'STORY_TAKE_OVERWRITE'"""
    
    conn = pymssql.connect(host='vpanos.stern.nyu.edu:1433', user='devel', password='developer', database='Reuters')
    cursor = conn.cursor()
    cursor.execute(queryText)
    results = cursor.fetchall()
    print 'Query done!'

    return list(results)
