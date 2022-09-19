import pygame, time
from pygame.locals import *
from PIL import Image
from clases import *
from dibujar import *
from imag import *
from herramientas import *

def DimensionesImag (title, dim) :

	Ancho = 500
	Alto = 300
	Color = pygame.Color(30,30,30)

	Numero = 0
	status = 0

	dimensiones = [0,0]

	vent = pygame.display.set_mode((Ancho, Alto))
	pygame.display.set_caption(title)

	pygame.display.init()
	vent.fill(Color)
	pygame.display.update()

	fin = False

	#Texto

	font = pygame.font.Font(None, 50)
	texto = "A N C H O"
	posX = Ancho / 2 - 80
	posY = 30
	color = pygame.Color(255,0,0)
	TextoTitulo = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 120)
	texto = dim[0][0]
	posX = 80
	posY = 90
	color = pygame.Color(255,255,255)
	TextoNum1 = Texto(None, texto, font, (posX, posY), color)
	TextoNum1.Dim = [45, 70]

	font = pygame.font.Font(None, 120)
	texto = dim[0][1]
	posX = 180
	posY = 90
	color = pygame.Color(255,255,255)
	TextoNum2 = Texto(None, texto, font, (posX, posY), color)
	TextoNum2.Dim = [45, 70]

	font = pygame.font.Font(None, 120)
	texto = dim[0][2]
	posX = 280
	posY = 90
	color = pygame.Color(255,255,255)
	TextoNum3 = Texto(None, texto, font, (posX, posY), color)
	TextoNum3.Dim = [45, 70]

	font = pygame.font.Font(None, 120)
	texto = dim[0][3]
	posX = 380
	posY = 90
	color = pygame.Color(255,255,255)
	TextoNum4 = Texto(None, texto, font, (posX, posY), color)
	TextoNum4.Dim = [45, 70]	

	font = pygame.font.Font(None, 30)
	texto = "-- Presiona ENTER para continuar --"
	posX = 70
	posY = Alto - 80
	color = pygame.Color(255,255,255)
	TextoInfo1 = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 25)
	texto = "-- Presiona ESC para cancelar --"
	posX = 100
	posY = Alto - 40
	color = pygame.Color(255,255,255)
	TextoInfo2 = Texto(None, texto, font, (posX, posY), color)

	while not fin :

		for evento in pygame.event.get() :

			if evento.type == QUIT :

				return None

			if evento.type == pygame.MOUSEBUTTONDOWN :

				if evento.button == 1 :

					if TextoNum1.PulsarTexto(pygame.mouse.get_pos()) :

						Numero = 1
						TextoNum1.Color = pygame.Color(255,255,0)
						TextoNum2.Color = pygame.Color(255,255,255)
						TextoNum3.Color = pygame.Color(255,255,255)
						TextoNum4.Color = pygame.Color(255,255,255)

					elif TextoNum2.PulsarTexto(pygame.mouse.get_pos()) :

						Numero = 2
						TextoNum2.Color = pygame.Color(255,255,0)
						TextoNum1.Color = pygame.Color(255,255,255)
						TextoNum3.Color = pygame.Color(255,255,255)
						TextoNum4.Color = pygame.Color(255,255,255)

					elif TextoNum3.PulsarTexto(pygame.mouse.get_pos()) :

						Numero = 3
						TextoNum3.Color = pygame.Color(255,255,0)
						TextoNum1.Color = pygame.Color(255,255,255)
						TextoNum2.Color = pygame.Color(255,255,255)
						TextoNum4.Color = pygame.Color(255,255,255)

					elif TextoNum4.PulsarTexto(pygame.mouse.get_pos()) :

						Numero = 4
						TextoNum4.Color = pygame.Color(255,255,0)
						TextoNum1.Color = pygame.Color(255,255,255)
						TextoNum2.Color = pygame.Color(255,255,255)
						TextoNum3.Color = pygame.Color(255,255,255)

			if evento.type == pygame.KEYDOWN :

				key = evento.key

				if key == K_RETURN or key == K_KP_ENTER :

					if status == 0 :

						letra = TextoNum1.texto + TextoNum2.texto + TextoNum3.texto + TextoNum4.texto
						print(letra)
						dimensiones[0] = int(letra)

						if dimensiones[0] <= 0 :
							continue 

						status = 1
						Numero = 0
						TextoNum1.Color = pygame.Color(255,255,255)
						TextoNum2.Color = pygame.Color(255,255,255)
						TextoNum3.Color = pygame.Color(255,255,255)
						TextoNum4.Color = pygame.Color(255,255,255)
						TextoNum1.texto = dim[1][0]
						TextoNum2.texto = dim[1][1]
						TextoNum3.texto = dim[1][2]
						TextoNum4.texto = dim[1][3]
						TextoTitulo.texto = "A L T O"
						TextoTitulo.Pos = [TextoTitulo.Pos[0] + 20, TextoTitulo.Pos[1]]

					elif status == 1 :

						letra = TextoNum1.texto + TextoNum2.texto + TextoNum3.texto + TextoNum4.texto
						print(letra)
						dimensiones[1] = int(letra)

						if dimensiones[1] <= 0 :
							continue

						return dimensiones

				if key == K_ESCAPE :

					return None

				if key == K_0 or key == K_KP0 :
					if Numero == 1 :
						TextoNum1.texto = "0"
					elif Numero == 2 :
						TextoNum2.texto = "0"
					elif Numero == 3 :
						TextoNum3.texto = "0"
					elif Numero == 4 :
						TextoNum4.texto = "0"
				elif key == K_1 or key == K_KP1 :
					if Numero == 1 :
						TextoNum1.texto = "1"
					elif Numero == 2 :
						TextoNum2.texto = "1"
					elif Numero == 3 :
						TextoNum3.texto = "1"
					elif Numero == 4 :
						TextoNum4.texto = "1"
				elif key == K_2 or key == K_KP2 :
					if Numero == 1 :
						TextoNum1.texto = "2"
					elif Numero == 2 :
						TextoNum2.texto = "2"
					elif Numero == 3 :
						TextoNum3.texto = "2"
					elif Numero == 4 :
						TextoNum4.texto = "2"
				elif key == K_3 or key == K_KP3 :
					if Numero == 1 :
						TextoNum1.texto = "3"
					elif Numero == 2 :
						TextoNum2.texto = "3"
					elif Numero == 3 :
						TextoNum3.texto = "3"
					elif Numero == 4 :
						TextoNum4.texto = "3"
				elif key == K_4 or key == K_KP4 :
					if Numero == 1 :
						TextoNum1.texto = "4"
					elif Numero == 2 :
						TextoNum2.texto = "4"
					elif Numero == 3 :
						TextoNum3.texto = "4"
					elif Numero == 4 :
						TextoNum4.texto = "4"
				elif key == K_5 or key == K_KP5 :
					if Numero == 1 :
						TextoNum1.texto = "5"
					elif Numero == 2 :
						TextoNum2.texto = "5"
					elif Numero == 3 :
						TextoNum3.texto = "5"
					elif Numero == 4 :
						TextoNum4.texto = "5"
				elif key == K_6 or key == K_KP6 :
					if Numero == 1 :
						TextoNum1.texto = "6"
					elif Numero == 2 :
						TextoNum2.texto = "6"
					elif Numero == 3 :
						TextoNum3.texto = "6"
					elif Numero == 4 :
						TextoNum4.texto = "6"
				elif key == K_7 or key == K_KP7 :
					if Numero == 1 :
						TextoNum1.texto = "7"
					elif Numero == 2 :
						TextoNum2.texto = "7"
					elif Numero == 3 :
						TextoNum3.texto = "7"
					elif Numero == 4 :
						TextoNum4.texto = "7"
				elif key == K_8 or key == K_KP8 :
					if Numero == 1 :
						TextoNum1.texto = "8"
					elif Numero == 2 :
						TextoNum2.texto = "8"
					elif Numero == 3 :
						TextoNum3.texto = "8"
					elif Numero == 4 :
						TextoNum4.texto = "8"
				elif key == K_9 or key == K_KP9 :
					if Numero == 1 :
						TextoNum1.texto = "9"
					elif Numero == 2 :
						TextoNum2.texto = "9"
					elif Numero == 3 :
						TextoNum3.texto = "9"
					elif Numero == 4 :
						TextoNum4.texto = "9"

		vent.fill(Color)

		#Dibujar

		vent.blit(TextoTitulo.getSurface(), TextoTitulo.Pos)
		vent.blit(TextoNum1.getSurface(), TextoNum1.Pos)
		vent.blit(TextoNum2.getSurface(), TextoNum2.Pos)
		vent.blit(TextoNum3.getSurface(), TextoNum3.Pos)
		vent.blit(TextoNum4.getSurface(), TextoNum4.Pos)
		vent.blit(TextoInfo1.getSurface(), TextoInfo1.Pos)
		vent.blit(TextoInfo2.getSurface(), TextoInfo2.Pos)

		pygame.display.update()



