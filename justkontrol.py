import os
import binascii
from bitcoin import *
import requests
from threading import Thread
import certifi
import time
import datetime

threadcount=50
rpr=2000
PFile="file1.txt"
addresslist=[]
loglama=False

with open(PFile,"r",encoding = "utf-8") as file:
    for i in file:
        addresslist.append(i[:len(i)-1])
        
class totalcount():
    syc=1
    
def btcsearch():
    while(True):
        addr=addresslist[0]
        addresslist.remove(addr)
        wif=addresslist[0]
        addresslist.remove(wif)
        if (len(addresslist)==0):
            break
        while (True):
            try:
                openurl= requests.get("https://blockchain.info/q/getreceivedbyaddress/" + addr)
                float(openurl.text)
                if(loglama==True):
                    f = open("Log_"+str(datetime.date.today())+".txt","a")
                    f.write(addr+" " +wif+ " Bakiye : "+openurl.text+"\n")
                    f.close()
                break
            except:
                time.sleep(1)
                continue			
        totalcount.syc+=1
        if (totalcount.syc%rpr==0):
            print(totalcount.syc, " Adet Adres",time.time()-stime, " Saniyede Bulundu.\nSaniyede ", totalcount.syc/(time.time()-stime)," Tarama Yapıldı. \nGünde Ortalama ", totalcount.syc/(time.time()-stime)*60*60*24,"Adres Tarayabilir.")
        if (openurl.text!="0"):
            print(addr, wif, "Bakiye Bulundu! Bulunan Bakiye :",openurl.text)
            f = open("Bulunan_"+str(datetime.date.today())+".txt","a")
            f.write(addr+" " +wif+ " Bakiye : "+openurl.text+"\n")
            f.close()
        if (addresslist.len==0):
            print("Adreslist Bitti. Yeni liste ekleyin.")

for i in range(threadcount):
    stime=time.time()
    Thread(target=btcsearch).start()
