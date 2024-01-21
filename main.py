import os
os.system("cls")
import requests
import time
import pyfade
from pypresence import Presence
RPC = Presence("1191806913734783046")
RPC.connect()
RPC.update(state='Generating Promos', details='Astral Nitro Generator', large_image='astrala',small_image="astrala",large_text="discord.astralmods.com",small_text="AstralGen")

print(pyfade.Fade.Vertical(pyfade.Colors.blue_to_red, text = f"""                                                                       
                     █████╗ ███████╗████████╗██████╗  █████╗ ██╗     
                    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     
                    ███████║███████╗   ██║   ██████╔╝███████║██║     
                    ██╔══██║╚════██║   ██║   ██╔══██╗██╔══██║██║     
                    ██║  ██║███████║   ██║   ██║  ██║██║  ██║███████╗
                    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                     ██████╗ ███████╗███╗   ██╗
                    ██╔════╝ ██╔════╝████╗  ██║
                    ██║  ███╗█████╗  ██╔██╗ ██║
                    ██║   ██║██╔══╝  ██║╚██╗██║
                    ╚██████╔╝███████╗██║ ╚████║
                     ╚═════╝ ╚══════╝╚═╝  ╚═══╝ By Kerely and vowzy."""))

print("\n")

headers = {
    "authority": 'api.discord.gx.games',
    "accept": '*/*',
    "accept-language": 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    "content-type": 'application/json',
    "origin": 'https://www.opera.com',
    "referer": 'https://www.opera.com/',
    "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": 'empty',
    "sec-fetch-mode": 'cors',
    "sec-fetch-site": 'cross-site',
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0 (Edition std-1)'
}

json_data = {"partnerUserId": "a599e4c9-d746-4516-8abb-067070a06ef7"}

while True:
    api_fulfillment = "https://api.discord.gx.games/v1/direct-fulfillment"
    response = requests.request("POST", api_fulfillment, json=json_data, headers=headers)
    data = response.json()
    
    url = 'https://discord.com/billing/partner-promotions/1180231712274387115/' + data['token']
    
    if response.status_code == 200:
       print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text=f"[+] Valid = " + url))
       with open('nitros.txt', 'a') as file:
        file.write(url + '\n')
        print('\n')
        time.sleep(0.2)
    elif response.status_code == 429:
                print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text=f"Rate Limited. Waiting for cooldown..."))
                time.sleep(60)  
    else:
        print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text=f"{response.status_code}."))    
        print(pyfade.Fade.Horizontal(pyfade.Colors.blue_to_purple, text=f"{response.text}"))
        time.sleep(5)
