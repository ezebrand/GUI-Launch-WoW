import subprocess
from tkinter import *
from tkinter import ttk

def get_elysium(event):
    file = open("realmlist.wtf","w")
    file.write("set realmlist logon.elysium-project.org")
    file.close()
    #subprocess.Popen([r"C:\Users\e_h67\Desktop\Current SW (new)\WoW.exe"])
    root.destroy()

def get_lightsHope(event):
    file = open("realmlist.wtf","w")
    file.write("set realmlist logon.lightshope.org")
    file.close()
    #subprocess.Popen([r"C:\Users\e_h67\Desktop\Current SW (new)\WoW.exe"])
    root.destroy()

def get_maximumEffort(event):
    file = open("realmlist.wtf","w")
    file.write("set realmlist 35.194.35.198")
    file.close()
    #subprocess.Popen([r"C:\Users\e_h67\Desktop\Current SW (new)\WoW.exe"])
    root.destroy()

root = Tk()
root.geometry("325x175")

root.title("Vanilla WoW Server Selection")

elysiumButton = Button(root, text="Elysium - Nighthaven")
elysiumButton.grid(padx=30, pady=15)
elysiumButton.bind("<Button-1>", get_elysium)

lightsHopeButton = Button(root, text="Light's Hope - Northdale")
lightsHopeButton.grid(padx=30, pady=15)
lightsHopeButton.bind("<Button-1>", get_lightsHope)

maximumButton = Button(root, text="Maximum Effort - PTR")
maximumButton.grid(padx=30, pady=15)
maximumButton.bind("<Button-1>", get_maximumEffort)

root.mainloop()
