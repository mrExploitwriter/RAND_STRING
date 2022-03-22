from rand_string.rand_string import RandString
from colorama import Fore
from time import sleep
from random import randint
from os import system

system("cls")
print(Fore.GREEN + """
     (               ) (       (          (   (       )         
 )\ )   (     ( /( )\ )    )\ )  *   ))\ ))\ ) ( /( (       
(()/(   )\    )\()|()/(   (()/(` )  /(()/(()/( )\()))\ )    
 /(_)|(((_)( ((_)\ /(_))__ /(_))( )(_))(_))(_)|(_)\(()/(    
(_))  )\ _ )\ _((_|_))|___(_)) (_(_()|_))(_))  _((_)/(_))_  
| _ \ (_)_\(_) \| ||   \  / __||_   _| _ \_ _|| \| (_)) __| 
|   /  / _ \ | .` || |) | \__ \  | | |   /| | | .` | | (_ | 
|_|_\ /_/ \_\|_|\_||___/  |___/  |_| |_|_\___||_|\_|  \___| 
                                                            
    """)
print(Fore.BLUE + "\n[1] Random String(Lover)\n\n[2] Random String(Upper)\n\n[0] Exit.")

while True:
    what = input(Fore.RED+"\n\n ┌─["+Fore.LIGHTGREEN_EX+"RAND-STRING"+Fore.RED+"/"+Fore.BLUE+"Select"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
    if what == "1":
        char = int(input(Fore.CYAN + "\n Char:>> "))
        print(Fore.RED + "\n"+RandString("lowercase", char))
    elif what == "2":
        char = int(input(Fore.CYAN + "\n Char:>> "))
        print(Fore.RED + "\n"+RandString("uppercase", char))
    elif what == "0":
        exit(Fore.RED + "\n...")
    else:
        print(Fore.YELLOW + "\nWhat??")
    