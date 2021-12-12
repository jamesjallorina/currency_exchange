import socket
import sys
import signal
import os
import getopt

LOCALHOST = '127.0.0.1'
PORT = 8888  # socket server port number

def client_program(host, port):
	sample_request = '100.5/USD/PHP'
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
	client_socket.connect((host, port))  # connect to the server

    #while message.lower().strip() != 'bye':
	client_socket.send(sample_request.encode())  # send message
	data = client_socket.recv(1024)
	print('data received: ' + data.decode())
	client_socket.close()  # close the connection

def main(argv):
	host = LOCALHOST
	port = PORT
	try:
		opts, args = getopt.getopt(argv,"hi:p:",["ip=", "port="])
	except getopt.GetoptError:
		print('backend.py -i <ip_address> -p <port>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('backend.py -i <ip_address> -p <port>')
			sys.exit()
		elif opt in ("-i", "--ip"):
			host = arg
		elif opt in ("-p", "--port"):
			port = int(arg)
	client_program(host, port)

if __name__ == '__main__':
    main(sys.argv[1:])