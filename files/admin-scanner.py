�
���c           @   s|   e  Z e r# d  d  Z � � Z n  d d l Z d d l Z d d l Z d d l Z e d d � Z	 d Z
 d �  Z e �  d S(   i    i����Ns   scan.txtt   rs�   [1;94m
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
[93m TYPE    : Admin-Scanner
[1;32m------------------------------------------
c          C   s�   t  j d � t GHHt d � }  t d � } |  d | d } t j | � } H| j d k rr d |  GHd GHd GHn{ d	 |  GHd
 GHd GHt j d � HxW t	 D]O } | j
 �  } | | } t j | � } | j d k r� d | GHq� d | GHq� Wd  S(   Nt   clearsE   [1;31m[+] [1;32mSITE URL[1;31m (http://site.com) [1;33m: [1;36m sO   [1;31m[+] [1;32mADMIN DIRECTORY[1;31m (admin,administrator)[1;33m :[1;36m t   /i�   s%      [1;31m>>[1;32m SITE    : [1;33ms0      [1;31m>>[1;32m STATUS  :[1;31m NOT FOUND !s,      [1;31m>>[1;32m SCANING :[1;31m ERROR !s%      [1;31m>>[1;32m SITE    :[1;33m s'      [1;31m>>[1;32m STATUS  :[1;32m OKs0      [1;31m>>[1;32m SCANING :[1;32m STARTING...i   s   [1;31m[+] [32mFOUND : s   [1;31m[+] NOT FOUND : (   t   ost   systemt   logot	   raw_inputt   nabilt   gett   status_codet   timet   sleept   filet   strip(   t   sitet   admint   totalt   it   wordst   maint   req(    (    s   admin-scanner.pyR   "   s0    		
(   t   Falset   foot   bart   requestsR   R
   R   t   syst   openR   R   R   (    (    (    s   admin-scanner.pyt   <module>   s   
	