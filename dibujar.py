import pygame
from pygame.locals import *
from herramientas import *

#Dibuja el fondo de la venana

def dibujarVentana (ventana, Vent, Color) :

	pygame.draw.rect(ventana, Color, (Vent.posicion[0], Vent.posicion[1], Vent.dimensiones[0], Vent.dimensiones[1]))

#Dibujamos la imagen

def dibujarImagen (ventana, Vent, programa, FON, Fondo) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Tam = programa.Proyec.Tam
	Borde = programa.Proyec.Borde

	posicion = programa.Proyec.posicion

	dimensiones = dimensionesImagen(Imagen)
	ancho = dimensiones[0]
	alto = dimensiones[1]

	PosX = posicion[0]
	PosY = posicion[1]

	if programa.Proyec != None :
		if Imagen != None :

			contador = 0

			for x in range(ancho) : #Recorremos el ancho de la imagen

				PosY = posicion[1]

				for y in range(alto) : #Recorremos el alto de la imagen

					#Variables

					dibujar = False

					anch = Tam
					alt = Tam
					posx = PosX
					posy = PosY

					#Esquinas dentro de la ventana

					Esquinas = CuadroDentro(Vent.dimensiones, Vent.posicion, (Tam, Tam), (PosX, PosY))

					#Validamos dependiendo de las equinas

					if Esquinas == 4 : #Dentro de la ventana

						dibujar = True
						anch = Tam
						alt = Tam
						posx = PosX
						posy = PosY

					elif Esquinas > 0 :

						if colisionRecuadro((Tam, Tam), (PosX, PosY), Vent.posicion) : #Esquina superior izquierda
						
							dibujar = True
							anch = PosX + Tam - Vent.posicion[0]
							alt = PosY + Tam - Vent.posicion[1]
							posx = Vent.posicion[0]
							posy = Vent.posicion[1]

						elif colisionRecuadro((Tam, Tam), (PosX, PosY), (Vent.posicion[0] + Vent.dimensiones[0], Vent.posicion[1])) : #Esquina superior derecha
							
							dibujar = True
							anch = Vent.posicion[0] + Vent.dimensiones[0] - PosX
							alt = PosY + Tam - Vent.posicion[1]
							posx = PosX
							posy = Vent.posicion[1]

						elif colisionRecuadro((Tam, Tam), (PosX, PosY), (Vent.posicion[0], Vent.posicion[1] + Vent.dimensiones[1])) : #Esquina inferior izquierda
							
							dibujar = True
							anch = PosX + Tam - Vent.posicion[0]
							alt = Vent.posicion[1] + Vent.dimensiones[1] - PosY
							posx = Vent.posicion[0]
							posy = PosY

						elif colisionRecuadro((Tam, Tam), (PosX, PosY), (Vent.posicion[0] + Vent.dimensiones[0], Vent.posicion[1] + Vent.dimensiones[1])) : #Esquina inferior derecha
							
							dibujar = True
							anch = Vent.posicion[0] + Vent.dimensiones[0] - PosX
							alt = Vent.posicion[1] + Vent.dimensiones[1] - PosY
							posx = PosX
							posy = PosY

						elif PosY < Vent.posicion[1] and PosY + Tam > Vent.posicion[1] : #Linea superior

							dibujar = True
							anch = Tam
							alt = PosY + Tam - Vent.posicion[1]
							posx = PosX
							posy = Vent.posicion[1]

						elif PosX < Vent.posicion[0] + Vent.dimensiones[0] and PosX + Tam > Vent.posicion[0] + Vent.dimensiones[0] : #Linea derecha

							dibujar = True
							anch = Vent.posicion[0] + Vent.dimensiones[0] - PosX
							alt = Tam
							posx = PosX
							posy = PosY

						elif PosY < Vent.posicion[1] + Vent.dimensiones[1] and PosY + Tam > Vent.posicion[1] + Vent.dimensiones[1] : #Linea Inferior

							dibujar = True
							anch = Tam
							alt = Vent.posicion[1] + Vent.dimensiones[1] - PosY
							posx = PosX
							posy = PosY

						elif PosX < Vent.posicion[0] and PosX + Tam > Vent.posicion[0] : #Linea Izquierda

							dibujar = True
							anch = PosX + Tam - Vent.posicion[0]
							alt = Tam
							posx = Vent.posicion[0]
							posy = PosY

					else : #Fuera de la ventana

						dibujar = False


					if not Fondo :
						if Imagen[x][y] == FON :
							dibujar = False
 
					if dibujar :

						#Dibujamos

						pygame.draw.rect(ventana, Imagen[x][y], (posx, posy, anch, alt)) 

						if Imagen[x][y] == FON : #Si es el fondo dibujamos cruces

							dibujarFondo(ventana, programa, (x, y), (posx,posy), (anch, alt))

					contador += 1
					PosY += Borde + Tam

				PosX += Borde + Tam

