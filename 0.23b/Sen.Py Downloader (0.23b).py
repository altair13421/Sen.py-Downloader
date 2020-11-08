################################
# Sen.PyDowloader ver 0.23beta #
################################

########################
# importing Statements #
########################

import tkinter as tk
from tkinter import ttk
from os import *

# Creating Main Window #
mainWindow = tk.Tk()
mainWindow.title("THE SENPAI DOWNLOADER")

mainLabel = ttk.Label(mainWindow, width = 55, text = "Welcome to The Senpai Downloader\n Here you Can Download Youtube VIDEOS\n It's Something of a Project (Self Inflicted wounds, It Hurts, doesn't It?)")
mainLabel.grid(column = 0, row = 0)
# Now with that out of the way #
# Let's Create a Downloader for Real, Senpai #

def downloaddepen():
    system("pip3 install youtube-dl")
    system("echo Proceed to Download, Close all Other Windows (Not this One)")

def downloadYTDL():
    ytWin = tk.Tk()
    ytWin.title("Dependency")
    ytLabel = ttk.Label(ytWin, width = 40, text = "Download Dependency?")
    ytLabel.grid(column = 0, row = 0)
    ytButton = ttk.Button(ytWin, width = 35, text = "Download and Install", command = downloaddepen)
    ytButton.grid(column = 1, row = 1)

def installed():
    insWin = tk.Tk()
    insWin.title("Installation?")
    insLabel = ttk.Label(insWin, width = 40, text = "It is Installed\nClose this Window")
    insLabel.grid(column = 0, row = 0)

def check():
    try:
        youtubecheck = "youtube-dl -help"
        if system(youtubecheck) != 0:
            raise Exception("youtube-dl Doesn't Exist")
        else:
            installed()
    except:
        downloadYTDL()

def disclaimer():
    disclWindow = tk.Tk()
    disclWindow.title("Disclaimer")
    disclaimLabel = ttk.Label(disclWindow,width = 70, text = "I hope you do have Python Installed, Cause This Won't Work Without it\n Download it using the Button below")
    disclaimLabel.grid(column = 0, row = 0)
    disclWindow.resizable(False, False)

    downYTButton = ttk.Button(disclWindow, text = "Check for Dependencies", command = check)
    downYTButton.grid(column = 0, row = 2)

def downloadCommand():
    system("youtube-dl " + link.get())
    system("echo \"It is Done, Senpai\"")

def runCommand():
    downloaderWin = tk.Tk()
    downloaderWin.title("Download Bar (Supposed)")
    downloadLabel = ttk.Label(downloaderWin, width = 50, text = "Senpai, it Hath Downloadeth")
    downloadLabel.grid(column = 2, row = 2)
    downloaderWin.resizable(False, False)
    downloadCommand()

discButton = ttk.Button(mainWindow, width = 30, text = "Disclaimer (Senpai Look at me)", command = disclaimer)
discButton.grid(column = 4, row = 2)

link = tk.StringVar()
link_entry = ttk.Entry(mainWindow, width = 50, textvariable = link)
link_entry.grid(column = 0, row = 5)

downloadButton = ttk.Button(mainWindow, width = 30, text = "Download Now, Senpai", command = runCommand)
downloadButton.grid(column = 4, row = 5)
# To do List: Dark Mode #
# mainLabel.configure(background = "grey", foreground = "white")
# RUNNING THE GUI #
mainWindow.mainloop()

########################################################################################################
# ver 0.23beta (and Yet It works Perfectly Somehow, Not perfectly "Set" as that, but it works Perfect) #
########################################################################################################
