import socket

port1 = 6000

s = socket.socket()          
print ("Servidor iniciado")

s.bind(('', port1))         
print ("Puerto del servidor %s" %(port1))
  
s.listen(5)      
print ("Servidor escuchando..")
lista_robot = []
while True: 
   c, addr = s.accept()      
   print ('Robot conectado', addr)
   print (c.recv(1024))
   lista_robot.append(c)
   c.sendall(b'Identifiquese robot!')
   c.close()
   print("Robot desconectado")