#Dibujamos cruces en el fondo del dibujo

def dibujarFondo (ventana, programa, cuadro, pos, dim) :

	#Variables

	Bor = 1
	Color = pygame.Color(200,200,200)

	if programa.Proyec.Tam >= 5 : #Si los cuadros son demasiado pequeños no dibujamos

		if dim[0] == programa.Proyec.Tam and dim[1] == programa.Proyec.Tam : #Si el cuadro no esta entero no dibujamos

			#Dibujamos

			pygame.draw.line(ventana, Color, (pos[0], pos[1]), (pos[0] + dim[0], pos[1] + dim[1]), Bor)
			pygame.draw.line(ventana, Color, (pos[0] + dim[0], pos[1]), (pos[0], pos[1] + dim[1]), Bor)

		else :

			posx = programa.Proyec.posicion[0] + cuadro[0] * (programa.Proyec.Tam + programa.Proyec.Borde)
			posy = programa.Proyec.posicion[1] + cuadro[1] * (programa.Proyec.Tam + programa.Proyec.Borde)
			tam = programa.Proyec.Tam

			p1 = (0,0)
			d1 = (0,0)
			p2 = (0,0)
			d2 = (0,0)

			dibujar = False

			if posx < pos[0] and posy < pos[1] : #Esquina superior izquierda
				if dim[0] > dim[1] :
					p1 = (pos[0] + dim[0] - dim[1], pos[1])
					d1 = (dim[1], dim[1])
					p2 = (0, 0)
					d2 = (0, 0)
				elif dim[1] > dim[0] :
					p1 = (pos[0], pos[1] + dim[1] - dim[0])
					d1 = (dim[0], dim[0])
					p2 = (0, 0)
					d2 = (0, 0)
				else :
					p1 = (pos[0], pos[1])
					d1 = (dim[0], dim[1])
					p2 = (0,0)
					d2 = (0,0)
				dibujar = True
			elif posx + tam > pos[0] + dim[0] and posy < pos[1] : #Esquina superior derecha
				if dim[0] > dim[1] :
					p1 = (0,0)
					d1 = (0,0)
					p2 = (pos[0], pos[1] + dim[1])
					d2 = (dim[1], - dim[1])
				elif dim[1] > dim[0] :
					p1 = (0,0)
					d1 = (0,0)
					p2 = (pos[0], pos[1] + dim[1])
					d2 = (dim[0], - dim[0])
				else :
					p1 = (0, 0)
					d1 = (0, 0)
					p2 = (pos[0],pos[1] + dim[1])
					d2 = (dim[0],dim[1])
				dibujar = True
			elif posx + tam > pos[0] + dim[0] and posy + tam > pos[1] + dim[1] : #Esquina inferior derecha
				if dim[0] > dim[1] :
					p1 = (pos[0], pos[1])
					d1 = (dim[1], dim[1])
					p2 = (0, 0)
					d2 = (0, 0)
				elif dim[1] > dim[0] :
					p1 = (pos[0], pos[1])
					d1 = (dim[0], dim[0])
					p2 = (0, 0)
					d2 = (0, 0)
				else :
					p1 = (pos[0], pos[1])
					d1 = (dim[0], dim[1])
					p2 = (0,0)
					d2 = (0,0)
				dibujar = True
			elif posx < pos[0] and posy + tam > pos[1] + dim[1] : #Esquina inferior izquierda
				if dim[0] > dim[1] :
					p1 = (0,0)
					d1 = (0,0)
					p2 = (pos[0] + dim[0] - dim[1], pos[1] + dim[1])
					d2 = (dim[1], - dim[1])
				elif dim[1] > dim[0] :
					p1 = (0,0)
					d1 = (0,0)
					p2 = (pos[0], pos[1] + dim[0])
					d2 = (dim[0], - dim[0])
				else :
					p1 = (0, 0)
					d1 = (0, 0)
					p2 = (pos[0], pos[1] + dim[1])
					d2 = (dim[0], dim[1])
				dibujar = True
			elif posx < pos[0] : #Lado izquierdo
				p1 = (pos[0], pos[1] + dim[1] - dim[0])
				d1 = (dim[0], dim[0])
				p2 = (pos[0], pos[1] + dim[0])
				d2 = (dim[0], - dim[0])
				dibujar = True
			elif posy < pos[1] : #Lado superior
				p1 = (pos[0] + dim[0] - dim[1],pos[1])
				d1 = (dim[1], dim[1])
				p2 = (pos[0], pos[1] + dim[1])
				d2 = (dim[1], - dim[1])
				dibujar = True
			elif posx + tam > pos[0] + dim[0] : #Lado derecho
				p1 = (pos[0], pos[1])
				d1 = (dim[0], dim[0])
				p2 = (pos[0], pos[1] + dim[1])
				d2 = (dim[0], - dim[0])
				dibujar = True
			elif posy + tam > pos[1] + dim[1] : #Lado inferior
				p1 = (pos[0], pos[1])
				d1 = (dim[1], dim[1])
				p2 = (pos[0] + dim[0] - dim[1], pos[1] + dim[1])
				d2 = (dim[1], - dim[1])
				dibujar = True

			#dibujar
			if dibujar :
				pygame.draw.line(ventana, Color, p1, (p1[0] + d1[0], p1[1] + d1[1]), Bor)
				pygame.draw.line(ventana, Color, p2, (p2[0] + d2[0], p2[1] + d2[1]), Bor)

