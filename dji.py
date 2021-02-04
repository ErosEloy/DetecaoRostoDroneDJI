import socket
host = '192.168.10.2'
port = 9000
locaddr = (host,port) 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

def resposta():
	while True: 
		try:
			data, _ = sock.recvfrom(1518)
			print(data.decode(encoding="utf-8"))

		except Exception:
			print ('\nExit . . .\n')
			break


def enviar(msg,ip):


	msg = msg.encode(encoding="utf-8")
	sock.sendto(msg, ip)