def VentanaInformacion (info) :

	Ancho = 500
	Alto = 200
	Color = pygame.Color(30,30,30)

	vent = pygame.display.set_mode((Ancho, Alto))
	pygame.display.set_caption("Información")

	pygame.display.init()
	vent.fill(Color)
	pygame.display.update()

	font = pygame.font.Font(None, 60)
	texto = "Información"
	posX = 30
	posY = 30
	color = pygame.Color(0,255,0)
	TextoTitulo = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 30)
	texto = info
	posX = 30
	posY = 100
	color = pygame.Color(255,255,255)
	TextoInfo = Texto(None, texto, font, (posX, posY), color)	

	while True :

		for evento in pygame.event.get() :

			if evento.type == pygame.QUIT :

				return

			if evento.type == pygame.KEYDOWN :

				key = evento.key

				if key == K_RETURN or key == K_KP_ENTER or key == K_ESCAPE :

					return

			vent.fill(Color)

			#Dibujar

			vent.blit(TextoTitulo.getSurface(), TextoTitulo.Pos)
			vent.blit(TextoInfo.getSurface(), TextoInfo.Pos)

			pygame.display.update()

def DimArchivo () :

	MaxPixel = 25000

	dimensiones = DimensionesImag("Dimensiones Archivo", ("0000","0000"))

	if not dimensiones :
		return None

	if dimensiones[0] * dimensiones[1] > MaxPixel :
		VentanaInformacion("Tamaño demasiado grande.")
		return None

	return dimensiones

