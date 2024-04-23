import sys
import requests
from colorama import Fore


def __start__():
        try:
                print(Fore.RED+"\n [!] Plase Enter IP/Domain\n")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Whois"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_EaoezVVG7wSzPsBts70iDWRabR1TA&domainName=' + inp).text
                #The used apikey in this link would still work if not try another api in whoisxmlapi.com (signup and generate a new one ;)
                print(Fore.BLUE+result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nExit :)")