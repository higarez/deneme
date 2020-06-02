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
match = "1"
loglama=False

class totalcount():
	syc=1

def btcsearch():
	t=totalcount()
	while(True): 
		wif = encode_privkey(random_key(), 'wif')
		addr = privtoaddr(wif)
		if (addr[0:len(match)].lower()==match):
				while (True):
					try:
						openurl= requests.get("https://blockchain.info/q/getreceivedbyaddress/" + addr)
						float(openurl.text)
						time.sleep(1)
						if(loglama==True):
							f = open("Log_"+str(datetime.date.today())+".txt","a")
							f.write(addr+" " +wif+ " Bakiye : "+openurl.text+"\n")
							f.close()
						break
					except:
						time.sleep(0.5)
						continue			
				totalcount.syc+=1
				if (totalcount.syc%rpr==0):
					print(totalcount.syc, " Adet Adres",time.time()-stime, " Saniyede Bulundu.\nSaniyede ", totalcount.syc/(time.time()-stime)," Tarama Yapıldı. \nGünde Ortalama ", totalcount.syc/(time.time()-stime)*60*60*24,"Adres Tarayabilir.")
				if (str(openurl.text)!="0"):
							print(addr, wif, "Bakiye Bulundu! Bulunan Bakiye :",openurl.text)
							f = open("Bulunan_"+str(datetime.date.today())+".txt","a")
							f.write(addr+" " +wif+ " Bakiye : "+openurl.text+"\n")
							f.close()
                            
for i in range(threadcount):
    Thread(target=btcsearch).start()
    if(i==threadcount):
        stime=time.time()