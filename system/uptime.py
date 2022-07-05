import os
from time import time

def ping(ip):
    os.system('ping ' + (ip) + ' -t 5')

def curl(url):
    os.system('curl ' + (url))    