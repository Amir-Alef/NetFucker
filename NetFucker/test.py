import builtwith
from colorama import Fore
domain = input(Fore.RED+"Please enter your domain target...").lower()
if not "https://" in domain or not "http://" in domain :
    domain = "http://"+domain

infor = builtwith.parse(domain)
for name in infor :
    value = ' '
    for val in infor[str(name)]:
        name = name.replace('-' , " ")
        name = name.title()
        value += str(val)
    print(f"{name} : {value}")
    