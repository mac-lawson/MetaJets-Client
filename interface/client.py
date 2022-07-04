from clientStyle import logo
from clientStyle import coloring


def mainMenu():
    print((coloring.terminal.fail) + (logo.logo) + (coloring.terminal.end))
    print("[1] Settings")
    print("[2] Run")
    menuOptions = input('MetaJets ~ ')
    if (menuOptions == "1"):
        print("")
    if (menuOptions == "2"):
        print('')

    