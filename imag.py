import pygame
from PIL import Image
from pygame.locals import *
from herramientas import *

def GuardarImagen (Imagen, ruta) :

	img = CargarImagen(Imagen)

	img.show()
	img.save(ruta)
	img.close()

def CargarImagen (Imagen) :

	dimensiones = dimensionesImagen(Imagen)

	img = Image.new(mode = "RGBA", size = dimensiones)
	pixelsNew = img.load()

	for i in range(dimensiones[0]) :
		for j in range(dimensiones[1]) :
			pixelsNew[i,j] = Imagen[i][j]

	return img

def PygameColor (Imagen, FON) :

	Img = []
	dimensiones = dimensionesImagen(Imagen)

	for i in range(dimensiones[0]) :
		fila = []
		fila.clear()
		for j in range(dimensiones[1]) :
			color = Imagen[i][j]
			if color == FON :
				fila.append((0,0,0,0))
				continue
			fila.append((color[0], color[1], color[2], color[3]))
		Img.append(fila)

	return Img

def RedimensionarImagen (Imagen, num) :

	Img = []
	dimensiones = dimensionesImagen(Imagen)

	for i in range(dimensiones[0]) :
		fila = []
		fila.clear()
		for j in range(dimensiones[1]) :
			for k in range(num) :
				fila.append(Imagen[i][j])
		for k in range(num) :
			Img.append(fila)

	return Img