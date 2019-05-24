import requests
import traceback
import time
from datetime import datetime
from subprocess import call

MIME_TYPE_JSON = 'application/json'
CONTENT_TYPE = 'Content-type'

def pinger():

   try:
      begin = datetime.now()
      #headers = {CONTENT_TYPE: MIME_TYPE_JSON}
      #response = requests.get("dig-mysql.miserver.it.umich.edu", headers=headers)

      end = datetime.now()
      diff = end - begin
      #print str(i) + " execution time: " + str(diff.total_seconds())
      #print "execution time: " + str(diff.total_seconds()) + "\n"

      #if diff.total_seconds() > 3:
      #  print "clock time: " + str(end)            
      #  print call(["host", "-v", "google.com"])
                
#   except (requests.exceptions.RequestException, Exception) as exception:
   except Exception as e:
      print("an exception was encountered" + traceback.format_exc())



#print 'started at: ' + str(datetime.now())

#for i in range(1, 100000):
while(True):
   pinger()
   time.sleep(3)

#print 'ended at: ' + str(datetime.now())
