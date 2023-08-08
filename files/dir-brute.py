# -*- coding: utf-8 -*-
import time
import os
import concurrent.futures
import requests
try:
        from colorama import *
except ImportError:
        os.system("clear")
        os.system("pip install colorama")
import time
### LOGO
logo = """ \033[1;94m
   _    _  _____   _   _ ________   ___    _  _____        
 | |  | |/ ____| | \ | |  ____\ \ / / |  | |/ ____|       
 | |  | | (___   |  \| | |__   \ V /| |  | | (___         
 | |  | |\___ \  | . ` |  __|   > < | |  | |\___ \        
 | |__| |____) | | |\  | |____ / . \| |__| |____) |       
 _\____/|_____/__|_|_\_|______/_/_\_\\____/|_____/ _      
 \ \        / /  ____|  _ \  |__   __/ __ \ / __ \| |     
  \ \  /\  / /| |__  | |_) |    | | | |  | | |  | | |     
   \ \/  \/ / |  __| |  _ <     | | | |  | | |  | | |     
    \  /\  /  | |____| |_) |    | | | |__| | |__| | |____ 
     \/  \/   |______|____/     |_|  \____/ \____/|______|
                                                          

"""
os.system("clear")
print (logo)
print(Style.BRIGHT)
inp = input('\033[1;31m>>\033[1;32m Enter Your Url : \033[1;36m')
site = str(inp+"/")
print()
try:
        opn = open("dir.txt","r").readlines()
except:
        print("[+] File Not Found")
        quit()
def scan(x):
        try:
                st = x.strip()
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
                r = requests.get(site+'/'+st,timeout=10,headers=headers)
                code = int(r.status_code)
                if code < 400:
                        print(Fore.GREEN+" [✔] FOUND : "+site+st)
                else:
                        print(Fore.RED+" [❌] NOT FOUND : "+site+st)
        except Exception as e:
                b = 2
try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(scan,opn)
except:
        print(Fore.RED+" [!] Check Your Internet ! ")

