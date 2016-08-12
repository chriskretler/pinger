import requests
import time
from datetime import datetime

MIME_TYPE_JSON = 'application/json'
CONTENT_TYPE = 'Content-type'

def api_handler():

   response = None

   try:
      begin = datetime.now()
      headers = {CONTENT_TYPE: MIME_TYPE_JSON}

      response = requests.get("https://www.google.com/logos/doodles/2016/2016-doodle-fruit-games-day-8-5666133911797760.3-hp.gif", headers=headers)
                
      end = datetime.now()
      diff = end - begin
      print "GET api execution time: " + str(diff)             
                
   except (requests.exceptions.RequestException, Exception) as exception:
      raise exception

   return response

for i in range(1, 100):
   print i
   api_handler()
   time.sleep(1)


