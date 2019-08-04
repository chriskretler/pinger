import time
import subprocess
import datetime

def dns_lookup():
   try:
      results = subprocess.run(
      ["dig", "dig-mysql.miserver.it.umich.edu", 
      capture_output=True, text=True])
      
      if '141.211.7.100' not in results.stdout:
         print(datetime.datetime.now())
         print(results.stdout.splitlines())
         print('\n')    

   except Exception as e:
      print("an exception was encountered: " + format(e))

while(True):
   dns_lookup()
   time.sleep(3)
