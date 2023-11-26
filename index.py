import uuid
import time 
import socket
import os
import json
import colorama


def reset():
    RzIp = "default/ip.json"
    RzUz = "default/user.json"
    with open(RzIp) as mon_fichiersid1:
         dataIp = json.load(mon_fichiersid1) 

    with open(RzUz) as mon_fichiersid2:
         dataUz = json.load(mon_fichiersid2)

    with open("user_data/user.json", 'w') as mon_fichier:
    	json.dump(dataUz, mon_fichier)

    with open("data/ip.json", 'w') as mon_fichier:
    	json.dump(dataIp, mon_fichier)



helper = {"ip s":"save the ip","ip-gui":"show action and your local save","exit":"quit fire shell","profile":"change your name/password"}

os.system("color 0f")

class info:
    version = "1.0"
    creator = "hi group"
    right = None

def cls():
    os.system("cls")
def sleep(t):
    time.sleep(int(t))
print("arret des service veyon")
cls()
os.system("taskkill /F /IM veyon")

print(colorama.Fore.RED)

print(" (                            )       (   (   ")
print(" )\ )  (   (      (        ( /(    (  )\  )\  ")
print("(()/(  )\  )(    ))\   (   )\())  ))\((_)((_) ")
print(" /(_))((_)(()\  /((_)  )\ ((_)\  /((_)_   _   ")
print("(_) _| (_) ((_)(_))   ((_)| |(_)(_)) | | | |  ")
print(" |  _| | || '_|/ -_)  (_-<| ' \ / -_)| | | |  ")
print(" |_|   |_||_|  \___|  /__/|_||_|\___||_| |_|  ")
print("                                        version : "+info.version)

sleep(2)

print("[+] STARTING ...")
null = None
class acjson :
    
    def action(file,name,values):

        modif = None

        if not os.path.isfile(file) : 
            print("error")
            exit()

        with open(file) as mon_fichiers:
            data = json.load(mon_fichiers) 

        modif = data
        modif[name] = values

        with open(file, 'w') as mon_fichier:
        	json.dump(modif, mon_fichier)
        
    def look(file):
        modif = None

        if not os.path.isfile(file) : 
            return "error"

        with open(file) as mon_fichiers:
            data = json.load(mon_fichiers)
        return data


class path:
    data = "./data"
    user_data="./user_data"

class login:
    file = path.user_data+"/user.json"

with open(login.file) as mon_fichier:
    users_data = json.load(mon_fichier) 

class data:
    ip = "./data/ip.json"
    user = "./user_data/user.json"

class user_data :
    name = os.getlogin()
    user = users_data["name"]
    password = users_data["password"]
    login = False

with open(data.ip) as mon_fichier:
    ip_dat_json = json.load(mon_fichier)
    
    
def add(ip,HostName,name):
    lst = { "ip" : ip, "HostName" : HostName , "name" : name}
    num = str(len(ip_dat_json) + 1)

    modif = ip_dat_json
    modif[num] = lst

    print(lst)

    with open(data.ip, 'w') as mon_fichier:
        json.dump(modif, mon_fichier)

# for i in range((len(ip_dat_json)-1)):
       
#        num = str(i+1)
#        print(num)
#        in_lst = ip_dat_json[num]
#        F_ip = in_lst["ip"]

#        print("shutdown /f "+F_ip)


attempt = 5

print("[-]login")
while not user_data.login:
    try_uz = False
    try_pass = False
    
    print(colorama.Fore.WHITE+"attempt "+str(attempt))
    
    users = str(input("user >"))
    passw = str(input("password >"+colorama.Fore.BLACK))
    
    if users == user_data.user:
        try_uz = True
    
    if passw == user_data.password :
        try_pass = True

    if try_uz and try_pass:
        user_data.login = True
    else :
        attempt = attempt - 1
    if attempt == 0:
        print("too many attempt")
        exit()

exita = False

print(colorama.Fore.WHITE+"hello")

class chut:
    ip = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]

cls()

pass_check = False

while not exita:
    usin = input("\n("+user_data.user+"@"+user_data.name+"[shell]>")
    if usin == "ip s":
        print(colorama.Fore.YELLOW,"[saving ip]",colorama.Style.RESET_ALL)
        add(chut.ip,socket.gethostname(),input("name=>"))
        print(colorama.Fore.GREEN+"[+]save"+colorama.Fore.WHITE)
        pass_check = True
    if usin == "getip":
        hname = input("   host_name>")
        print("\n"+ [ip for ip in socket.gethostbyname_ex(hname)[2] if not ip.startswith("127.")][0])
        pass_check = True
    if usin == "ip-gui":
        pass_check = True
        print("--ip gui--\n1:look ip\n2:action\n3:shutdown gui")
        inpu = input(">")
        if inpu == "1":
        
            print(acjson.look(data.ip))
        
        if inpu == "2":

            print("1:shutoff pc")
            inpu = input(">")
            if inpu == "1":
                inpu = input("host>")
                os.system("shutdown -s -t 1 -m "+inpu)
        if inpu == "3":
            os.system("shutdown -i")
    if usin == "exit" :
        pass_check = True
        exita =True
    if usin == "profile":
        pass_check = True
        nw_user = str(input("user_name>"))
        nw_pasw = str(input("password>"))
        
        acjson.action(data.user,"name",nw_user)
        acjson.action(data.user,"password",nw_pasw)
    if usin == "help":
        pass_check = True
        print(helper)

    if usin == "reset":
        rep = input("are you sure you want reset this app [y/N]")
        if rep == "n":
            pass
        if rep =="y":
            print("reseting in progress...")
            print("reseting successe")
            pass_check = True

    if not pass_check:
        print(colorama.Fore.RED+"[!] command not found"+colorama.Fore.RESET)
    pass_check = False

print(colorama.Fore.RED+"end")
os.system("timeout 3")
exit()
