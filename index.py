"""
Desenvolvido por Eros Eloy.
4 de fevereiro 2021.

Deteção de rosto em drone da DJI TELLO 
"""

import cv2
import threading 
import dji as drone

#IP do Drone
ipDrone = ('192.168.10.1', 8889)

#Thread das respostas do drone
recvThread = threading.Thread(target=drone.resposta)
recvThread.start()

#Iniciar Ligação com drone
drone.enviar('command',ipDrone)

#Pedir transmissão de video para a porta 11111
drone.enviar('streamon',ipDrone)

#OPENCV E MODELO
cap = cv2.VideoCapture('udp://192.168.10.1:11111')
modelo = cv2.CascadeClassifier('modelo.xml')

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = modelo.detectMultiScale(gray, 1.3, 5)
	

	for (x,y,w,h) in faces:

		img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		
	cv2.imshow('Video Do Drone', frame)

	key = cv2.waitKey(1)

	if key == 27:
		break