def dibujarSeleccion (ventana, Vent, programa, seleccion) :

	#Si hay una seleccion dibujamos el cuadro

	if seleccion.Selec :

		#Variables

		Color = seleccion.Color
		Bor = 3
		Imagen = programa.Proyec.Imagenes[programa.Imag]
		Tam = programa.Proyec.Tam
		Borde = programa.Proyec.Borde
		posicion = programa.Proyec.posicion

		pos0 = seleccion.pos0
		pos1 = seleccion.pos1

		pos00 = []
		pos11 = []

		linea1 = True
		linea2 = True
		linea3 = True
		linea4 = True

		#Validamos posiciones de las esquinas

		if pos0[0] <= pos1[0] :
			if pos0[1] <= pos1[1] :
				pos00 = [posicion[0] + pos0[0] * (Tam + Borde), posicion[1] + pos0[1] * (Tam + Borde)]
				pos11 = [posicion[0] + (pos1[0] + 1) * (Tam + Borde), posicion[1] + (pos1[1] + 1) * (Tam + Borde)]
				if pos00[0] < Vent.posicion[0] :
					pos00[0] = Vent.posicion[0]
					linea4 = False
					if pos11[0] < Vent.posicion[0] :
						return
				if pos11[0] > Vent.posicion[0] + Vent.dimensiones[0] :
					pos11[0] = Vent.posicion[0] + Vent.dimensiones[0]
					linea2 = False
					if pos00[0] > Vent.posicion[0] + Vent.dimensiones[0] :
						return
				if pos00[1] < Vent.posicion[1] :
					pos00[1] = Vent.posicion[1]
					linea1 = False
					if pos11[1] < Vent.posicion[1] :
						return
				if pos11[1] > Vent.posicion[1] + Vent.dimensiones[1] : 
					pos11[1] = Vent.posicion[1] + Vent.dimensiones[1]
					linea3 = False
					if pos00[1] > Vent.posicion[1] + Vent.dimensiones[1] :
						return
			else :
				pos00 = [posicion[0] + pos0[0] * (Tam + Borde), posicion[1] + (pos0[1] + 1) * (Tam + Borde)]
				pos11 = [posicion[0] + (pos1[0] + 1) * (Tam + Borde), posicion[1] + pos1[1] * (Tam + Borde)]
				if pos00[0] < Vent.posicion[0] :
					pos00[0] = Vent.posicion[0]
					linea4 = False
					if pos11[0] < Vent.posicion[0] :
						return
				if pos11[0] > Vent.posicion[0] + Vent.dimensiones[0] :
					pos11[0] = Vent.posicion[0] + Vent.dimensiones[0]
					linea2 = False
					if pos00[0] > Vent.posicion[0] + Vent.dimensiones[0] :
						return
				if pos11[1] < Vent.posicion[1] :
					pos11[1] = Vent.posicion[1]
					linea3 = False
					if pos00[1] < Vent.posicion[1] :
						return
				if pos00[1] > Vent.posicion[1] + Vent.dimensiones[1] : 
					pos00[1] = Vent.posicion[1] + Vent.dimensiones[1]
					linea1 = False
					if pos11[1] > Vent.posicion[1] + Vent.dimensiones[1] :
						return
		else :
			if pos0[1] <= pos1[1] :
				pos00 = [posicion[0] + (pos0[0] + 1) * (Tam + Borde), posicion[1] + pos0[1] * (Tam + Borde)]
				pos11 = [posicion[0] + pos1[0] * (Tam + Borde), posicion[1] + (pos1[1] + 1) * (Tam + Borde)]
				if pos11[0] < Vent.posicion[0] :
					pos11[0] = Vent.posicion[0]
					linea2 = False
					if pos00[0] < Vent.posicion[0] :
						return
				if pos00[0] > Vent.posicion[0] + Vent.dimensiones[0] :
					pos00[0] = Vent.posicion[0] + Vent.dimensiones[0]
					linea4 = False
					if pos11[0] > Vent.posicion[0] + Vent.dimensiones[0] :
						return
				if pos00[1] < Vent.posicion[1] :
					pos00[1] = Vent.posicion[1]
					linea1 = False
					if pos11[1] < Vent.posicion[1] :
						return
				if pos11[1] > Vent.posicion[1] + Vent.dimensiones[1] : 
					pos11[1] = Vent.posicion[1] + Vent.dimensiones[1]
					linea3 = False
					if pos00[1] > Vent.posicion[1] + Vent.dimensiones[1] :
						return
			else :
				pos00 = [posicion[0] + (pos0[0] + 1) * (Tam + Borde), posicion[1] + (pos0[1] + 1) * (Tam + Borde)]
				pos11 = [posicion[0] + pos1[0] * (Tam + Borde), posicion[1] + pos1[1] * (Tam + Borde)]
				if pos11[0] < Vent.posicion[0] :
					pos11[0] = Vent.posicion[0]
					linea2 = False
					if pos00[0] < Vent.posicion[0] :
						return
				if pos00[0] > Vent.posicion[0] + Vent.dimensiones[0] :
					pos00[0] = Vent.posicion[0] + Vent.dimensiones[0]
					linea4 = False
					if pos11[0] > Vent.posicion[0] + Vent.dimensiones[0] :
						return
				if pos11[1] < Vent.posicion[1] :
					pos11[1] = Vent.posicion[1]
					linea3 = False
					if pos00[1] < Vent.posicion[1] :
						return
				if pos00[1] > Vent.posicion[1] + Vent.dimensiones[1] : 
					pos00[1] = Vent.posicion[1] + Vent.dimensiones[1]
					linea1 = False
					if pos11[1] > Vent.posicion[1] + Vent.dimensiones[1] :
						return

		#Dibujamos lineas

		if linea1 :
			pygame.draw.line(ventana, Color, (pos00[0], pos00[1]), (pos11[0], pos00[1]), Bor)
		if linea2 :
			pygame.draw.line(ventana, Color, (pos11[0], pos00[1]), (pos11[0], pos11[1]), Bor)
		if linea3 :
			pygame.draw.line(ventana, Color, (pos11[0], pos11[1]), (pos00[0], pos11[1]), Bor)
		if linea4 :
			pygame.draw.line(ventana, Color, (pos00[0], pos11[1]), (pos00[0], pos00[1]), Bor)

