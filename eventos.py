import pygame
from pygame.locals import *
from clases import *
from herramientas import *

#Zoom en la imagen

def Zoom (programa, pos, Aum) :

	#Variables

	posicion = programa.Proyec.posicion
	Tam = programa.Proyec.Tam
	Borde = programa.Proyec.Borde
	Imagen = programa.Proyec.Imagenes[programa.Imag]

	Aumento = 1
	if Tam > 20 :
		Aumento = 3
	if Tam > 50 :
		Aumento = 5
	if Tam > 80 :
		Aumento = 7

	dimensionIm = dimensionesImagen(Imagen) 
	if dimensionIm[0] == 0 or dimensionIm[1] == 0 :
		return None
	dimension0 = [dimensionIm[0] * (Tam + Borde), dimensionIm[1] * (Tam + Borde)] #dimension inicial


	if Aum == 1 :

		Tam += Aumento

	if Aum == -1 :

		if Tam > 1 :

			Tam -= Aumento

	dimension1 = [dimensionIm[0] * (Tam + Borde), dimensionIm[1] * (Tam + Borde)] #dimension final
	dif = [dimension1[0] - dimension0[0], dimension1[1] - dimension0[1]] #Diferencia de dimensiones inicial y final
	por = [(pos[0] - posicion[0]) / dimension0[0], (pos[1] - posicion[1]) / dimension1[1]] #Proporcion posicion dimension inicial y final

	posicion = PosicionZoom(posicion, dif, por)

	return [posicion, Tam]

#Calculo de la posicion de la nueva imagen

def PosicionZoom (posicion, dif, por) :

	posicion[0] -= int(dif[0] * por[0])
	posicion[1] -= int(dif[1] * por[1])

	return posicion

#Mover imagen

def Mover (programa, difRaton) :

	#Variables

	posicion = [0,0]

	dimensionImagen = dimensionesImagen(programa.Proyec.Imagenes[programa.Imag])
	ancho = dimensionImagen[0] * (programa.Proyec.Tam + programa.Proyec.Borde)
	alto = dimensionImagen[1] * (programa.Proyec.Tam + programa.Proyec.Borde)

	pos = pygame.mouse.get_pos()

	posicion[0] = pos[0] - difRaton[0]
	posicion[1] = pos[1] - difRaton[1]

	return posicion

#Pintar cuadro

def Pincel (programa, seleccion, BLOC, FON, Color) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Selec = seleccion.Selec

	cuadro = PixelTocado(programa, pygame.mouse.get_pos()) #Cuadro Tocado

	if cuadro == None : #No toca ningun cuadro
		return None

	if BLOC :
		if Imagen[cuadro[0]][cuadro[1]] != FON :
			return None

	if Selec : #Si hay alguna seleccion
		if not seleccion.Seleccionado(cuadro) :
			return None

	if Imagen[cuadro[0]][cuadro[1]] == Color : #Si ya tiene el mismo color
		return None

	Imagen[cuadro[0]][cuadro[1]] = Color #Cambio de color al cuadro

	return Imagen

#Recoger el color del cuadro tocado

def CogerColor (programa) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]

	cuadro = PixelTocado(programa, pygame.mouse.get_pos()) #Cuadro tocado

	if not cuadro : #No toca ningun cuadro
		return None

	return Imagen[cuadro[0]][cuadro[1]]

#Bote de pintura

def Pintura (programa, seleccion, BLOC, FON, Color) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Selec = seleccion.Selec

	cuadro = PixelTocado(programa, pygame.mouse.get_pos()) #Pixel tocado

	if not cuadro : #No toca ningun cuadro
		return None

	if BLOC :
		if Imagen[cuadro[0]][cuadro[1]] != FON :
			return None

	if Selec : #Si existe una seleccion
		if not seleccion.Seleccionado(cuadro) :
			return None

	if Imagen[cuadro[0]][cuadro[1]] == Color : #Si tiene el mismo color
		return None

	color = Imagen[cuadro[0]][cuadro[1]] #Color del cuadro tocado

	dimensiones = dimensionesImagen(Imagen)
	ancho = dimensiones[0]
	alto = dimensiones[1]

	matriz = []

	#Creamos matriz

	#Inicializamos con 1 los que tengan ese color y 0 con los que no

	for i in range(ancho) :
		fila = []
		fila.clear()
		for j in range(alto) :
			if Imagen[i][j] == color :
				fila.append(1) #Mismo color
			else :
				fila.append(0) #Distinto color
		matriz.append(fila)

	#Colocamos dos en los cuadros afectados

	matriz[cuadro[0]][cuadro[1]] = 2

	salir = False

	while not salir :

		salir = True

		for i in range(ancho) :
			for j in range(alto) :
				if Selec : #Existe una seleccion
					if not seleccion.Seleccionado((i,j)) : #No está en esa selección
						continue
				if matriz[i][j] == 1 :
					for a in range(-1,2,1) :
						for b in range(-1,2,1) :
							x = i + a
							y = j + b
							if a == 0 and b == 0 :
								continue
							if x < 0 or x > ancho - 1 :
								continue
							if y < 0 or y > alto - 1 :
								continue
							if matriz[x][y] == 2 :
								matriz[i][j] = 2 
								salir = False

	for i in range(ancho) :
		for j in range(alto) :
			if matriz[i][j] == 2 :
				Imagen[i][j] = Color

	return Imagen

#Calcula el cuadro de la imagen tocada

