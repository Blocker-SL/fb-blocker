#!/ufr/bin/python2
#coding=utf-8
#shell

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
print("FB GRABER")
os.system('clear')




reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 OPR/69.0.3686.77')]


def kelwa():
  print "\x1b[1;96m🚶‍  \x1b[1;91 Chwna dara wa"
  os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def anime(z):
  for e in z + '\n':
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(000.1)


#### LOGO ####
logo = """

___.   .__                 __                 
\_ |__ |  |   ____   ____ |  | __ ___________ 
 | __ \|  |  /  _ \_/ ___\|  |/ // __ \_  __ \
 | \_\ \  |_(  <_> )  \___|    <\  ___/|  | \/
 |___  /____/\____/ \___  >__|_ \\___  >__|   
     \/                 \/     \/    \/       

                                                        
"""
def tik():
  titik = ['.   ','..  ','... ']
  for o in titik:
    print("\r\x1b[1;95mLoding bwasta \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
\x1b[31;1m@            Blocker  SL                @
\x1b[37;1m+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×+×++×+×+×+×+
"""                                
hr = """

___.   .__                 __                 
\_ |__ |  |   ____   ____ |  | __ ___________ 
 | __ \|  |  /  _ \_/ ___\|  |/ // __ \_  __ \
 | \_\ \  |_(  <_> )  \___|    <\  ___/|  | \/
 |___  /____/\____/ \___  >__|_ \\___  >__|   
     \/                 \/     \/    \/       

  
version >> 1.0
BLOCKER >> SL                                  
"""
print(hr)
CorrectUsername = "Kurdm"
CorrectPassword = "Blockerm"
os.system('xdg-open https://www.instagram.com/sparok.io')
loop = 'true'
while (loop == 'true'):
    username = raw_input("\x1b[34;1m👨‍ \x1b[1;95mID \x1b[31;1m>>\x1b[1;91m")
    if (username == CorrectUsername):
      password = raw_input("\x1b[34;1m🤖 \x1b[1;95mID Paswword \x1b[37;1m>>>\x1b[1;91m")
        if (password == CorrectPassword):
            print " Krayawa ID " + username #Baha J HeX
      time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96m password xalata"
            
    else:
        print "\033[1;96mID xalata "
