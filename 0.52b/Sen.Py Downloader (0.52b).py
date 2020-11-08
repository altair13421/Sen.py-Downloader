################################
# Sen.Py Dowloader ver 0.52beta #
################################

from tkinter import *
from os import *

# Checking the Dependecy #
try:
    checking = "youtube-dl -help"
    if system(checking) != 0:
        raise Exception()
except:
    system('pip3 install youtube-dl')

# Creating MainWindow #
root = Tk()
root.geometry('848x480')
root.title('Sen.Py Downloader (WIP)')
root.config(background='#23272a')
root.resizable(False,False)

c1 = Canvas(root, width=848, height=350, bg='#23272a', bd=0, highlightthickness=0, relief='ridge')
c1.create_text(424, 50, fill="#ffffff", text="Sen.Py Downloader v0.52b (WIP)", font=('whitney', 22))
c1.pack()

c2 = Canvas(c1, width=626, height=196, bg='#2c2f33', bd=0, highlightthickness=0, relief='ridge')
t = Label(c2, text='CONSOLE WILL BE DISPLAYED HERE',bg='#2c2f33',fg='#99aab5',font=('whitney',16))
c2.create_window(1,1,anchor=NW,window=t)

c1.create_window(424, 240,anchor=CENTER, window=c2)

lab = Label(root,text='Paste Link',bg='#23272a',fg='#99aab5',font=('whitney',16))
lab.pack()
link = StringVar()
link_entry = Entry(root, width = 48, textvariable = link ,fg='#ffffff', bg='#2c2f33',relief='ridge',bd=0,font=('whitney', 18))
link_entry.pack()
pc = Canvas(root, width=848,height=10,bg='#23272a', bd=0, highlightthickness=0, relief='ridge')
pc.pack()
def run():
    system("youtube-dl " + link.get())
downloadButton = Button(root, width = 20, text = "Download",fg='#ffffff', bg='#7289da',relief='ridge',bd=0,font=('whitney', 18),command = run)
downloadButton.pack()

root.mainloop()