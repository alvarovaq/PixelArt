import pygame
from pygame.locals import *
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import *
from herramientas import *
from clases import *
from dibujar import *
from eventos import *


def CambiarModoVision (modoVision, programa) :

	if modoVision == 0 :
		programa.Proyec.Borde = 1
	elif modoVision == 1 :
		programa.Proyec.Borde = 0
	elif modoVision == 2 :
		programa.Proyec.Borde = 1
	elif modoVision == 3 :
		programa.Proyec.Borde = 0

	return programa

def _ZoomPlay_ (programa, pos, num) :

	vector = Zoom(programa, pos, num)

	if vector :

		programa.Proyec.Tam = vector[1]
		programa.Proyec.posicion = vector[0]

	return programa

def _MoverPlay_ (Vent, programa, difRaton) :

	#Botones del raton que están presionadas
	mouseButtons = pygame.mouse.get_pressed()

	#Mover

	if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

		if mouseButtons[0] : #Esta pulsando el click izquierdo

			posicion = Mover(programa, difRaton)

			programa.Proyec.posicion = posicion

	return programa

def IzqVentanaPlay (programa) :

	lon = len(programa.Proyec.Imagenes)
	Imag = programa.Imag

	if Imag  == 0 :

		programa.Imag = lon - 1

	else :

		programa.Imag -= 1

	return programa

def DerVentanaPlay (programa) :

	lon = len(programa.Proyec.Imagenes)
	Imag = programa.Imag

	if Imag >= lon - 1 :

		programa.Imag = 0

	else :

		programa.Imag += 1

	return programa

def ModoVisionIzq (modoVision) :

	if modoVision == 0 :

		modoVision = 3

	else :

		modoVision -= 1

	return modoVision

def ModoVisionDer (modoVision) :

	if modoVision == 3 :

		modoVision = 0

	else :

		modoVision += 1

	return modoVision

