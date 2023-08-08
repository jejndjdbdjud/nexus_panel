#!/usr/bin/python 
import os 
from googlesearch import search 

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
[93m TYPE    : DORK SCANNER
[1;32m------------------------------------------
os.system("clear")
print(logo)

query = str(input("\033[1;31m>> \033[1;32mEnter Dork To Scan : \033[1;36m"))
limit = int(input("\033[1;31m>> \033[1;32mHow Many Site You Want To Display : \033[1;36m"))
if query == "":
	exit()
if limit == "":
	exit()

print("")
count = 0 
for url in search(query,num=limit,start=0,stop=None,pause=2):
	print(f"\033[1;35m[+] \033[1;31m>> \033[1;32m{url}")
	if count == limit:
		exit()
	count = count + 1
