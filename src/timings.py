from datetime import datetime
import logging
import os
import requests
import time

def fetch_time(site):
    try:
        r = requests.get(site) #, verify='incommon.pem')
        results = r.elapsed.total_seconds()
    except Exception as e:
        logging.error("an exception was encountered: " + format(e))
    else:
        logging.info("{},{},{}".format(datetime.now().strftime("%H:%M"),site,results))

def main():

    logging.basicConfig()
    logging.getLogger().setLevel(level='INFO')
    # What sites to query? Default to none
    site = []

    try:
       sites = os.environ["SITES"].split(",")
    except KeyError:
       logging.error("no sites g")
       return 1

    logging.info("sites are {}".format(sites))

    while len(sites) > 0:
       for site in sites:
           fetch_time(site)
       time.sleep(30)


if __name__ == '__main__':
    main()
