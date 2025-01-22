# Coded and Developed By: Tyler Caselli (AKA: Tyguy47/Tyguy047 on GitHub and other online spaces)
############################################################################################

# Imports
import time
from functions import *

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

        if choice == KeyboardInterrupt:
                clear()
                print()
                print("Goodbye!")
                time.sleep(1)
                quit()

# End Of Code
