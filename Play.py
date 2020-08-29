#from rpg import *
import os
import random
#import re
current_path = os.getcwd()
while(True):
    os.chdir(current_path)
    choice = int(input("We currently only generate Python and Lua programs.\nEnter 1 if you want to work on Python.\n2 to work on Lua.\n3 to run already built programs.\n"))
    if(choice == 1):
        choice = int(input("1 - To work on GUI.\n2 - To work without GUI.\n"))
        if(choice == 1):
            import Python_g
        else:
            import Python
    elif(choice == 2):
        import Lua
        #print("Okay.")
    else:
        import Run
    choice= int(input("Enter:\n1 to continue working.\n2 to stop.\n"))
    if(choice == 2):
        break