def PixelTocado (programa, pos) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	posicion = programa.Proyec.posicion
	Tam = programa.Proyec.Tam
	Borde = programa.Proyec.Borde
	#pos = pygame.mouse.get_pos()
	cuadro = [0,0]
	encontrado = False

	for i in range(len(Imagen)) :

		for j in range(len(Imagen[i])) :

			#Propiedades cuadro

			posx = i * (Tam + Borde) + posicion[0]
			posy = j * (Tam + Borde) + posicion[1]
			ancho = Tam
			alto = Tam

			if colisionRecuadro((ancho, alto), (posx, posy), pos) : #Toca cuadro

				encontrado = True
				cuadro[0] = i
				cuadro[1] = j
				break

		if encontrado :

			break

	if encontrado :

		return cuadro

	else :

		return None

#Borrar cuadro que está en la seleccion

def BorrarSelec (programa, seleccion, FON) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Selec = seleccion.Selec

	dimensiones = dimensionesImagen(Imagen)
	ancho = dimensiones[0]
	alto = dimensiones[1]

	if not Selec : #No existe una selección
		return None

	for i in range(ancho) :
		for j in range(alto) :
			if seleccion.Seleccionado((i,j)) : #El cuadro pertenece a la selección
				Imagen[i][j] = FON

	return Imagen

#Copia una selección

def Copiar (programa, seleccion) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Selec = seleccion.Selec

	dimensiones = dimensionesImagen(Imagen)
	ancho = dimensiones[0]
	alto = dimensiones[1]

	matriz = []

	if not Selec : #No existe una selección
		return None

	for i in range(ancho) :
		fila = []
		fila.clear()
		for j in range(alto) :
			if seleccion.Seleccionado((i,j)) :
				fila.append(Imagen[i][j])
		if len(fila) > 0 :
			matriz.append(fila)


	return (matriz)

#Pegar en selección

def Pegar (programa, seleccion, matriz, FON) :

	#Variables

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Selec = seleccion.Selec
	pos = [0,0]

	dimensiones = dimensionesImagen(Imagen)
	ancho = dimensiones[0]
	alto = dimensiones[1]

	if not matriz : #No existe una copia
		return None

	difx = abs(seleccion.pos0[0] - seleccion.pos1[0]) + 1 #Ancho copia
	dify = abs(seleccion.pos0[1] - seleccion.pos1[1]) + 1 #Alto copia

	if not Selec : #No existe una selección
		return None

	enc = False
	for i in range(ancho) :
		for j in range(alto) :
			if seleccion.Seleccionado((i,j)) : #Cuadro pertenece a la selección
				pos = [i,j] #Posicion de inicio
				enc = True
				break
		if enc :
			break

	if len(matriz) < difx :
		ancho = len(matriz)
	else :
		ancho = difx
	if len(matriz[0]) < dify :
		alto = len(matriz[0])
	else :
		alto = dify

	for i in range(ancho) : 
		for j in range(alto) :
			x = pos[0] + i
			y = pos[1] + j
			if matriz[i][j] == FON : #Pertenece al fondo
				continue
			Imagen[x][y] = matriz[i][j]

	return Imagen

def EspejoVer (programa, seleccion, FON) :

	Imagen = programa.Proyec.Imagenes[programa.Imag]

	if seleccion.Selec :

		matriz = Copiar(programa, seleccion)
		matriz.reverse()
		BorrarSelec(programa, seleccion, FON)
		Pegar(programa, seleccion, matriz, FON)

	else :

		Imagen.reverse()

	return Imagen

def EspejoHor (programa, seleccion, FON) :

	Imagen = programa.Proyec.Imagenes[programa.Imag]

	if seleccion.Selec :

		matriz = Copiar(programa, seleccion)
		for i in range(len(matriz)) :
			matriz[i].reverse()
		BorrarSelec(programa, seleccion, FON)
		Pegar(programa, seleccion, matriz, FON)

	else :

		for i in range(len(Imagen)) :

			Imagen[i].reverse()

	return Imagen

def MoverSeleccion (programa, seleccion, Raton0) :

	pass

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	Selec = seleccion.Selec
	pos0 = seleccion.pos0
	pos1 = seleccion.pos1

	if not Selec :
		return None

	cuadro = PixelTocado(programa, pygame.mouse.get_pos())

	if not cuadro :
		return None

	dimensiones = dimensionesImagen(Imagen)

	ancho = abs(pos0[0] - pos1[0])
	alto = abs(pos0[1] - pos1[1])

	x = None
	y = None

	if cuadro[0] - Raton0[0] < 0 :
		return None
	elif cuadro[0] - Raton0[0] + ancho > dimensiones[0] - 1 :
		return None
	elif cuadro[1] - Raton0[1] < 0 :
		return None
	elif cuadro[1] - Raton0[1] + alto > dimensiones[1] - 1 :
		return None
 
	if pos0[0] <= pos1[0] :
		if pos0[1] <= pos1[1] :
			pos0[0] = cuadro[0] - Raton0[0]
			pos0[1] = cuadro[1] - Raton0[1]
			pos1[0] = cuadro[0] - Raton0[0] + ancho
			pos1[1] = cuadro[1] - Raton0[1] + alto
		else :
			pos0[0] = cuadro[0] - Raton0[0]
			pos1[1] = cuadro[1] - Raton0[1]
			pos1[0] = cuadro[0] - Raton0[0] + ancho
			pos0[1] = cuadro[1] - Raton0[1] + alto
	else :
		if pos0[1] <= pos1[0] :
			pos1[0] = cuadro[0] - Raton0[0]
			pos0[1] = cuadro[1] - Raton0[1]
			pos0[0] = cuadro[0] - Raton0[0] + ancho
			pos1[1] = cuadro[1] - Raton0[1] + alto
		else :
			pos1[0] = cuadro[0] - Raton0[0]
			pos1[1] = cuadro[1] - Raton0[1]
			pos0[0] = cuadro[0] - Raton0[0] + ancho
			pos0[1] = cuadro[1] - Raton0[1] + alto

	return (pos0, pos1)



	

