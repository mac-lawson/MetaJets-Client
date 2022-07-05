from clientStyle import logo
from clientStyle import coloring
from interface import run   

def mainMenu():
    while True:
        print((coloring.terminal.fail) + (logo.logo) + (coloring.terminal.end))
        menuOptions = input('Press Enter to Run')
        run.getWeb('http://metajets.tk')



    