#Dibujar bordes de la ventana

def dibujarBordes (ventana, Vent, Color, Borde) :

	#Variables

	Ancho = Vent.dimensiones[0]
	Alto = Vent.dimensiones[1]
	PosX = Vent.posicion[0]
	PosY = Vent.posicion[1]

	#Dibujamos

	pygame.draw.line(ventana, Color, (PosX, PosY), (PosX + Ancho, PosY), Borde)
	pygame.draw.line(ventana, Color, (PosX + Ancho, PosY), (PosX + Ancho, PosY + Alto), Borde)
	pygame.draw.line(ventana, Color, (PosX + Ancho, PosY + Alto), (PosX, PosY + Alto), Borde)
	pygame.draw.line(ventana, Color, (PosX, PosY + Alto), (PosX, PosY), Borde)

#Dibujar boton

def dibujarBoton (ventana, Vent, Boton, Color, Borde) :

	#Variables

	Ancho = 30
	Alto = 30
	PosX = Boton.posicion[0] + Boton.dimensiones[0] / 2 - Ancho / 2
	PosY = Boton.posicion[1] + Boton.dimensiones[1] / 2 - Alto / 2

	#Dibujamos imagen

	ventana.blit(Boton.Imagen, (PosX, PosY))

	#Dibujamos bordes

	pygame.draw.line(ventana, Color, (Boton.posicion[0], Boton.posicion[1]), (Boton.posicion[0] + Boton.dimensiones[0], Boton.posicion[1]), Borde)
	pygame.draw.line(ventana, Color, (Boton.posicion[0] + Boton.dimensiones[0], Boton.posicion[1]), (Boton.posicion[0] + Boton.dimensiones[0], Boton.posicion[1] + Boton.dimensiones[1]), Borde)
	pygame.draw.line(ventana, Color, (Boton.posicion[0] + Boton.dimensiones[0], Boton.posicion[1] + Boton.dimensiones[1]), (Boton.posicion[0], Boton.posicion[1] + Boton.dimensiones[1]), Borde)
	pygame.draw.line(ventana, Color, (Boton.posicion[0], Boton.posicion[1] + Boton.dimensiones[1]), (Boton.posicion[0], Boton.posicion[1]), Borde)

