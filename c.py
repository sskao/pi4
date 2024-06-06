import socket
import datetime

HOST = '192.168.1.115'
PORT = 1115

while 1:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))        
        while True:    
            data = s.recv(1024).decode()    
            data = float(data)    
            print (f'Form Server Recv Data : {data} ')
            s.send("ACK!".encode())             
    except Exception as e:
        f = open("./log.txt","a+")
        t=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S ")
        f.write(t+str(e)+"\n")				
        f.close()
        s.close()
        print(e)        
        pass 
