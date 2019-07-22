import socket as so
import threading
import sys

host=''
port=1224
encodingType='utf-8'
def startSV(conn,addr):
    
        with conn:
            print('client with address {}:{} is connected!'.format(addr[0],addr[1]))
            while True:
                data=conn.recv(1024)
                if not data:
                    print('Empty String')
                    conn.sendall('empty String'.encode(encodingType))
                    break
                print('Recived:',data.decode(encodingType))
                if data.decode(encodingType)=='exit':
                    conn.sendall('Connection Closed!'.encode(encodingType))
                    print('The Connection to Client with address = {} : {} has terminated! '.format(addr[0],addr[1]))
                    break
                conn.sendall(data)
                print('Echo data to ',addr[0], ":",addr[1] )


def run():
    #Starting Server
   
    print('Server Started')
    with so.socket() as s:
        s.bind((host,port))
        s.listen(10)
        
        
        while True:
            conn,addr=s.accept()
            threading.Thread(target=startSV, args=(conn,addr),daemon=True).start()



threading.Thread(target=run,daemon=True).start()  
inp=input('Type "exit" to stop server\n')
print('Server Will Stop Now! ')
if inp=='exit':
    sys.exit(0)


