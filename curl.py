import datetime
import os
import subprocess
import time
from statistics import mean

def action():
   try:
      results = subprocess.run(
      ["curl", "https://yahoo.com", "-o", "/dev/null", "-w", "%{time_namelookup}"], 
      capture_output=True, text=True)
    
      return results.stdout
      
   except Exception as e:
      print("an exception was encountered: " + format(e))

def main():

   # Use an environmental variable to set the pause b/w executions.
   # If the variable is undefined, use 3 seconds.
   try:
      sleep_time = int(os.environ["DELAY"])
   except KeyError:
      sleep_time = 3

   # Define results as a list
   results = []

   for i in range(0,100):
      results.append(float(action()))
      time.sleep(sleep_time)

   #print(results)
   print("Delay between executions is {} seconds.".format(sleep_time))
   print("Executed query {} times.".format(len(results)))
   print("Minimum exection time is: {}. Maximum time is: {}".format(min(results), max(results)))
   print("Mean time is: {}".format(mean(results)))
      
if __name__ == '__main__':
    main()

