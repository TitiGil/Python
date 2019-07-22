import socket

s=socket.socket()
s.connect(('localhost',1224))
while True:
    outData=input('insert data:')
    if outData=='':
        continue
    
    if outData=='exit':
        s.sendall('exit'.encode('utf8'))
        data=s.recv(1024)
        print('recievd',data.decode('utf-8'))
        break
    s.sendall(outData.encode('utf-8'))
    data=s.recv(1024)
    print('recievd',data.decode('utf-8'))   
s.close()
