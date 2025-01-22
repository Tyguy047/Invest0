# Imports
import os
import platform

# Functions
def quit():
    if platform.system() == "Windows":
        os.system("taskkill /f /im cmd.exe")     
    else:
        os.system("exit")
        os.system("killall Terminal")

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def real_roi():
    print()
    paid = float(input("How Much Did You Pay?: "))
    clear()
    print()
    now = float(input("How Much Is It Now Worth?: "))
    clear()
    roi = ((now - paid) / paid) * 100
    print()
    print(f"Your Return On Investment Is: {roi}%")

def requested_roi():
    print()
    paid = float(input("How Much Did You Pay?: "))
    clear()
    print()
    roi = float(input("What ROI% Are You Looking For?: "))
    clear()
    now = (roi / 100 * paid) + paid
    print()
    print(f"You Need To Sell For: {now}")