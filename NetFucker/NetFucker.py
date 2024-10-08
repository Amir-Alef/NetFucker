import os 
import sys 
import socket
import time
from HelpList import help
from Modules import whois , cms , finder , iplocation , reverseip , robots , cloudflare 

try :
    from colorama import Fore
except :
    os.system("clear")
    print("""\n
    please install colorama than run the tool!\n
    pip3 install colorama
    """)  

try :
   import requests 
except :
    os.system("clear")
    print("""\n
    please install colorama than run the tool!\n
    pip3 install requests
    """)  

try :
    import ipapi 
except :
    os.system("clear")
    os.system("pip3 install ipapi")
    print("""\n
    please install colorama than run the tool!\n
    pip3 install ipapi \n
    we just installed it try again :)
    """)  

try :
   import builtwith
except :
   os.system("clear")
   print("""\n
    please install colorama than run the tool!\n
    pip3 install builtwith
    """)  
  

number = None
while True:
    help.Banner()    
    help.infoList1()
    number= input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"NETFUCKER"+Fore.BLUE+"~"+Fore.WHITE+("@HOME")+Fore.RED+"""]
     └──╼ """+Fore.WHITE+"$ ").lower()
    


    if number == "4":
        print("GOOD LUCK SEE YOU SOON :D ... ")
        time.sleep(2)
        sys.exit()

    elif number == "" or number==" " or number== None:
        input(Fore.RED+"[ ! ]"+ Fore.WHITE+"Please Enter A Number(Press Enter) ")
       
    
 #-----------INFOREMATION GATHERING-------------


    elif number == '1':
        try:
            help.Banner()
            help.infoList2()
            infor = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"NETFUCKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"Information Gathering"+Fore.RED+"""]
            └──╼ """+Fore.WHITE+"$ ").lower()
            
            if infor == "1":
                help.Banner()
                cloudflare.__start__()


            elif infor == "2":
                help.Banner()
                iplocation.__start__()

   
            elif infor == "3":
                help.Banner()
                cms.__start__()


#            elif infor == "4":
#                helpp.Banner()
#               portscan.__start__()
                

            elif infor == "5":
                help.Banner()
                whois.__start__()    


            elif infor == "6":
                help.Banner()
                finder.__start__()


#            elif infor == "7":
#                helpp.Banner()
#                findsharedns.__start__()



#            elif infor == "8":
#               helpp.Banner()
#                Traceroute.__start__()
# coming soon ... (debugging...)




            elif infor == "9":
                help.Banner()
                reverseip.__start__()



#            elif infor == "10":
#                helpp.Banner()
#               httpheader.__start__()



#            elif infor == "11":
#               helpp.Banner()
#                dnslookup.__start__()  


            elif infor == "12":
                help.Banner()
                robots.__start__()


            elif infor == "13":
                input(Fore.RED+" [!]"+Fore.GREEN+" Back To Menu (Press Enter...) ")


            elif infor == "14":
                sys.exit()

                
            elif infor == "" or " ":
                input(Fore.RED+" [!]"+Fore.GREEN+" Please Enter Number (Press Enter...) ")

        except KeyboardInterrupt:
            print("")
            sys.exit()
    elif number == "2":
        try:
            help.infolist4()
            infor2 = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"NETFUCKER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"CMS Detection"+Fore.RED+"""]
                └──╼ """+Fore.WHITE+"$ ").lower()
            if infor2 == "" or " " :
                input(Fore.RED+"Please Enter a Number (Press Enter...)")
            
        except KeyboardInterrupt:
            print("")
            sys.exit()
    

    elif number == "3":
        try:
            help.infolist3()
        except KeyboardInterrupt:
            print("")
            sys.exit()
