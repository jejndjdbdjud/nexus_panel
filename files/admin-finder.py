�
����c           @   s�   e  Z e r# d  d  Z � � Z n  d d l Z d d l Z d d l Z d d l Z e j �  Z e	 d d � Z
 e j d � d Z d �  Z e �  d S(   i    i����Ns	   paths.txtt   rs   rm -rf found.txts�   [1;94m
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
[93m TYPE    : Admin-Finder
[1;32m------------------------------------------
c          C   sA  t  j d � t GHHt d � }  t j |  � } | j d k rE d GHn� Hx� t D]� } | j �  } t	 j
 |  | � } | j d k r� d |  | GHt  j d � |  | } t d d � } | j d	 | d
 � } | j �  n  |  | |  d k r,t j d � t  j d � t GHHd GHd GHt  j d � Hd GHqM d |  | GHqM Wd  S(   Nt   clears)   [1;31m>>[1;32m Enter Your Url : [1;36mi�   s   URL ERROR PLS CHK !s   [1;32m[+] FOUND : s   touch found.txts	   found.txtt   as   [+] s   
s   /Admin2015/i   s)   [1;31m<<<[1;33m FOUNDED URLS [1;31m>>>s   [1;32ms   cat found.txts    [1;33m   << Thanks For Using >>s   [1;31m[!] Not Found (   t   ost   systemt   logot	   raw_inputt   requestst   headt   status_codet   wordlistt   stript   sessiont   gett   opent   writet   closet   timet   sleep(   t   webt   req_codet   wordt   reqt   foundt   vt   f(    (    s   admin-finder.pyt   main"   s:    
(   t   Falset   foot   barR   t   sysR   R   t   SessionR   R   R
   R   R   R   (    (    (    s   admin-finder.pyt   <module>   s   
	'