def DimPng (Imagen) :

	dimensiones = dimensionesImagen(Imagen)

	mult = MultImagen("Dimensiones Imagen", dimensiones, "01")

	if not mult :
		return None

	Imagen = RedimensionarImagen(Imagen, mult)

	return Imagen

def MultImagen (title, dimensiones, mult) :

	Ancho = 500
	Alto = 300
	Color = pygame.Color(30,30,30)

	Numero = 0

	vent = pygame.display.set_mode((Ancho, Alto))
	pygame.display.set_caption(title)

	pygame.display.init()
	vent.fill(Color)
	pygame.display.update()

	fin = False

	#Texto

	font = pygame.font.Font(None, 50)
	texto = "REDIMENSIONAR"
	posX = Ancho / 2 - 150
	posY = 30
	color = pygame.Color(255,0,0)
	TextoTitulo = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 80)
	texto = "X"
	posX = 160
	posY = 110
	color = pygame.Color(0,255,0)
	TextoPor = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 120)
	texto = mult[0]
	posX = 240
	posY = 90
	color = pygame.Color(255,255,255)
	TextoNum1 = Texto(None, texto, font, (posX, posY), color)
	TextoNum1.Dim = [45, 70]

	font = pygame.font.Font(None, 120)
	texto = mult[1]
	posX = 300
	posY = 90
	color = pygame.Color(255,255,255)
	TextoNum2 = Texto(None, texto, font, (posX, posY), color)
	TextoNum2.Dim = [45, 70]

	font = pygame.font.Font(None, 30)
	anch = dimensiones[0] * int(mult)
	alt = dimensiones[1] * int(mult)
	texto = str(anch) + " x " + str(alt)
	posX = 300
	posY = 180
	color = pygame.Color(255,255,0)
	TextoDim = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 30)
	texto = "-- Presiona ENTER para continuar --"
	posX = 70
	posY = Alto - 80
	color = pygame.Color(255,255,255)
	TextoInfo1 = Texto(None, texto, font, (posX, posY), color)

	font = pygame.font.Font(None, 25)
	texto = "-- Presiona ESC para cancelar --"
	posX = 100
	posY = Alto - 40
	color = pygame.Color(255,255,255)
	TextoInfo2 = Texto(None, texto, font, (posX, posY), color)

	while not fin :

		for evento in pygame.event.get() :

			if evento.type == QUIT :

				return None

			if evento.type == pygame.MOUSEBUTTONDOWN :

				if evento.button == 1 :

					if TextoNum1.PulsarTexto(pygame.mouse.get_pos()) :

						Numero = 1
						TextoNum1.Color = pygame.Color(255,255,0)
						TextoNum2.Color = pygame.Color(255,255,255)

					elif TextoNum2.PulsarTexto(pygame.mouse.get_pos()) :

						Numero = 2
						TextoNum2.Color = pygame.Color(255,255,0)
						TextoNum1.Color = pygame.Color(255,255,255)

			if evento.type == pygame.KEYDOWN :

				key = evento.key

				if key == K_RETURN or key == K_KP_ENTER :

					letra = TextoNum1.texto + TextoNum2.texto
					print(letra)
					multt = int(letra)

					if multt <= 0 :
						continue

					return multt

				if key == K_ESCAPE :

					return None

				if key == K_0 or key == K_KP0 :
					if Numero == 1 :
						TextoNum1.texto = "0"
					elif Numero == 2 :
						TextoNum2.texto = "0"
				elif key == K_1 or key == K_KP1 :
					if Numero == 1 :
						TextoNum1.texto = "1"
					elif Numero == 2 :
						TextoNum2.texto = "1"
				elif key == K_2 or key == K_KP2 :
					if Numero == 1 :
						TextoNum1.texto = "2"
					elif Numero == 2 :
						TextoNum2.texto = "2"
				elif key == K_3 or key == K_KP3 :
					if Numero == 1 :
						TextoNum1.texto = "3"
					elif Numero == 2 :
						TextoNum2.texto = "3"
				elif key == K_4 or key == K_KP4 :
					if Numero == 1 :
						TextoNum1.texto = "4"
					elif Numero == 2 :
						TextoNum2.texto = "4"
				elif key == K_5 or key == K_KP5 :
					if Numero == 1 :
						TextoNum1.texto = "5"
					elif Numero == 2 :
						TextoNum2.texto = "5"
				elif key == K_6 or key == K_KP6 :
					if Numero == 1 :
						TextoNum1.texto = "6"
					elif Numero == 2 :
						TextoNum2.texto = "6"
				elif key == K_7 or key == K_KP7 :
					if Numero == 1 :
						TextoNum1.texto = "7"
					elif Numero == 2 :
						TextoNum2.texto = "7"
				elif key == K_8 or key == K_KP8 :
					if Numero == 1 :
						TextoNum1.texto = "8"
					elif Numero == 2 :
						TextoNum2.texto = "8"
				elif key == K_9 or key == K_KP9 :
					if Numero == 1 :
						TextoNum1.texto = "9"
					elif Numero == 2 :
						TextoNum2.texto = "9"

		vent.fill(Color)

		#Dibujar

		mult = TextoNum1.texto + TextoNum2.texto
		anch = dimensiones[0] * int(mult)
		alt = dimensiones[1] * int(mult)
		TextoDim.texto = str(anch) + " x " + str(alt)

		vent.blit(TextoTitulo.getSurface(), TextoTitulo.Pos)
		vent.blit(TextoPor.getSurface(), TextoPor.Pos)
		vent.blit(TextoNum1.getSurface(), TextoNum1.Pos)
		vent.blit(TextoNum2.getSurface(), TextoNum2.Pos)
		vent.blit(TextoDim.getSurface(), TextoDim.Pos)
		vent.blit(TextoInfo1.getSurface(), TextoInfo1.Pos)
		vent.blit(TextoInfo2.getSurface(), TextoInfo2.Pos)

		pygame.display.update()