def VentanaPlay (Imagenes, FON, FonPlay) :

	#Variables

	Ancho = 1000
	Alto = 600
	Color = pygame.Color(50,50,50)
	Fon = pygame.Color(50, 50, 50, 0)
	Fondo = False
	fon = Fon
	modoVision = 3

	difRaton = [None, None]

	if FonPlay :
		Fon = FonPlay

	#Ventana

	vent = pygame.display.set_mode((Ancho, Alto))
	pygame.display.set_caption("Pixel Art")

	pygame.display.init()
	pygame.display.update()

	#Ventanas

	ancho = Ancho - 150
	alto = Alto - 75
	posX = 0
	posY = 0
	VentIm = Ventana((ancho, alto), (posX, posY))

	ancho = 150
	alto = Alto
	posX = Ancho - 150
	posY = 0
	VentHerr = Ventana((ancho, alto), (posX, posY))

	ancho = Ancho - 150
	alto = 75
	posX = 0
	posY = Alto - 75
	VentVent = Ventana((ancho, alto), (posX, posY))

	#Botones

	ancho = 30
	alto = 30
	posX = int(VentHerr.posicion[0] + 35)
	posY = int(VentHerr.posicion[1] + 180)
	imagen = pygame.image.load("Imagenes/aumentar.png")
	BotonAumentar = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

	ancho = 30
	alto = 30
	posX = int(VentHerr.posicion[0] + 95)
	posY = int(VentHerr.posicion[1] + 180)
	imagen = pygame.image.load("Imagenes/disminuir.png")
	BotonDisminuir = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

	ancho = 30
	alto = 30
	posX = int(VentHerr.posicion[0] + 100)
	posY = int(VentHerr.posicion[1] + VentHerr.dimensiones[1] - 60)
	imagen = pygame.image.load("Imagenes/Salir.png")
	BotonSalir = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

	ancho = 40
	alto = 40
	posX = VentVent.posicion[0] + 30
	posY = VentVent.posicion[1] + 15
	imagen = pygame.image.load("Imagenes/Retroceder.png")
	BotonRetroceder = Boton(VentVent, (ancho, alto), (posX, posY), imagen)

	ancho = 40
	alto = 40
	posX = VentVent.posicion[0] + 85
	posY = VentVent.posicion[1] + 15
	imagen = pygame.image.load("Imagenes/Avanzar.png")
	BotonAvanzar = Boton(VentVent, (ancho, alto), (posX, posY), imagen)


	#Texto

	font = pygame.font.SysFont("comic sans ms", 25)
	texto = "Vista"
	posX = int(VentHerr.posicion[0] + 50)
	posY = int(VentHerr.posicion[1] + 27)
	color = pygame.Color(255,255,255)
	TextoVista = Texto(VentHerr, texto, font, (posX, posY), color)

	font = pygame.font.SysFont("comic sans ms", 30)
	texto = "<"
	posX = int(VentHerr.posicion[0] + 35)
	posY = int(VentHerr.posicion[1] + 70)
	color = pygame.Color(255,255,255)
	TextoVistaIzq = Texto(VentHerr, texto, font, (posX, posY), color)
	TextoVistaIzq.Dim = [30,30]

	font = pygame.font.SysFont("comic sans ms", 30)
	texto = str(modoVision + 1)
	posX = int(VentHerr.posicion[0] + 70)
	posY = int(VentHerr.posicion[1] + 70)
	color = pygame.Color(255,0,0)
	TextoVision = Texto(VentHerr, texto, font, (posX, posY), color)

	font = pygame.font.SysFont("comic sans ms", 30)
	texto = ">"
	posX = int(VentHerr.posicion[0] + 110)
	posY = int(VentHerr.posicion[1] + 70)
	color = pygame.Color(255,255,255)
	TextoVistaDer = Texto(VentHerr, texto, font, (posX, posY), color)
	TextoVistaDer.Dim = [30,30]
	
	font = pygame.font.SysFont("comic sans ms", 25)
	texto = "Zoom"
	posX = int(VentHerr.posicion[0] + 47)
	posY = int(VentHerr.posicion[1] + 130)
	color = pygame.Color(255,255,255)
	TextoZoom = Texto(VentHerr, texto, font, (posX, posY), color)

	font = pygame.font.SysFont("comic sans ms", 25)
	texto = "Fondo"
	posX = int(VentHerr.posicion[0] + 47)
	posY = int(VentHerr.posicion[1] + 225)
	color = pygame.Color(255,255,255)
	TextoFondo = Texto(VentHerr, texto, font, (posX, posY), color)

	font = pygame.font.SysFont("comic sans ms", 25)
	texto = ""
	posX = int(VentVent.posicion[0] + 150)
	posY = int(VentVent.posicion[1] + 20)
	color = pygame.Color(255,255,255)
	TextoVentana = Texto(VentVent, texto, font, (posX, posY), color)	

	#Cápsula colores

	ancho = 100
	alto = 25
	posX = int(VentHerr.posicion[0] + 30)
	posY = int(VentHerr.posicion[1] + 275)
	color = Fon
	CapsulaFondo = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

	#Programa

	proyec = Proyecto(VentIm, None, Imagenes[0])
	proyec.Imagenes = Imagenes
	programa = Programa(proyec, 0)

	programa = CambiarModoVision(modoVision, programa)

	programa.Proyec.Tam = 20

	#Centrar imagen

	dimensiones = dimensionesImagen(programa.Proyec.Imagenes[0])
	ancho = dimensiones[0]
	alto = dimensiones[1]

	programa.Proyec.posicion[0] = VentIm.posicion[0] + VentIm.dimensiones[0] / 2 - ancho * (programa.Proyec.Tam + programa.Proyec.Borde) / 2
	programa.Proyec.posicion[1] = VentIm.posicion[1] + VentIm.dimensiones[1] / 2 - alto * (programa.Proyec.Tam + programa.Proyec.Borde) / 2

	#Bucle principal

	while True :

		#Eventos

		programa = _MoverPlay_(VentIm, programa, difRaton)

		for evento in pygame.event.get() :

			if evento.type == QUIT :

				return Fon

			if evento.type == pygame.MOUSEBUTTONDOWN :

				if evento.button == 1 : #Click izquierdo
					pos = pygame.mouse.get_pos() #Posicion del cursor
					difRaton[0] = pos[0] - programa.Proyec.posicion[0]
					difRaton[1] = pos[1] - programa.Proyec.posicion[1]
				if evento.button == 4 : #Ruleta hacia adelante
					if colisionRecuadro(VentIm.dimensiones, VentIm.posicion, pygame.mouse.get_pos()) :	#Si el cursor está dentro de la ventana
						programa = _ZoomPlay_(programa, pygame.mouse.get_pos(), 1)
				if evento.button == 5 : #Ruleta hacia atras
					if colisionRecuadro(VentIm.dimensiones, VentIm.posicion, pygame.mouse.get_pos()) :	#Si el cursor está dentro de la ventana
						programa = _ZoomPlay_(programa, pygame.mouse.get_pos(),-1)

			elif evento.type == KEYDOWN :

				key = evento.key

				if key == K_ESCAPE :

					return Fon

				elif key == K_UP :

					programa = _ZoomPlay_(programa, (VentIm.posicion[0] + VentIm.dimensiones[0] / 2, VentIm.posicion[1] + VentIm.dimensiones[1] / 2), 1)

				elif key == K_DOWN :

					programa = _ZoomPlay_(programa, (VentIm.posicion[0] + VentIm.dimensiones[0] / 2, VentIm.posicion[1] + VentIm.dimensiones[1] / 2), -1)

				elif key == K_LEFT :

					programa = IzqVentanaPlay(programa)

				elif key == K_RIGHT :

					programa = DerVentanaPlay(programa)

				elif key == K_1 or key == K_KP1 :

					programa = CambiarModoVision(0, programa)
					modoVision = 0

				elif key == K_2 or key == K_KP2 :

					programa = CambiarModoVision(1, programa)
					modoVision = 1

				elif key == K_3 or key == K_KP3 :

					programa = CambiarModoVision(2, programa)
					modoVision = 2

				elif key == K_4 or key == K_KP4 :

					programa = CambiarModoVision(3, programa)
					modoVision = 3

			if evento.type == pygame.MOUSEBUTTONDOWN :

				if evento.button == 1 :

					#Botones

					if BotonDisminuir.PulsarBoton(pygame.mouse.get_pos()) :

						programa = _ZoomPlay_(programa, (VentIm.posicion[0] + VentIm.dimensiones[0] / 2, VentIm.posicion[1] + VentIm.dimensiones[1] / 2), -1)

					elif BotonAumentar.PulsarBoton(pygame.mouse.get_pos()) :

						programa = _ZoomPlay_(programa, (VentIm.posicion[0] + VentIm.dimensiones[0] / 2, VentIm.posicion[1] + VentIm.dimensiones[1] / 2), 1)

					elif BotonRetroceder.PulsarBoton(pygame.mouse.get_pos()) :

						programa = IzqVentanaPlay(programa)

					elif BotonAvanzar.PulsarBoton(pygame.mouse.get_pos()) :

						programa = DerVentanaPlay(programa)

					elif BotonSalir.PulsarBoton(pygame.mouse.get_pos()) :

						return Fon

					#Texto

					if TextoVistaIzq.PulsarTexto(pygame.mouse.get_pos()) :

						modoVision = ModoVisionIzq(modoVision)
						programa = CambiarModoVision(modoVision, programa)

					elif TextoVistaDer.PulsarTexto(pygame.mouse.get_pos()) :

						modoVision = ModoVisionDer(modoVision)
						programa = CambiarModoVision(modoVision, programa)

					#Capsulas

					if CapsulaFondo.PulsarCapsula(pygame.mouse.get_pos()) :

						cambiar = False
						color = Fon
						(colorcode, hexa) = askcolor(title = "Color")
						if colorcode == None :
							cambiar = False
						try:
							color = pygame.Color(int(colorcode[0]),int(colorcode[1]),int(colorcode[2]), 0)
							cambiar = True
						except:
							cambiar = False
							print("Error")
						if cambiar :
							Fon = color
							CapsulaFondo.Color = color


			vent.fill(Color)

			#Dibujar

			if modoVision == 0 or modoVision == 1 :
				Fondo = True
			else :
				Fondo = False

			#Ventanas
			dibujarVentana(vent, VentIm, Fon)
			#Proyecto
			dibujarImagen(vent, VentIm, programa, FON, Fondo)
			#Ventanas
			color = pygame.Color(0,0,0)
			dibujarBordes(vent, VentIm, color, 3)
			dibujarBordes(vent, VentHerr, color, 3)
			dibujarBordes(vent, VentVent, color, 3)
			#Botones
			dibujarBoton(vent, VentHerr, BotonDisminuir, color, 0)
			dibujarBoton(vent, VentHerr, BotonAumentar, color, 0)
			dibujarBoton(vent, VentHerr, BotonSalir, color, 0)
			dibujarBoton(vent, VentVent, BotonRetroceder, color, 0)
			dibujarBoton(vent, VentVent, BotonAvanzar, color, 0)
			#Texto
			TextoVision.texto = str(modoVision + 1)
			dibujarTexto(vent, VentHerr, TextoVista)
			dibujarTexto(vent, VentHerr, TextoVistaIzq)
			dibujarTexto(vent, VentHerr, TextoVision)
			dibujarTexto(vent, VentHerr, TextoVistaDer)
			dibujarTexto(vent, VentHerr, TextoZoom)
			dibujarTexto(vent, VentHerr, TextoFondo)
			TextoVentana.texto = str(programa.Imag + 1) + " / " + str(len(programa.Proyec.Imagenes))
			dibujarTexto(vent, VentVent, TextoVentana)
			#Capsulas
			color = pygame.Color(255,255,255)
			dibujarCapsula(vent, VentHerr, CapsulaFondo, color, 3)

			pygame.display.update()