from datetime import datetime
import os
import requests
import time
from statistics import mean

def fetch_time(site):
    try:
        r = requests.get(site) #, verify='incommon.pem')
        results = r.elapsed.total_seconds()
    except Exception as e:
        print("an exception was encountered: " + format(e))
    else:
        print("{},{},{}".format(datetime.now().strftime("%H:%M"),site,results))

def main():
   # What sites to query? Default to none
   site = []

   try:
       sites = os.environ["SITES"].split(",")
   except KeyError:
       print("no sites g")
       return 1

   print("sites are {}".format(sites))

   while len(sites) > 0:
       for site in sites:
           fetch_time(site)

       time.sleep(30)


if __name__ == '__main__':
    main()
