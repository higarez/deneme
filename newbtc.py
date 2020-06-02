import os
import binascii
from bitcoin import *
import requests
from threading import Thread
import certifi
import time
import datetime
import random

threadcount=100
rpr=100
PFile="Plist.txt"

match = "1"
a=0
tproxy=0
http_proxy=[]
testlist=[]
       
class tc():
	syc=1
	ptest=0
	prohttp=True
	stime=time.time()
	restart=False
	etime=stime
	http_syc=0
	""""
def proxytest():
	while(True):
		try:
			tc.restart=True
			for i in range(len(http_proxy)):
				testp=http_proxy[i]
				http_proxy.remove(testp)
				prx= { "http" : testp, "https":testp}
				openurl= requests.get("https://blockchain.info/q/getreceivedbyaddress/147SwRQdpCfj5p8PnfsXV2SsVVpVcz3aPq",certifi.where(),proxies=prx,timeout=10)
				float(openurl.text)
				testlist.append(testp)
				f = open("Proxy_"+str(datetime.date.today())+".txt","a")
				f.write(testp+"\n")
				f.close()
		except:
			if(len(http_proxy)==0):
				tc.ptest+=1
				print(str((threadcount*2)-tc.ptest))
				try:
					print(testp+" Silindi!")
					http_proxy.remove(testp)	
				except:
					fas=False
				break
			try:
				print(testp+" Silindi!")
				http_proxy.remove(testp)
			except:
				fas=False
	if(tc.ptest==tc.http_syc):
		#clear()
		print("Toplam "+str(len(testlist))+ " proxy çalışıyor!\nADRES TARAMA BAŞLIYOR!")
		tc.stime=time.time()
		for i in range(threadcount):
			Thread(target=btcsearch).start()
		"""
def proxycagir():
	try:
		with open(PFile,"r",encoding = "utf-8") as file:
			for i in file:
				testlist.append(i[:len(i)-1])
	except:
		print(PFile +" Bulunamadı!")
	print("Toplam "+str(len(testlist))+" adet proxy bulundu!\nPROXY TESTi BAŞLIYOR!")
	if(threadcount*2>len(testlist)):
		for i in range(len(testlist)):
			tc.http_syc+=1
			Thread(target=btcsearch).start()
	else:
		for i in range(threadcount):
			tc.http_syc+=1
			Thread(target=btcsearch).start()
	
def restarter():
	if(tc.restart==True):
		Thread(target=btcsearch).stop()
		time.sleep(10)
		Thread(target=proxycagir).start()
		tc.restart=False
	
def btcsearch():
	while(True): 
		wif = encode_privkey(random_key(), 'wif')
		addr = privtoaddr(wif)
		if (addr[0:len(match)].lower()==match):
				while (True):
					if(tc.prohttp==True):
						if(tc.syc%4==1 or tc.syc%4==2):
							rndp2=random.randint(0,len(testlist)-1)
							prornd=testlist[rndp2]
							try:
								psel={"http" : prornd,"https" : prornd}
								openurl= requests.get("https://blockchain.info/q/getreceivedbyaddress/" + addr,proxies=psel,timeout=10)
								float(openurl.text)
								#time.sleep(0.5)
								break
							except:
								continue
						elif(tc.syc%4==0 or tc.syc%4==3): 
							prohttp=False
							continue
                     
						try:
							openurl= requests.get("https://blockchain.info/q/getreceivedbyaddress/" + addr,certifi.where())
							float(openurl.text)
							#time.sleep(0.5)
							tc.prohttp=True
							break
						except:
							#time.sleep(1)
							continue
				tc.syc+=1
				if (tc.syc%rpr==0):
					print("Toplam "+str(tc.syc)+" Adres "+str(time.time()-tc.etime)+" Saniyede Bulundu. \nSaniyede ", rpr/(time.time()-tc.stime)," Tarama Yapıldı. \nGünde Ortalama ", rpr/(time.time()-tc.stime)*60*60*24,"Adres Tarayabilir.")
					tc.stime=time.time()
				if (str(openurl.text)!="0"):
							print(addr, wif, "Bakiye Bulundu! Bulunan Bakiye :",openurl.text)
							f = open("Log_"+str(datetime.date.today())+".txt","a")
							f.write(addr+" " +wif+ " Bakiye : "+openurl.text+"\n")
							f.close()
if(tc.prohttp==True):						
	Thread(target=proxycagir).start()
else:
	for i in range(threadcount):
		Thread(target=btcsearch).start()	
		
		
		
		
def clear():
    # İşletim Sistemi Windows ise
    if os.name == 'nt':
        _ = os.system('cls')
    # İşletim Sistemi MacOS ise
    elif os.name == 'mac':
        _ = os.system('clear')
    # İşletim Sistemi Linux ise
    elif os.name == 'posix':
        _ = os.system('clear')
    # Yabancı bir işletim sistemi ise
    else:
        _ = os.system('clear')