import requests
import time
import json
import os
from colorama import Fore, init
import ctypes
from pystyle import *
ctypes.windll.kernel32.SetConsoleTitleW("HypeSquad Setter | @x.skuno")
init(autoreset=True)
banner = """ 

      :::    :::      ::::::::  :::    ::: :::    ::: ::::    :::  :::::::: 
     :+:    :+:     :+:    :+: :+:   :+:  :+:    :+: :+:+:   :+: :+:    :+: 
     +:+  +:+      +:+        +:+  +:+   +:+    +:+ :+:+:+  +:+ +:+    +:+  
     +#++:+       +#++:++#++ +#++:++    +#+    +:+ +#+ +:+ +#+ +#+    +:+   
   +#+  +#+             +#+ +#+  +#+   +#+    +#+ +#+  +#+#+# +#+    +#+    PRESS ENTER
 #+#    #+# #+# #+#    #+# #+#   #+#  #+#    #+# #+#   #+#+# #+#    #+#     
###    ### ###  ########  ###    ###  ########  ###    ####  ########       V1.0


"""

bannermenu = """ 
███████╗███████╗████████╗████████╗███████╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
███████╗█████╗     ██║      ██║   █████╗  ██████╔╝
╚════██║██╔══╝     ██║      ██║   ██╔══╝  ██╔══██╗
███████║███████╗   ██║      ██║   ███████╗██║  ██║
╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                  
[!] https://github.com/skun0
[+] https://salvatorerusso.xyz   


HypeSquad IDs:
1 = Bravery
2 = Brilliance
3 = Balance                    """
with open("config.json", "r") as f:
    config = json.load(f)

token = config.get("token")
def set_hypesquad(house_id, token):
    url = "https://discord.com/api/v9/hypesquad/online"
    headers = {"Authorization": f"{token}"}
    data = {"house_id": house_id}
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 204:
            print(Fore.GREEN + "[!] HypeSquad set successfully.")
            
            
    else:
        print(Fore.RED + f"[!] {response.status_code}")
        Fore.RESET
        

def menu():
    print(Colorate.Vertical(Colors.red_to_yellow, f'{bannermenu}'))
    house_choice = input("\nEnter ID: ")
    set_hypesquad(int(house_choice), token)
    os.system("pause")
while True:
    os.system("cls")
    Anime.Fade(Center.Center(banner), Colors.red_to_yellow, Colorate.Vertical, enter=True)
    menu()
