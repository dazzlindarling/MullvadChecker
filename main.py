# https://www.youtube.com/@opseec | https://github.com/opseec | opseec

from colorama import Fore
import requests
import time
from datetime import datetime, timezone
import random
import os
from pystyle import Colorate,Colors

r = Fore.RED
re = Fore.RESET
g = Fore.GREEN

URL = "https://api.mullvad.net/public/accounts/v1"
file = "keys.txt"

def main():
    os.system("cls")
    print(Colorate.Vertical(Colors.blue_to_purple,"""
 ███▄ ▄███▓ █    ██  ██▓     ██▓  ██▒   █▓ ▄▄▄      ▓█████▄ 
▓██▒▀█▀ ██▒ ██  ▓██▒▓██▒    ▓██▒ ▓██░   █▒▒████▄    ▒██▀ ██▌
▓██    ▓██░▓██  ▒██░▒██░    ▒██░  ▓██  █▒░▒██  ▀█▄  ░██   █▌
▒██    ▒██ ▓▓█  ░██░▒██░    ▒██░   ▒██ █░░░██▄▄▄▄██ ░▓█▄   ▌
▒██▒   ░██▒▒▒█████▓ ░██████▒░██████▒▒▀█░   ▓█   ▓██▒░▒████▓ 
░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░░ ▐░   ▒▒   ▓▒█░ ▒▒▓  ▒ 
░  ░      ░░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░░ ░░    ▒   ▒▒ ░ ░ ▒  ▒ 
░      ░    ░░░ ░ ░   ░ ░     ░ ░     ░░    ░   ▒    ░ ░  ░ 
       ░      ░         ░  ░    ░  ░   ░        ░  ░   ░    By ru
                                      ░              ░      
                             ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  
                            ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
                            ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
                            ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
                            ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
                            ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
                              ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
                            ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ 
                            ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     
                            ░                       ░                               

                            https://github.com/ru6w
    """))
    with open(file, "r") as f:
        keys = [line.strip() for line in f if line.strip()]
    keys = list(dict.fromkeys(keys)) 
    vk = []
    for key in keys:
        try:
            res = requests.get(f"{URL}/{key}/")
            json = res.json()
            exp = json["expiry"]
            expiration = datetime.fromisoformat(exp)
            delta = expiration - datetime.now(timezone.utc)
            days = "day" if delta.days == 1 else "days"            

            if res.status_code == 200:
                print(f"{g}VALID - {key} - {delta.days}{days} left{re}")
                vk.append(key)
                time.sleep(0.7)
            else:
                print(f"{r}INVALID - {key} - {res.status_code}{re}")
                time.sleep(0.7)
        except Exception as e:
            print(f"{r}INVALID - {key} - {e} - {res.status_code}{re}")
            time.sleep(0.7)
    if vk:
        rand = random.randint(100000, 999999)
        filename = f"valids{rand}.txt"
        with open(filename, "w") as f:
            for k in vk:
                f.write(f"{k}\n")
        print(f"{g}File: {filename}{re}")
    else:
        print(f"{r}No valid keys found{re}")

main()
