import requests
import logging
import threading
import time
import socket
import sys
import getopt
import signal
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8888	# Arbitrary non-privileged port # Port to listen on (non-privileged ports are > 1023)

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
#https://v6.exchangerate-api.com/v6/64476c34684aa8f913d634c9/pair/USD/PHP

def loginfo(message, function_name):
	logging.info('function=%s thread_id=%s:' + message, function_name, threading.get_ident())

def logdebug(message, function_name):
	logging.debug('function=%s thread_id=%s:' + message, function_name, threading.get_ident())

def logerror(message, function_name):
	logging.error('function=%s thread_id=%s:' + message, function_name, threading.get_ident())

def logfatal(message, function_name):
	logging.fatal('function=%s thread_id=%s:' + message, function_name, threading.get_ident())

def logcritical(message, function_name):
	logging.critical('function=%s thread_id=%s:' + message, function_name, threading.get_ident())

def get_conversion_rate(response_data):
	data = str(response_data)
	keyword_conversion = 'conversion_rate'
	slen = len(keyword_conversion)
	start_index = response_data.find(keyword_conversion)
	extra_len = 9 # additional len to get the actual conversion rate
	extracted_str = response_data[start_index:start_index+slen+extra_len]
	word_list = extracted_str.split(':')
	conversion_rate = word_list[1]
	return conversion_rate


def construct_http_get_request(base_code, target_code):
	# misc
	pair = 'pair'
	separator = '/'
	#base url exchange rate api
	base_url = 'https://v6.exchangerate-api.com'
	# version of endpoint api
	version = 'v6'
	# access key generated after you registered
	access_key = '64476c34684aa8f913d634c9'

	formed_request = base_url + separator + version + separator + access_key + separator + pair + separator + base_code + separator + target_code
	loginfo('API Request = ' + formed_request, construct_http_get_request.__name__)
	return formed_request


# send a request
# example request_api = construct_http_get_request('USD', 'PHP')
def send_request_api(base_code, target_code):
	request_api = construct_http_get_request(base_code, target_code)
	try:
		response = requests.get(request_api)
		response_data = response.text
	except requests.exceptions.RequestException as err:
		raise SystemExit(err)
	#loginfo('Received response from Endpoint API = ' + data, send_request_api.__name__)
	return response_data

#get conversion rate from response json data
def get_conversion_rate(response_data):
	data = str(response_data)
	keyword_conversion = 'conversion_rate'
	slen = len(keyword_conversion)
	start_index = data.find(keyword_conversion)
	extra_len = 9 #additional len to get the actual conversion rate
	extracted_str = data[start_index:start_index + slen + extra_len]
	word_list = extracted_str.split(':')
	conversion_rate = word_list[1]
	result = float(conversion_rate)
	loginfo('Conversion Rate = '+ str(result), get_conversion_rate.__name__)
	return result

# get calculated converted amount
def calculate_conversion(base_amount, target_rate_amount):
	converted_amount = base_amount * target_rate_amount
	return converted_amount

class Processor:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		loginfo('Socket created',Processor.__name__)	
		#bind socket to local host and port
		try:
			self.server_socket.bind((self.host, self.port))
		except self.server_socket.error as msg:
			logerror('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1], Processor.__name__)
			sys.exit()

	def start_listening(self):
		self.server_socket.listen(10)
		loginfo('Socket now listening', Processor.start_listening.__name__)
	
	def process_request(self):
		keep_listening = True
		while keep_listening:
			#wait to accept a connection - blocking call
			conn, addr = self.server_socket.accept()
			client_address = addr[0]
			client_port = str(addr[1])
			loginfo('Connected with ' + client_address + ':' + client_port, Processor.process_request.__name__)
			request_data = conn.recv(1024)
			request = str(request_data.decode())
			request_list = request.split('/')
			amount = request_list[0]
			base_code = request_list[1]
			target_code = request_list[2]
			loginfo('amount=' + amount + ' base_code=' + base_code + ' target_code=' + target_code, Processor.process_request.__name__)
			converted_amount = self.process(float(amount), base_code, target_code)
			response_data = str(converted_amount) + target_code
			loginfo('sending response=' + response_data + ' to ' + client_address + ':' + client_port, Processor.process_request.__name__)
			conn.send(response_data.encode())

		self.server_socket.close()

	def process(self, amount, base_code, target_code):
		response = send_request_api(base_code, target_code)
		rate = get_conversion_rate(response)
		converted_amount = calculate_conversion(amount, rate)
		format_amount = "{:.2f}".format(converted_amount)
		loginfo('converted_amount=' + str(format_amount), Processor.process.__name__)
		return format_amount

	def close_server_socket(self):
		self.server_socket.close()

def main(argv):
	host = HOST	# default host
	port = PORT	# default port
	try:
		opts, args = getopt.getopt(argv,"hp:",["port="])
	except getopt.GetoptError:
		print('backend.py -p <port>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('backend.py -p <port>')
			sys.exit()
		elif opt in ("-p", "--port"):
			port = int(arg)

	try:
		instance = Processor(host, port)
		instance.start_listening()
		instance.process_request()
	except KeyboardInterrupt:	#  handle keyboard interupt and close socket
		instance.close_server_socket()
		logerror('Interrupted', __name__)
		try:
			sys.exit(0)
		except SystemExit:
			instance.close_server_socket()
			os._exit(0)

if __name__== "__main__" :
	main(sys.argv[1:])