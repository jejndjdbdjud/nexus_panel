#!/usr/bin/bash

main() {
clear

echo -en "
\033[34m
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
[93m TYPE    : NO-RE
[1;32m------------------------------------------ "
echo -e "\e[32m"

echo 
echo -e "\e[31m[+]\e[32m STARTING SERVER..."
sleep 2
php -S 127.0.0.1:5555 > /dev/null 2>&1 &
echo -e "\e[31m[+]\e[32m SERVER HOSTED SUCCESFULLY : 127.0.0.1:5555"
sleep 1
xdg-open http://127.0.0.1:5555 
echo 
read -p "PRESS ENTER TO GO BACK MENU" user 
if [ user = "" ]
then
python2 n-web.py 
fi
}
main

