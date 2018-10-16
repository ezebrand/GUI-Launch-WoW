import subprocess

print("""
***************************
* Type 1 for WoW Elysium  *
* Type 2 for Light's Hope *
* Type 3 for PTR (ME)     *
***************************
""")

file = open("realmlist.wtf","w")
loop_ctrl = True

while loop_ctrl is True:
    answer = input("Enter choice: ")

    if str(answer) == '1':
        file.write("set realmlist logon.elysium-project.org")
        subprocess.Popen([r"C:\Users\e_h67\Desktop\Current SW (new)\WoW.exe"])
        loop_ctrl = False
    elif str(answer) == '2':
        file.write("set realmlist logon.lightshope.org")
        subprocess.Popen([r"C:\Users\e_h67\Desktop\Current SW (new)\WoW.exe"])
        loop_ctrl = False
    elif str(answer) == '3':
        file.write("set realmlist 35.194.35.198")
        subprocess.Popen([r"C:\Users\e_h67\Desktop\Current SW (new)\WoW.exe"])
        loop_ctrl = False
    else:
        print("Incorrect selection! Try again or type X to exit.")

    if answer in ('X','x'):
        print("Exiting...")
        break

file.close()
