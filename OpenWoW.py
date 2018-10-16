import subprocess
from tkinter import *
from tkinter import ttk

def get_elysium(event):
    file = open("realmlist.wtf","w")
    file.write("set realmlist logon.elysium-project.org")
    file.close()
    subprocess.Popen([r"C:\Users\e_h67\Desktop\Current_SW_(new)\WoW.exe"])
    root.destroy()

def get_lightsHope(event):
    file = open("realmlist.wtf","w")
    file.write("set realmlist logon.lightshope.org")
    file.close()
    subprocess.Popen([r"C:\Users\e_h67\Desktop\Current_SW_(new)\WoW.exe"])
    root.destroy()

def get_maximumEffort(event):
    file = open("realmlist.wtf","w")
    file.write("set realmlist 35.194.35.198")
    file.close()
    subprocess.Popen([r"C:\Users\e_h67\Desktop\Current_SW_(new)\WoW.exe"])
    root.destroy()

root = Tk()

windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))
root.geometry("325x175")

background_image = PhotoImage(file = "C:\\Users\\e_h67\\Desktop\\Git_testing\\Vanilla.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.title("Vanilla WoW Server Selection")

elysiumButton = Button(root, text="Elysium - Nighthaven", bg="khaki2")
elysiumButton.grid(padx=30, pady=15)
elysiumButton.bind("<Button-1>", get_elysium)

lightsHopeButton = Button(root, text="Light's Hope - Northdale", bg="sandy brown")
lightsHopeButton.grid(padx=30, pady=15)
lightsHopeButton.bind("<Button-1>", get_lightsHope)

maximumButton = Button(root, text="Maximum Effort - PTR", bg="thistle4")
maximumButton.grid(padx=30, pady=15)
maximumButton.bind("<Button-1>", get_maximumEffort)

root.mainloop()
