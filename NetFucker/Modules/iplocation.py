import requests
import os
import sys
import ipapi
from colorama import Fore

def __start__():
    print(Fore.RED+"\n [!] Enter IP Address")
    print(Fore.RED+"\n [/] Or Press The Enter Key :))) \n")
    
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"NetFucker"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Location"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
    source = requests.get("https://ipapi.co/"+site+"/json/").json()
    try:
        print(str(source))
        print(Fore.GREEN+" [!]"+Fore.RED+" See your info")
        print(Fore.GREEN+" [!]"+Fore.BLUE+" ip = "+ source["ip"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" city = " + source["city"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" region = "+ source["region"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" id country = "+source["country"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" country = "+ source["country_name"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Calling Code = "+source["country_calling_code"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" Languages = "+source["languages"])
        print(Fore.GREEN+" [!]"+Fore.BLUE+" org = "+ source["org"])
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
        except:
            print("something in our apis went wrong Sorry:( )")
            print("")
            sys.exit()  
    except:
        print(Fore.RED+"Sorry Please Enter IP Address")