#Dibujamos capsula de color

def dibujarCapsula (ventana, Vent, Capsula, Color, Borde) :

	#Variables

	Ancho = Capsula.dimensiones[0]
	Alto = Capsula.dimensiones[1]
	PosX = Capsula.posicion[0]
	PosY = Capsula.posicion[1]
	color = Capsula.Color

	#Dibujamos color

	pygame.draw.rect(ventana, color, (PosX, PosY, Ancho, Alto))

	#Dibujamos Borde

	pygame.draw.line(ventana, Color, (Capsula.posicion[0], Capsula.posicion[1]), (Capsula.posicion[0] + Capsula.dimensiones[0], Capsula.posicion[1]), Borde)
	pygame.draw.line(ventana, Color, (Capsula.posicion[0] + Capsula.dimensiones[0], Capsula.posicion[1]), (Capsula.posicion[0] + Capsula.dimensiones[0], Capsula.posicion[1] + Capsula.dimensiones[1]), Borde)
	pygame.draw.line(ventana, Color, (Capsula.posicion[0] + Capsula.dimensiones[0], Capsula.posicion[1] + Capsula.dimensiones[1]), (Capsula.posicion[0], Capsula.posicion[1] + Capsula.dimensiones[1]), Borde)
	pygame.draw.line(ventana, Color, (Capsula.posicion[0], Capsula.posicion[1] + Capsula.dimensiones[1]), (Capsula.posicion[0], Capsula.posicion[1]), Borde)

#Dibujamos Texto

def dibujarTexto (ventana, Vent, texto) :

	#Variables

	text = texto.getSurface()

	#Dibujamos

	ventana.blit(text, texto.Pos)