import socket
import urllib.request as request

#Using Socket Lib

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
	response = mysocket.recv(512)
	if (len(response) < 1):
		break
	print(response.decode())
mysocket.close()

#Using urllib.request lib

response = request.urlopen('http://data.pr4e.org/romeo.txt')
for line in response:
	print(line.decode().strip())
