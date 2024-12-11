# Coded and Developed By: Tyler Caselli (AKA: Tyguy047 on GitHub and other online spaces)
############################################################################################

# Imports
import os
import platform
import time

# Functions
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def quit():
    def quit():
        if platform.system() == "Windows":
            os.system("taskkill /F /IM cmd.exe")
        else:
            os.system("pkill -f Invest0")

def real_roi():
    print()
    paid = float(input("How Much Did You Pay?: "))
    os.system("clear")
    print()
    now = float(input("How Much Is It Now Worth?: "))
    os.system("clear")
    roi = ((now - paid) / paid) * 100
    print()
    print(f"Your Return On Investment Is: {roi}%")

    

def requested_roi():
    print()
    paid = float(input("How Much Did You Pay?: "))
    os.system("clear")
    print()
    roi = float(input("What ROI% Are You Looking For?: "))
    os.system("clear")
    now = (roi / 100 * paid) + paid
    print()
    print(f"You Need To Sell For: {now}")

# Main Code
while True:
    clear()
    print()
    print("Welcome To Invest0!")
    print("The easiest way to calculate your ROI's (Return On Investments)!")
    print()
    print("1. Calculate Your ROI if you sell now or already sold!")
    print("2. Calculate what you need to sell for to get ROI you want!")
    print()
    choice = input("What Would You Like To Do?: ")


    if choice == "1":
            clear()
            real_roi()
            print()
            input("Press Enter To Go Back To The Menu...")

    elif choice == "2":
            clear()
            requested_roi()
            print()
            input("Press Enter To Go Back To The Menu...")

    else:
            print()
            print("Invalid Choice!")
            print()
            time.sleep(3)
            clear()
    # End Of Code