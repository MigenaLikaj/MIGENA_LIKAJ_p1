from _thread import *
import random
import datetime
import os
import socket
import sys
import math

host='localhost'
port=12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try :
    serverSocket.bind((host,port))
except socket.error:
    print("Client can't be reached!")
    sys.exit()

serverSocket.listen(5)

print("Tani SERVERI mund te pranoje kerkesa")


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

def fibonacci(number):
     x=1
     y=1
     for numeruesi in range(2,number):
            fibonacci = x + y;
            x = y;
            y = fibonacci;
     return fibonacci


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





def clientthread(conn):
    while True:
        try:
            data = conn.recv(128).decode()  
        except socket.error:
            print("A problem has occurred!") 
            break   

        
        merr=str(data).rsplit(" ")
        fjalia=""
        i=len(merr)
        for fjala in range(1,i):
            fjalia=fjalia+merr[fjala]          
            if(fjala!=i):
                fjalia+=" "
        if not data:
            break
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
            data="Jane gjeneruar keta numra: "+loja()
        elif(merr[0]=="FIBONACCI"):
            try:
                fjalia=int(merr[1])                
            except Exception:
                break
            data="Fibonacci: "+str(fibonacci(fjalia))                           
        elif(merr[0]=="KONVERTO"):
            try:
                numri=float(merr[2])                
            except socket.error:
                break
            data="Vlera e konvertuar: "+str(konverto(merr[1], numri))       
        
        else:
            data="The server can't respond to this request!"
        conn.send(data.encode())
    conn.close()
    


while 1:
    connection, address=serverSocket.accept()
    print("In server is now connected:"+str(address))
    start_new_thread(clientthread,(connection,))

serverSocket.close()
