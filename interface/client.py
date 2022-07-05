from turtle import color
from click import command
from clientStyle import logo
from clientStyle import coloring
from interface import run   
from system import uptime
from time import sleep
import sys


def mainMenu():
    while True:
        print((coloring.terminal.fail) + (logo.logo) + (coloring.terminal.end))
        menuOptions = input('Press Enter to Run')


        print((coloring.terminal.green) + 'pinging localhost... ' + (coloring.terminal.end))
        sleep(3)
        uptime.ping('127.0.0.1')
        print((coloring.terminal.green) + 'cURL localhost... ' + (coloring.terminal.end))
        sleep(3)
        uptime.curl('127.0.0.1:80')
        print((coloring.terminal.green) + 'request GET to portal... ' + (coloring.terminal.end))
        sleep(3)
        uptime.get('http://metajets.tk')





    