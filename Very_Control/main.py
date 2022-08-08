# Copyright 2022 by PanDaoxi. All rights reserved.
from socket import socket, AF_INET, SOCK_DGRAM
from os import system, name
from time import strftime, sleep
from colorama import init, Fore, Back
from requests import get

def getIP():
    try:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip

if __name__ == "__main__" and name == "nt":
    print(
        """                                                                         _..._       .-\'\'\'-.                                    .-\'\'\'-.          
                                                                      .-'_..._''.   '   _    \                                 '   _    \  .---. 
 .----.     .----.   __.....__                                      .' .'      '.\/   /` '.   \    _..._                     /   /` '.   \ |   | 
  \    \   /    /.-''         '.         .-.          .-           / .'          .   |     \  '  .'     '.                  .   |     \  ' |   | 
   '   '. /'   //     .-''"'-.  `. .-,.--.\ \        / /          . '            |   '      |  '.   .-.   .     .|  .-,.--. |   '      |  '|   | 
   |    |'    //     /________\   \|  .-. |\ \      / /           | |            \    \     / / |  '   '  |   .' |_ |  .-. |\    \     / / |   | 
   |    ||    ||                  || |  | | \ \    / /            | |             `.   ` ..' /  |  |   |  | .'     || |  | | `.   ` ..' /  |   | 
   '.   `'   .'\    .-------------'| |  | |  \ \  / /             . '                '-...-'`   |  |   |  |'--.  .-'| |  | |    '-...-'`   |   | 
    \        /  \    '-.____...---.| |  '-    \ `  /               \ '.          .              |  |   |  |   |  |  | |  '-                |   | 
     \      /    `.             .' | |         \  /                 '. `._____.-'/              |  |   |  |   |  |  | |                    |   | 
      '----'       `''-...... -'   | |         / /                    `-.______ /               |  |   |  |   |  '.'| |                    '---' 
                                   |_|     |`-' /                              `                |  |   |  |   |   / |_|                          
                                            '..'                                                '--'   '--'   `'-'                               \n\n"""
    )

    init(autoreset=True)
    print(
        "Welcome to Very_Control !\nControlled end:",
        Fore.RED + "http://%s:%s/\n" % (getIP(), strftime("%Y")),
    )
    system("python manage.py runserver %s:%s" % (getIP(), strftime("%Y")))
    input()
