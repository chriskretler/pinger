import requests
import time
from datetime import datetime

MIME_TYPE_JSON = 'application/json'
CONTENT_TYPE = 'Content-type'

def api_handler(i):

   response = None

   try:
      begin = datetime.now()
      headers = {CONTENT_TYPE: MIME_TYPE_JSON}

      response = requests.get("https://www.google.com/logos/doodles/2016/2016-doodle-fruit-games-day-8-5666133911797760.3-hp.gif", headers=headers)
                
      end = datetime.now()
      diff = end - begin
      print str(i) + " execution time: " + str(diff)             
                
   except (requests.exceptions.RequestException, Exception) as exception:
      raise exception

   return response


print 'started at: ' + str(datetime.now())

for i in range(1, 100):
   api_handler(i)
   time.sleep(1)

print 'ended at: ' + str(datetime.now())