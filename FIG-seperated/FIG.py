import random
from random import randint
from random import choice
import time
import os
from FIGdb import *
commands = ["cls","clear"]
print("""

 __          __  _                            _          ______    _          _     _            _   _ _                                           _             
 \ \        / / | |                          | |        |  ____|  | |        (_)   | |          | | (_) |                                         | |            
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |__ __ _| | _____   _  __| | ___ _ __ | |_ _| |_ _   _    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __/ _` | |/ / _ \ | |/ _` |/ _ \ '_ \| __| | __| | | |  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | (_| |   <  __/ | | (_| |  __/ | | | |_| | |_| |_| | | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  \__,_|_|\_\___| |_|\__,_|\___|_| |_|\__|_|\__|\__, |  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                            __/ |   __/ |                                        
                                                                                                           |___/   |___/                                         

""")

def creds():
        print("Name          :",random.choice(names))
        print("Phone         :",random.choice(phones))
        print("Address       :",random.choice(addreses))
        print("Email         :",random.choice(emails))
        print("CreditCard    :",randint(1000000000000000, 9999999999999999))
        print("ExpirationDate:",randint(1,12), "/", randint(24,28))
        print("CVC           :",randint(100, 999))
        print("PIN           :",randint(1000,9999))
        print("Balance       :",randint(300000, 20000000))
        print("IPV4          :",random.choice(ipv4))
        print("IPV6          :",random.choice(ipv6))
        print("Age           :",randint(0,90))
        print("Password      :",random.choice(password))
        print("SSN           :",random.choice(ssn))
        print("SIN           :",random.choice(sin))
        print("")
oschoice = int(input("""Which os are you using?
    0 -- windows
    1 -- linux """))

def manual():
    while 0 == 0:
        b = input("Press enter if you want to generate ")
        if b == "A" or "a":
            os.system(commands[oschoice])
            creds()
def automatic():
    creds()
    while 0 == 0:
        os.system(commands[oschoice])
        creds()
        time.sleep(2)
        
    

choice = int(input("""Choose:
    1 -- Manual mode
    2 -- Automatic mode """))
if choice == 1:
    manual()
elif choice == 2:
    automatic()








