##############################
## Custom PYTHON DOWNLOADER ##
##############################

from os import *
from subprocess import *
from time import *
system('pip3 install pyperclip')
import pyperclip as clipb

def prompt():
    print("What Kind Of Input Method Will You Like?")
    print("1. Copy From Clipboard?")
    print("2. Copy Link Now And Paste From Clipboard?")
    print("How Will Option 1 and Option 2 Work?")
    print("Option 1 Will Copy anything that is In the Clipboard. You can Copy On this Menu and not wait Or Option 2")
    print("And Option 2 Will Wait For your Input until you Copy it and Will Paste it When You input any key (and Press Enter)")
    input_method = input(" > ")
    if input_method == 1:
        option1()
    else:
        option2()
    
def option1():
    pastedLink = clipb.paste()
    try:
        if pastedLink.find('youtu') >= 0:
            print("It is a Youtube Link..... Proceeding to Download..... ")
            downloading(pastedLink)
        else:
            raise Exception("It is Not a Youtube Link")
            
    except:
        print("Trying Option 2")
        option2()
        
def option2():
    print('No Link Copied')
    print('Copy the Link and Whenever You\'re Ready, press Enter')
    input("Are You Ready?\n > ")
    option1()
        
def downloading(link):
    system(f"youtube-dl {link}")
    print("It's Downloaded in The Folder Where you Put this FILE IN")
    sleep(2)
    input("Press anything to exit")

def installingytdl():
    print('Installing youtube-dl.......')
    system("pip3 install youtube-dl")
    prompt()
    
def checkingforstuff():
    system('cls')
    print("This Will Require a checking Whether dependencies are installed or not. (Disclaimer: Don't Worry, it's Harmless)")
    pythoncheck = 'python -help'
    youtubecheck = 'youtube-dl -help'
    sleep(3)
    print("Checking youtube-dl........ ", end = '')
    
    try:
        if system(youtubecheck) != 0:
            raise Exception("youtube-dl Doesn't Exist")
        else:
            print("installed")
            sleep(2)
            system("cls")
            prompt()
    except:
        print("Youtube-dl not Installed! Install youtube-dl now? press Y")
        check = input(" > ")
        if check in {'y', "Y"}:
            installingytdl()
        else:
            print('Ok, Sayonara')
            system("exit")
            
print('Welcome to My Downloader, It uses another Download To Become a Downloader Funky, ain\'t it?')
checkingforstuff()
