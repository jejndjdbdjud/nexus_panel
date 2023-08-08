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
[93m TYPE    : xss scanner
[1;32m------------------------------------------
"""
os.system('clear')
print(logo)

url = "http://testphp.vulnweb.com/listproducts.php?cat="

##### Paylaods From : https://github.com/capture0x/
print(
"""
\033[1;32m[1] \033[1;31m>> \033[1;32mBasic Payload 
\033[1;32m[2] \033[1;31m>> \033[1;32mDiv Paylaod
\033[1;32m[3] \033[1;31m>> \033[1;32mImage Paylaod
\033[1;32m[4] \033[1;31m>> \033[1;32mBody Paylaod

"""
)

choice = str(input("\033[1;31m>> \033[1;32mChocse Paylaod : \033[1;36m"))
if choice == "1":
	pay = "xss-pay/basic.txt"
elif choice == "2":
	pay = "xss-pay/div.txt"
elif choice == "3":
	pay = "xss-pay/img.txt"
elif choice == "4":
	pay = "xss-pay/body.txt"
else:
	print("\033[1;32m[!] \033[1;31mERROR : Not Found !")
	exit()
o = open(pay,"r",encoding="utf8").readlines()

url = str(input("\033[1;31m>> \033[1;32mEnter Site Url : \033[1;36m"))
if '?' in url:
	url = url 
else:
	print("\033[1;32m[!] \033[1;31mERROR : Enter url with paramater ! ")
	exit()

def scan(x):
	pay = x.strip()
	url_P = url+pay
	req = nabil.get(url_P).text 
	if pay in req:
		print(f"\033[1;32m[+] FOUND     : {url_P}")
	else:
		print(f"\033[1;31m[!] NOT FOUND : {url_P}")
with concurrent.futures.ThreadPoolExecutor() as exe:
	exe.map(scan,o)