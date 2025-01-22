import os
import time

os.system("pip3 install pyinstaller")
time.sleep(0.5)
os.system("pyinstaller --onefile Invest0.py")