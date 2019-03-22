import traceback
import socket
import time
from subprocess import call

def api_handler():
   try:
      #socket.getaddrinfo("dig-mysql.miserver.it.umich.edu", 3306)
      call(["host", "dig-mysql.miserver.it.umich.edu"])
      
   except Exception as e:
      print "an exception was encountered" + traceback.format_exc()
      call(["host", "-v", "dig-mysql.miserver.it.umich.edu"])

while(True):
   api_handler()
   time.sleep(3)
