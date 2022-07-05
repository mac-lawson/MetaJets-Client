import os
from time import time
from urllib import response
import requests

def ping(ip):
    os.system('ping ' + (ip) + ' -t 5')

def curl(url):
    os.system('curl ' + (url))    

def get(www):
    response = requests.get(www)
    print(response)