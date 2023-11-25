import colorama
import os
import requests
import time
from colorama import Fore, Back, Style

colorama.init(autoreset=True)
os.system("mode 80, 25")
os.system("title MCLo.gs Uploader v1.0")
api = "https://api.mclo.gs/1/log"
banner = Fore.LIGHTCYAN_EX + """
            ███╗   ███╗ ██████╗██╗      ██████╗     ██████╗ ███████╗
            ████╗ ████║██╔════╝██║     ██╔═══██╗   ██╔════╝ ██╔════╝
            ██╔████╔██║██║     ██║     ██║   ██║   ██║  ███╗███████╗
            ██║╚██╔╝██║██║     ██║     ██║   ██║   ██║   ██║╚════██║
            ██║ ╚═╝ ██║╚██████╗███████╗╚██████╔╝██╗╚██████╔╝███████║
            ╚═╝     ╚═╝ ╚═════╝╚══════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚══════╝
"""
print(banner)

text = input(Fore.LIGHTRED_EX + "[-] Text: ")

data = {
    'content': text
}

r = requests.post(api, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
if r.status_code == 200:
    result = r.json()
    success = result.get('success', False)

    if success:
        log_id = result.get('id', '')
        url = result.get('url', '')
        raw_url = result.get('raw', '')
        os.system("cls")
        print(banner)
        print(Fore.LIGHTCYAN_EX + "[-] Log URL:", url)
        print(Fore.LIGHTCYAN_EX + "[-] Raw Log URL:", raw_url)
