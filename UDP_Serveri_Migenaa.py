import socket
import sys
from _thread import *
import random
import datetime

print("----------------------------UDP SERVERI-----------------------")
host='localhost'
port=12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try :
    serverSocket.bind((host,port))
    
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()


print("Serveri tani eshte i gatshem per pranimin e kerkesave")
print("--------------------------------------------------------------")


def bashtingellore(x):
    bashtingelloret = ['B','C','Ç','D','DH','F','G','GJ','H','J','K','L','LL','M','N','NJ','P','Q','R','RR','S','SH','T','TH','V','X','XH','Z','ZH',
                       'b','c','ç','d','dh','f','g','gj','h','j','k','l','ll','m','n','nj','p','q','r','rr','s','sh','t','th','v','x','xh','z','zh']
    numeratori=0
    for shkronja in x:
        if(shkronja in bashtingelloret ):
            numeratori=numeratori+1
    return numeratori

def printo(print):
    print=(str(print)).strip()
    return print

def syprina(n):
    n=int(n)
    Syprina=n * n
    y="Syprina e katrorit =" +str(Syprina)
    return y

def vleraAbsolute(nr):

     if int(nr) >= 0:
       return int(nr)
	
     else:
		
       return -int(nr)

def loja():
    numrat=""
    for number in range(0,7):
        randomNumber=random.randint(1,49)
        numrat+=str(randomNumber)+", "
    return numrat

def fibonacci(numri):
     x=1
     y=1
     for numeruesi in range(2,numri):
            fibonacci = x + y;
            x = y;
            y = fibonacci;
     fibonacciString=str(fibonacci)
     return fibonacciString


def konverto(zgjedh, vlera):
    if zgjedh=="KilowattToHorsepower ":
        rezultati=vlera*1.43

    elif zgjedh=="HorsepowerToKilowatt ":
        rezultati=vlera/1.43 

    elif zgjedh=="DegreesToRadians ":
        rezultati = (180/math.pi) * vlera 

    elif zgjedh=="RadiansToDegrees ":
        rezultati = vlera*(math.pi/180) 

    elif zgjedh=="GallonsToLiters ":
         rezultati = vlera*3.44
     
    elif zgjedh=="LitersToGallons ":
         rezultati = vlera/3.44
   
    else:
        rezultati="Gabim"
    return rezultati



def clientthread(input, address):
    try:
        data = input.decode() 
    except socket.error:
        print("A problem has occurred!")   

    merr=str(data).rsplit(" ")    
    fjalia=""
    i=len(merr)
    for fjala in range(1,i):
        fjalia=fjalia+merr[fjala]          
        if(fjala!=i):
            fjalia+=" "
    if not data:
        return
    elif(merr[0]=="IPADDR"):
        data="Adresa e klientit: "+address[0]
    elif(merr[0]=="PORTNR"):
        data="Porti i klientit: "+str(address[1])
    elif(merr[0]=="BASHTINGELLORE"):
        data="Numri bashtingelloreve: "+str(bashtingellore(fjalia))
    elif(merr[0]=="PRINTO"):
        data="Print: "+str(printo(fjalia))
    elif (merr[0]=="SYPRINA"):
            data="SYPRINA:" +str(syprina(fjalia))
    elif (merr[0]=="ABS"):
            data="Vlera absolute:" +str(vleraAbsolute(fjalia))
    elif(merr[0]=="HOST"):
        try:
            data="Emri i hostit: "+str(socket.gethostbyaddr(host)[0])
        except socket.error:
            data="Host's name not found!"
    elif(merr[0]=="TIME"):
        data="Koha aktuale eshte: "+str(datetime.datetime.now())
    elif(merr[0]=="LOJA"):
        data="Loja ka gjeneruar keta numra: "+loja()
    elif(merr[0]=="FIBONACCI"):
        try:
            vlera=int(merr[1])                
        except Exception:
            return
        data="Fibonacci: "+str(fibonacci(vlera))                           
    elif(merr[0]=="KONVERTO"):
        try:
            numri=float(merr[2])                
        except socket.error:
            return
        data="Vlera e konvertuar: "+str(konverto(merr[1], numri))
       
    else:
        data="The server can't respond to this request!Serveri nuk mund ti pergjigjet kesaj kerkese"
    serverSocket.sendto(data.encode(),address)


while 1:

        data, address=serverSocket.recvfrom(128)
        print("Kerkese e re per: "+str(address))
        start_new_thread(clientthread,(data, address,))

serverSocket.close()
