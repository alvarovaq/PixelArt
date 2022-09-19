import pygame
from pygame.locals import *
from herramientas import *

class Programa () :

	#Constructor

	def __init__ (self, Proyec, Imag) :

		self.Proyec = Proyec
		self.Imag = Imag

	def __del__ (self) :

		pass

class Ventana () :

	#Constructor

	def __init__ (self, dimensiones, posicion) :

		self.dimensiones = dimensiones
		self.posicion = posicion

class Proyecto () :

	#Constructor

	def __init__ (self, Ventana, title, Imagen) :

		dimensiones = dimensionesImagen(Imagen)
		ancho = dimensiones[0]
		alto = dimensiones[1]

		self.title = title
		self.Tam = 40
		self.Borde = 1
		self.dTime = 0.1
		self.direccion = None
		self.Imagenes = [Imagen]
		self.posicion = [Ventana.posicion[0] + Ventana.dimensiones[0] / 2 - ancho * (self.Tam + self.Borde) / 2, Ventana.posicion[1] + Ventana.dimensiones[1] / 2 - alto * (self.Tam + self.Borde) / 2]	

	#Añade imagen de la lista

	def SumarImagen (self, Imagen, Imag) :

		if len(self.Imagenes) - 1 <= Imag :

			self.Imagenes.append(Imagen)

		else :

			self.Imagenes.append(Imagen)

			for i in range(Imag + 1,len(self.Imagenes) - 1, 1) :

				self.aux = self.Imagenes[i]
				self.Imagenes[i] = self.Imagenes[len(self.Imagenes) - 1]
				self.Imagenes[len(self.Imagenes)  - 1] = self.aux

	#Elimina imagen de la lista

	def RestarImagen(self, Imag) :

		if len(self.Imagenes) - 1 <= Imag :

			if len(self.Imagenes) > 1 :

				self.Imagenes.pop()

				return True

			else :

				return False

		else :

			for i in range(Imag, len(self.Imagenes) - 1, 1) :

				self.aux = self.Imagenes[i]
				self.Imagenes[i] = self.Imagenes[i + 1]
				self.Imagenes[i + 1] = self.aux

			self.Imagenes.pop()

			return True

class Herramientas () :

	#Constructor

	def __init__ (self, Herramienta, Color) :

		self.Herramienta = Herramienta
		self.Color = Color

class Boton () :

	#Constructor

	def __init__ (self, Ventana, dimensiones, posicion, Imagen) :

		self.Ventana = Ventana
		self.dimensiones = dimensiones
		self.posicion = posicion
		self.Imagen = Imagen

	#Comprueba si el boton es tocado

	def PulsarBoton (self, posicion) :

		if colisionRecuadro(self.dimensiones, self.posicion, posicion) :

			return True

		else :

			return False

class Texto () :

	#Constructor

	def __init__ (self, Ventana, texto, Font, Pos, Color) :

		self.Ventana = Ventana
		self.texto = texto
		self.Font = Font
		self.Pos = Pos
		self.Color = Color
		self.Dim = None

	#Devuelve surface

	def getSurface (self) :

		return self.Font.render(self.texto, False, self.Color)

	#Comprueba si el texto ha sido tocado

	def PulsarTexto (self, pos) :

		if colisionRecuadro((self.Dim[0],self.Dim[1]), self.Pos, pos) :

			return True

		else :

			return False

class CapsulaColor () :

	#Constructor

	def __init__ (self, Ventana, dimensiones, posicion, Color) :

		self.Ventana = Ventana
		self.dimensiones = dimensiones
		self.posicion = posicion
		self.Color = Color

	#Comprueba si la capsula es tocada

	def PulsarCapsula (self, posicion) :

		if colisionRecuadro(self.dimensiones, self.posicion, posicion) :

			return True

		else:

			return False

class Seleccion () :

	#Constructor

	def __init__ (self) :
		
		self.pos0 = [None, None]
		self.pos1 = [None, None]
		self.Selec = False
		self.Color = pygame.Color(255,0,255)

	#Comprueba si un cuadro pertenece a la seleccion

	def Seleccionado (self, pos) :

		if self.pos0[0] <= self.pos1[0] :
			if self.pos0[1] <= self.pos1[1] :
				if pos[0] >= self.pos0[0] and pos[0] <= self.pos1[0] : 
					if pos[1] >= self.pos0[1] and pos[1] <= self.pos1[1] :
						return True
				return False
			else :
				if pos[0] >= self.pos0[0] and pos[0] <= self.pos1[0] : 
					if pos[1] >= self.pos1[1] and pos[1] <= self.pos0[1] :
						return True
				return False
		else :
			if self.pos0[1] <= self.pos1[1] :
				if pos[0] >= self.pos1[0] and pos[0] <= self.pos0[0] : 
					if pos[1] >= self.pos0[1] and pos[1] <= self.pos1[1] :
						return True
				return False
			else :
				if pos[0] >= self.pos1[0] and pos[0] <= self.pos0[0] : 
					if pos[1] >= self.pos1[1] and pos[1] <= self.pos0[1] :
						return True
				return False

class CopiaPega () :

	#Constructor

	def __init__ (self) :

		self.Copia = []
		self.status = 0

class Historial () :

	#Constructor

	def __init__ (self) :
		
		self.Historia = []
		self.Max = 20
		self.pos = 0

	#Añade imagenes a la historia

	def SumarImagen (self, Imagenes, Imag) :

			if self.pos >= self.Max :
				self.Historia.reverse()
				self.Historia.pop()
				self.Historia.reverse()
			else :
				while len(self.Historia) > self.pos :
					self.Historia.pop()
				self.pos += 1

			self.Historia.append([Imagenes, Imag])

			print(self.pos)

	#Coger imagen

	def Get_Historia (self) :

		return self.Historia[self.pos - 1]

	#Retroceder

	def Retroceder (self) :

		if self.pos <= 1 :
			return None

		self.pos -= 1
		print(self.pos)

		res = self.Get_Historia()

		return res

	#Adelantar

	def Adelantar (self) :

		if self.pos >= self.Max :
			return None	

		if self.pos >= len(self.Historia) :
			return None

		self.pos += 1
		print(self.pos)

		res = self.Get_Historia()
		

		return res

	#Limpiamos matriz

	def Limpiar (self) :

		self.Historia.clear()
		self.pos = 0