'''
This code generate 10 random numbers and uploads to thingspeak channel.
Replace 'XXXXXXXXXXXXXXXX' with your api key
'''

import sys
from time import sleep
import urllib3
import random

a = 0
baseURL = 'http://api.thingspeak.com/update?api_key=XXXXXXXXXXXXXXXX&field1='
http = urllib3.PoolManager()

while(a < 10):
    b = random.uniform(30, 100)
    print(b)
    r = http.request('GET', baseURL+str(b))
    sleep(10)
    a = a + 1
print("Program has ended")
