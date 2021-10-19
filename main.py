import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysocket.send(cmd)

while True:
	response = mysocket.recv(512)
	if (len(response) < 1):
		break
	print(response.decode())
mysocket.close()


