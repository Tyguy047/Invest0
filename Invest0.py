# Coded and Developed By: Tyler Caselli (AKA: Tyguy047 on GitHub and other online spaces)
############################################################################################

# Imports
import os
import platform
import time

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

# Main Code
while True:
    clear()
    print("""
Welcome To 𝙸𝚗𝚟𝚎𝚜𝚝𝟶!
The easiest way to calculate your ROI's (Return On Investments)!

          
Menu:
          
1. Calculate Your ROI if you sell now or already sold!
2. Calculate what you need to sell for to get ROI you want!
3. Exit/Quit!
""")

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

    elif choice == "3":
            clear()
            print()
            print("Goodbye!")
            time.sleep(1)
            quit()

    else:
            print()
            print("Invalid Choice!")
            print()
            time.sleep(1)
            clear()
    # End Of Code