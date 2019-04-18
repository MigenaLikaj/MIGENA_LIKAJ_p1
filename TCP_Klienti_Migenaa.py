import socket
import sys
import io

host='localhost'
port=12000

socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketClient.connect((host,port))
print("------------------------TCP KLIENTI-------------------------------------")
print("Zgjedhni nje metode: \nIPADDR\nPORTNR\nHOST\nBASHTINGELLORE (+shkruaj nje fjale-fjali)\nSYPRINA(e katrorit) (+nje NUMER)\nABS (+nje NUMER)\nPRINTO (+shkruaj nje fjale/fjali)\nTIME\nLOJA\nFIBONACCI (nr>2)\nKONVERTO [(KilowattToHorsepower,\nHorsepowerToKilowatt,\nDegreesToRadians,\n RadiansToDegrees,\nGallonsToLiters,\nLitersToGallons]")

print("-------------------------------------------------------------------------")
message=input("Zgjedhni nje komande>>> ")
while(message!='Q' and (message !="")):
        socketClient.send(message.encode())                
        data=socketClient.recv(128).decode()
        '''
        if not data:
            print("Kjo mundesi nuk ekziston")
            message=input("Zgjedhni nje komande >>> ")
            continue
        '''
        print(data)
        message=input("Zgjedhni nje komande >>> ")

socketClient.close();
