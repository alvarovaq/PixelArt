import pygame, sys, time, os, copy
from pygame.locals import *
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import *
from clases import *
from herramientas import *
from eventos import *
from archivos import *
from pyg import *
from dibujar import *
from play import *
from imag import *

pygame.init()

#Constantes
ANCHO = 1200
ALTO = 650
COLOR = pygame.Color(50,50,50)
FON = pygame.Color(255,255,255,0)
Fon = COLOR
FonPlay = None
INANCH = 30
INALT = 30

BLOC = False

#Ventana
root = Tk()
root.title("Pixel Art")
root.geometry("260x50")
root.resizable(False,False)
root.config(bg = "white")
imagen = PhotoImage(file = "Imagenes/PixelArt.png")
fondo = Label(root, image = imagen).place(x = 0, y = 0)
root.update()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pixel Art")

pygame.display.init()
pygame.display.update()

#----Variables-------------------------------------------------------------------------------------------------------

programa = Programa(None, None)

herramientas = Herramientas("Mover", 0)

seleccion = Seleccion()

copiapega = CopiaPega()

historial = Historial()

#----Funciones----------------------------------------------------------

#Inicializar imagen con una dimension y un color determinado

def initImage (dimensiones, color) :

	#Variables

	ancho = dimensiones[0]
	alto = dimensiones[1]

	imagen = []

	for x in range(ancho) :

		fila = []
		fila.clear()

		for y in range(alto) :

			fila.append(color)

		imagen.append(fila)

	return imagen

#Inicio

def mainPixelArt (Prog) :

	imagen = initImage((INANCH, INALT), FON)
	proy = Proyecto(Vent, None, imagen)
	Prog.Proyec = proy
	Prog.Imag = 0

	return Prog

#Dibujamos componentes

def dibujar () :

	Color = pygame.Color(0,0,0)
	#Proyecto
	dibujarVentana(ventana, Vent, Fon)
	dibujarImagen(ventana, Vent, programa, FON, True)
	dibujarSeleccion(ventana, Vent, programa, seleccion)
	#Ventanas
	dibujarBordes(ventana, Vent, Color, 3)
	dibujarBordes(ventana, VentHerr, Color, 3)
	dibujarBordes(ventana, VentVent, Color, 3)
	dibujarBordes(ventana, VentOp, Color, 3)
	dibujarBordes(ventana, VentMas, Color, 3)
	#Botones
	ColorNor = pygame.Color(255,255,0)
	ColorSel = pygame.Color(255,0,255)
	Color = pygame.Color(255,255,255)
	if herramientas.Herramienta == "Mover" :
		Color = ColorSel
	else:
		Color = ColorNor
	dibujarBoton(ventana, VentHerr, BotonMover, Color, 3)
	if herramientas.Herramienta == "Pincel" :
		Color = ColorSel
	else:
		Color = ColorNor
	dibujarBoton(ventana, VentHerr, BotonPincel, Color, 3)
	if herramientas.Herramienta == "Borrar" :
		Color = ColorSel
	else:
		Color = ColorNor
	dibujarBoton(ventana, VentHerr, BotonBorrar, Color, 3)
	if herramientas.Herramienta == "Pintura" :
		Color = ColorSel
	else:
		Color = ColorNor
	dibujarBoton(ventana, VentHerr, BotonPintura, Color, 3)
	if herramientas.Herramienta == "CogerColor" :
		Color = ColorSel
	else:
		Color = ColorNor
	if not BLOC :
		BotonCandado.Imagen = pygame.image.load("Imagenes/CandadoOn.png")
	else :
		BotonCandado.Imagen = pygame.image.load("Imagenes/CandadoOff.png")
	dibujarBoton(ventana, VentHerr, BotonCogerColor, Color, 3)
	if herramientas.Herramienta == "Seleccionar" :
		Color = ColorSel
	else:
		Color = ColorNor
	dibujarBoton(ventana, VentHerr, BotonSeleccionar, Color, 3)
	dibujarBoton(ventana, VentHerr, BotonCandado, Color, 0)
	Color = pygame.Color(0,0,0)
	dibujarBoton(ventana, VentVent, BotonIzq, Color, 0)
	dibujarBoton(ventana, VentVent, BotonDer, Color, 0)
	dibujarBoton(ventana, VentVent, BotonPlay, Color, 0)
	dibujarBoton(ventana, VentVent, BotonNuevaVent, Color, 0)
	dibujarBoton(ventana, VentVent, BotonEliminarVent, Color, 0)
	dibujarBoton(ventana, VentOp, BotonCrear, Color, 0)
	dibujarBoton(ventana, VentOp, BotonAbrir, Color, 0)
	dibujarBoton(ventana, VentOp, BotonGuardar, Color, 0)
	dibujarBoton(ventana, VentOp, BotonRetrasar, Color, 0)
	dibujarBoton(ventana, VentOp, BotonAdelantar, Color, 0)
	dibujarBoton(ventana, VentOp, BotonIco, Color, 0)
	dibujarBoton(ventana, VentOp, BotonCamara, Color, 0)
	dibujarBoton(ventana, VentOp, BotonOpciones, Color, 0)
	dibujarBoton(ventana, VentOp, BotonSalir, Color, 0)
	dibujarBoton(ventana, VentMas, BotonDeseleccionar, Color, 0)
	dibujarBoton(ventana, VentMas, BotonSelec, Color, 0)
	dibujarBoton(ventana, VentMas, BotonAumentar, Color, 0)
	dibujarBoton(ventana, VentMas, BotonDisminuir, Color, 0)
	dibujarBoton(ventana, VentMas, BotonCop, Color, 0)
	dibujarBoton(ventana, VentMas, BotonPeg, Color, 0)
	dibujarBoton(ventana, VentMas, BotonCor, Color, 0)
	dibujarBoton(ventana, VentMas, BotonEspejoVer, Color, 0)
	dibujarBoton(ventana, VentMas, BotonEspejoHor, Color, 0)
	#Texto
	TextoVent.texto = str(programa.Imag + 1)  + " / " + str(len(programa.Proyec.Imagenes))
	dibujarTexto(ventana, VentVent, TextoVent)
	dibujarTexto(ventana, VentMas, TextoSelec)
	dibujarTexto(ventana, VentMas, TextoZoom)
	dibujarTexto(ventana, VentMas, TextoFondo)
	dibujarTexto(ventana, VentOp, TextoIco)
	#Capsulas
	Color = pygame.Color(255,255,255)
	dibujarCapsula(ventana, VentHerr, Capsula1, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula2, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula3, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula4, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula5, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula6, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula7, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula8, Color, 3)
	dibujarCapsula(ventana, VentHerr, Capsula9, Color, 3)
	ColorNor = pygame.Color(255,255,255)
	ColorSel = pygame.Color(255,0,255)
	Color = pygame.Color(0,0,0)
	if herramientas.Color == 0 :
		Color = ColorSel
	else :
		Color = ColorNor
	dibujarCapsula(ventana, VentHerr, Color1, Color, 3)
	if herramientas.Color == 0 :
		Color = ColorNor
	else :
		Color = ColorSel
	dibujarCapsula(ventana, VentHerr, Color2, Color, 3)
	Color = pygame.Color(255,255,255)
	dibujarCapsula(ventana, VentMas, CapsulaSeleccion, Color, 3)
	dibujarCapsula(ventana, VentMas, CapsulaFondo, Color, 3)

#Eventos de las herramientas

def eventos () :

	#Eventos

	#Botones del raton que están presionadas
	mouseButtons = pygame.mouse.get_pressed()

	#Validamos dependiendo de la herramienta seleccionada

	if herramientas.Herramienta == "Mover" :

		#Mover

		if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

			if mouseButtons[0] : #Esta pulsando el click izquierdo

				posicion = Mover(programa, difRaton)

				programa.Proyec.posicion = posicion

	if herramientas.Herramienta == "Pincel" :

		#Pintar

		if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

			Pintar = False
			Color = pygame.Color(0,0,0)

			if mouseButtons[0] : #Click izquierdo

				if herramientas.Color == 0 :
					Color = Color1.Color
				else :
					Color = Color2.Color

				Pintar = True

			elif mouseButtons[2] : #Click derecho

				if herramientas.Color == 0 :
					Color = Color2.Color
				else :
					Color = Color1.Color

				Pintar = True

			if Pintar :

				imagen = Pincel(programa, seleccion, BLOC, FON, Color)

				if imagen :

					programa.Proyec.Imagenes[programa.Imag] = imagen
					SumarHistorial()

	if herramientas.Herramienta == "Borrar" :

		#Borrar

		if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

			if mouseButtons[0] : #Click izquierdo

				imagen = Pincel(programa, seleccion, FALSE, FON, FON)

				if imagen :

					programa.Proyec.Imagenes[programa.Imag] = imagen
					SumarHistorial()

	if herramientas.Herramienta == "Pintura" :

		#Pintamos

		if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

			Pintar = False
			color = pygame.Color(0,0,0)

			if mouseButtons[0] : #Click izquierdo

				if herramientas.Color == 0:
					color = Color1.Color
				else :
					color = Color2.Color

				Pintar = True

			elif mouseButtons[2] : #Click derecho

				if herramientas.Color == 0 :
					color = Color2.Color
				else :
					color = Color1.Color

				Pintar = True

			if Pintar :

				imagen = Pintura(programa, seleccion, BLOC, FON, color)

				if imagen :

					programa.Proyec.Imagenes[programa.Imag] = imagen
					SumarHistorial()

	if herramientas.Herramienta == "CogerColor" :

		#Cogemos color

		if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

			color = CogerColor(programa)

			receptor = herramientas.Color

			if mouseButtons[0] : #Click izquierdo

				if color :

					if receptor == 0 :
						Color1.Color = color
					else :
						Color2.Color = color

			elif mouseButtons[2] : #Click derecho

				if color :

					if receptor == 0 :
						Color2.Color = color
					else :
						Color1.Color = color

	if herramientas.Herramienta == "Seleccionar" :

		#Seleccionamos

		if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) : #Si el cursor está dentro de la ventana

			if seleccion.Selec :

				if mouseButtons[0] : #Click izquierdo

					cuadro = CuadroTocado(programa, pygame.mouse.get_pos())
					if cuadro :
						seleccion.pos1[0] = cuadro[0]
						seleccion.pos1[1] = cuadro[1]

				elif mouseButtons[2] : #Click derecho

					if not Raton0[0] or not Raton0[1] :
						return

					pos = MoverSeleccion(programa, seleccion, Raton0)

					if not pos :
						return

					seleccion.pos0 = pos[0]
					seleccion.pos1 = pos[1]


#Zoom de la imagen

def _Zoom_ (pos, num) :

	vector = Zoom(programa, pos, num)

	if vector :

		programa.Proyec.Tam = vector[1]
		programa.Proyec.posicion = vector[0]

#Elegir direccion para guardar archivo

def direcArchivo (title, filetypes, extension) :

	print(extension)

	#Variables

	ruta = ""
	salir = False

	#Bucle

	while not salir :

		salir = True

		#Creamos tkinter

		tk = Tk()
		tk.title("Pixel Art")
		tk.geometry("200x100")

		#Pedimos direccion

		ruta = filedialog.asksaveasfilename(title = title, initialdir = "/", filetypes = filetypes)
		
		#Cerramos tkinter

		tk.destroy()

		#Si ha cancelado

		if not ruta :
			return None

		#Verificamos la sintaxis

		ext = ruta[len(ruta) - 4:len(ruta)] #Extension
		if ext == extension : #Sintaxis correcta
			salir = True
		else :
			for i in ruta :
				if i == "." : #Sintaxis incorrecta
					salir = False
					print("Debe ser de extension " + extension)
					break
			if salir : #Corregimos sintaxis
				ruta = ruta + extension
				salir = True

	return ruta

#Crea una ventana

def CrearVentana () :

	dimensiones = dimensionesImagen(programa.Proyec.Imagenes[programa.Imag])
	programa.Proyec.SumarImagen(initImage(dimensiones, FON), programa.Imag)
	programa.Imag += 1
	SumarHistorial()

#Elimina ventana

def EliminarVentana () :

	elim = programa.Proyec.RestarImagen(programa.Imag)

	if not elim : #Solo queda uno
		return

	if len(programa.Proyec.Imagenes) - 1 > 0 :
		if programa.Imag > 0 :
			programa.Imag -= 1
	else :
		programa.Imag = 0

	SumarHistorial()

#Cambia de ventana

def DerVentana () :

	if programa.Imag < len(programa.Proyec.Imagenes) - 1 :

		programa.Imag += 1

	else :

		programa.Imag = 0

#Cambia de ventana

def IzqVentana () :

	if programa.Imag > 0 :

		programa.Imag -= 1

	else :

		programa.Imag = len(programa.Proyec.Imagenes) - 1


#Guardar imagen en el pc

def guardar () :

	#Variables

	ruta = programa.Proyec.direccion

	if not ruta : #Si nunca se ha guardado

		ruta = direcArchivo("Guardar Como...", (("Pixel Art","*.pxa"),("Todos los archivos","*.*")), ".pxa")

		if not ruta : #Ha cancelado
			return

	#Guardamos

	programa.Proyec.direccion = ruta
	GuardarArchivo(programa.Proyec, ruta)

#Guardar imagen en otro archivo

def guardarComo () :

	#Variables

	ruta = direcArchivo("Guardar Como...", (("Pixel Art","*.pxa"),("Todos los archivos","*.*")), ".pxa")

	if not ruta : #Ha cancelado
		return

	#Guardamos

	programa.Proyec.direccion = ruta
	GuardarArchivo(programa.Proyec, ruta)

#Abrimos archivo

def abrir () :

	#Creamos tkinter

	tk = Tk()
	tk.title("Pixel Art")
	tk.geometry("200x100")

	#Variables

	ruta = filedialog.askopenfilename(title = "Abrir", initialdir = "/", filetypes = (("Pixel Art","*.pxa"),("Todos los ficheros","*.*")))

	#Quitamos tkinter

	tk.destroy()

	if not ruta : #Ha cancelado
		return

	try :

		#Abrimos

		programa.Proyec.Imagenes.clear()
		programa.Proyec.Imagenes = AbrirArchivo(ruta)

		programa.Proyec.direccion = ruta

		ReiniciarProyecto(programa.Proyec.Imagenes[0])

		SumarHistorial()

		pygame.display.set_caption(ruta)

	except :

		print("No se ha podido abrir el archivo")


#Creamos Proyecto

def crear () :

	#Variables

	ancho = 0
	alto = 0

	#Dimensiones del proyecto 

	dimensiones = DimArchivo()

	#Opciones ventana

	ventana = pygame.display.set_mode((ANCHO, ALTO))
	pygame.display.set_caption("Pixel Art")

	if not dimensiones : #Si cancela
		return

	#Valores nuevo proyecto

	imagen = initImage(dimensiones,FON)
	programa.Proyec.Imagenes.clear()
	programa.Imag = 0
	programa.Proyec = Proyecto(Vent,None,imagen)
	programa.Proyec.direccion = None

	historial.Historia.clear()
	historial.pos = 0

	SumarHistorial()

	seleccion.Selec = False

#Reiniciar variables del proyecto

def ReiniciarProyecto (imagenes) :

	programa.Proyec.Tam = 40
	programa.Proyec.Borde = 1
	programa.Imag = 0

	dimensiones = dimensionesImagen(imagenes)
	ancho = dimensiones[0]
	alto = dimensiones[1]

	programa.Proyec.posicion[0] = Vent.posicion[0] + Vent.dimensiones[0] / 2 - ancho * (programa.Proyec.Tam + programa.Proyec.Borde) / 2
	programa.Proyec.posicion[1] = Vent.posicion[1] + Vent.dimensiones[1] / 2 - alto * (programa.Proyec.Tam + programa.Proyec.Borde) / 2

	historial.Limpiar()

	seleccion.Selec = False

#Borrar lo que esté seleccionado

def Borr () :

	imagen = BorrarSelec(programa, seleccion, FON)
	if imagen :
		programa.Proyec.Imagenes[programa.Imag] = imagen
		SumarHistorial()
	seleccion.Selec = False

#Copiar lo que esté seleccionado

def Cop () :

	if seleccion.Selec :

		(matriz) = Copiar(programa, seleccion)
		if matriz :
			copiapega.Copia.clear()
			copiapega.Copia = matriz
			seleccion.Selec = False

#Pegar

def Peg () :

	(imagen) = Pegar(programa, seleccion, copiapega.Copia, FON)
	if imagen :
		programa.Proyec.Imagenes[programa.Imag] = imagen
		SumarHistorial()

#Cortar lo que esté seleccionado

def Cor () :

	if seleccion.Selec :

		Cop()
		seleccion.Selec = True
		Borr()

#Añade imagenes al historial

def SumarHistorial () :

	imagenes = programa.Proyec.Imagenes
	imag = programa.Imag
	historial.SumarImagen(copy.deepcopy(imagenes), imag)

#Retrocedemos en el historial

def RetrocederHistorial () :

	his = historial.Retroceder()
	if his :
		programa.Proyec.Imagenes = copy.deepcopy(his[0])
		programa.Imag = his[1]

#Adelantamos en el historial

def AdelantarHistorial () :

	his = historial.Adelantar()
	if his :
		programa.Proyec.Imagenes = copy.deepcopy(his[0])
		programa.Imag = his[1]

def DarPlay (FonPlay) :

	FonPlay = VentanaPlay(copy.deepcopy(programa.Proyec.Imagenes), FON, FonPlay)

	ventana = pygame.display.set_mode((ANCHO, ALTO))
	if programa.Proyec.direccion :
		pygame.display.set_caption(programa.Proyec.direccion)
	else :
		pygame.display.set_caption("Pixel Art")

	return FonPlay

def _EspejoVer_ () :

	programa.Proyec.Imagenes[programa.Imag] = EspejoVer(programa, seleccion, FON)
	SumarHistorial()

def _EspejoHor_ () :

	programa.Proyec.Imagenes[programa.Imag] = EspejoHor(programa, seleccion, FON)
	SumarHistorial()

def png () :

	ruta = direcArchivo("Guardar en png...", (("PNG","*.png"),("Todos los archivos","*.*")), ".png")
	print(ruta)
	if ruta :
		imagen = programa.Proyec.Imagenes[programa.Imag]
		img = PygameColor(imagen, FON)
		img = DimPng(img)
		ventana = pygame.display.set_mode((ANCHO, ALTO))
		pygame.display.set_caption("Pixel Art")
		if img :
			GuardarImagen(img, ruta)

#-----Inicializamos Variables------------------------------------------------------------------------------------------

#Ventanas

ancho = int(3 * ANCHO / 4)
alto = int(3 * ALTO / 4)
posX = int(ANCHO / 2 - ancho / 2)
posY = int(ALTO / 2 - alto / 2)
Vent = Ventana((ancho, alto), (posX, posY))

ancho = int(ANCHO / 8)
alto = int(3 * ALTO / 4 + ALTO / 8)
posX = 0
posY = int(ALTO / 8)
VentHerr = Ventana((ancho, alto), (posX, posY))

ancho = Vent.dimensiones[0]
alto = ALTO - Vent.posicion[1] - Vent.dimensiones[1]
posX = Vent.posicion[0]
posY = Vent.posicion[1] + Vent.dimensiones[1]
VentVent = Ventana((ancho, alto), (posX, posY))

ancho = ANCHO
alto = Vent.posicion[1]
posX = 0
posY = 0
VentOp = Ventana((ancho, alto), (posX, posY))

ancho = ANCHO - Vent.posicion[0] - Vent.dimensiones[0]
alto = ALTO - Vent.posicion[1]
posX = Vent.posicion[0] + Vent.dimensiones[0]
posY = Vent.posicion[1]
VentMas = Ventana((ancho, alto), (posX, posY))

#Botones

altura = 40

ancho = int(VentHerr.dimensiones[0] / 3)
alto = int(VentHerr.dimensiones[0] / 3)
posX = int(VentHerr.posicion[0] + 20)
posY = int(VentHerr.posicion[1] + altura)
imagen = pygame.image.load("Imagenes/Mover.png")
BotonMover = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

ancho = int(VentHerr.dimensiones[0] / 3)
alto = int(VentHerr.dimensiones[0] / 3)
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] - ancho - 20)
posY = int(VentHerr.posicion[1] + altura)
imagen = pygame.image.load("Imagenes/Pincel.png")
BotonPincel = Boton(VentHerr, (ancho, alto), (posX, posY), imagen) 

ancho = int(VentHerr.dimensiones[0] / 3)
alto = int(VentHerr.dimensiones[0] / 3)
posX = int(VentHerr.posicion[0] + 20)
posY = int(VentHerr.posicion[1] + 10 + alto + altura)
imagen = pygame.image.load("Imagenes/Borrar.png")
BotonBorrar = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

ancho = int(VentHerr.dimensiones[0] / 3)
alto = int(VentHerr.dimensiones[0] / 3)
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] - ancho - 20)
posY = int(VentHerr.posicion[1] + 10 + alto + altura)
imagen = pygame.image.load("Imagenes/Pintura.png")
BotonPintura = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

ancho = int(VentHerr.dimensiones[0] / 3)
alto = int(VentHerr.dimensiones[0] / 3)
posX = int(VentHerr.posicion[0] + 20)
posY = int(VentHerr.posicion[1] + 2 * 10 + 2 * alto + altura)
imagen = pygame.image.load("Imagenes/CogerColor.png")
BotonCogerColor = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

ancho = int(VentHerr.dimensiones[0] / 3)
alto = int(VentHerr.dimensiones[0] / 3)
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] - ancho - 20)
posY = int(VentHerr.posicion[1] + 2 * 10 + 2 * alto + altura)
imagen = pygame.image.load("Imagenes/Seleccionar.png")
BotonSeleccionar = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] / 2 - ancho / 2)
posY = int(VentHerr.posicion[1] + 235)
imagen = pygame.image.load("Imagenes/CandadoOn.png")
BotonCandado = Boton(VentHerr, (ancho, alto), (posX, posY), imagen)


ancho = 30
alto = 30
posX = int(VentVent.posicion[0] + 30)
posY = int(VentVent.posicion[1] + 25)
imagen = pygame.image.load("Imagenes/Izq.png")
BotonIzq = Boton(VentVent, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentVent.posicion[0] + 2 * ancho + 30)
posY = int(VentVent.posicion[1] + 25)
imagen = pygame.image.load("Imagenes/Der.png")
BotonDer = Boton(VentVent, (ancho, alto), (posX, posY), imagen)

ancho = 40
alto = 40
posX = int(VentVent.posicion[0] + VentVent.dimensiones[0] - 230)
posY = int(VentVent.posicion[1] + 17)
imagen = pygame.image.load("Imagenes/Play.png")
BotonPlay = Boton(VentVent, (ancho, alto), (posX, posY), imagen)

ancho = 40
alto = 40
posX = int(VentVent.posicion[0] + VentVent.dimensiones[0] - 150)
posY = int(VentVent.posicion[1] + 15)
imagen = pygame.image.load("Imagenes/NuevaVent.png")
BotonNuevaVent = Boton(VentVent, (ancho, alto), (posX, posY), imagen)

ancho = 40
alto = 40
posX = int(VentVent.posicion[0] + VentVent.dimensiones[0] - 85)
posY = int(VentVent.posicion[1] + 13)
imagen = pygame.image.load("Imagenes/EliminarVent.png")
BotonEliminarVent = Boton(VentVent, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + 30)
posY = 25
imagen = pygame.image.load("Imagenes/Crear.png")
BotonCrear = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + 60 + 20)
posY = 25
imagen = pygame.image.load("Imagenes/Abrir.png")
BotonAbrir = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + 90 + 40)
posY = 25
imagen = pygame.image.load("Imagenes/Guardar.png")
BotonGuardar = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + 220)
posY = 25
imagen = pygame.image.load("Imagenes/Retrasar.png")
BotonRetrasar = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + 270)
posY = 25
imagen = pygame.image.load("Imagenes/Adelantar.png")
BotonAdelantar = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 40
alto = 40
posX = int(VentOp.posicion[0] + 450)
posY = 20
imagen = pygame.image.load("Imagenes/Ico.png")
BotonIco = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + VentOp.dimensiones[0] - 200)
posY = 25
imagen = pygame.image.load("Imagenes/Camara.png")
BotonCamara = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + VentOp.dimensiones[0] - 120)
posY = 25
imagen = pygame.image.load("Imagenes/Opciones.png")
BotonOpciones = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentOp.posicion[0] + VentOp.dimensiones[0] - 70)
posY = 25
imagen = pygame.image.load("Imagenes/Salir.png")
BotonSalir = Boton(VentOp, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 35)
posY = int(VentMas.posicion[1] + 62)
imagen = pygame.image.load("Imagenes/deseleccionar.png")
BotonDeseleccionar = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 85)
posY = int(VentMas.posicion[1] + 60)
imagen = pygame.image.load("Imagenes/seleccionar.png")
BotonSelec = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 30)
posY = int(VentMas.posicion[1] + 190)
imagen = pygame.image.load("Imagenes/aumentar.png")
BotonAumentar = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 90)
posY = int(VentMas.posicion[1] + 190)
imagen = pygame.image.load("Imagenes/disminuir.png")
BotonDisminuir = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 20)
posY = int(VentMas.posicion[1] + 390)
imagen = pygame.image.load("Imagenes/Cop.png")
BotonCop = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 100)
posY = int(VentMas.posicion[1] + 390)
imagen = pygame.image.load("Imagenes/Peg.png")
BotonPeg = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 60)
posY = int(VentMas.posicion[1] + 390)
imagen = pygame.image.load("Imagenes/Cor.png")
BotonCor = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 40)
posY = int(VentMas.posicion[1] + 330)
imagen = pygame.image.load("Imagenes/EspejoVer.png")
BotonEspejoVer = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

ancho = 30
alto = 30
posX = int(VentMas.posicion[0] + 80)
posY = int(VentMas.posicion[1] + 330)
imagen = pygame.image.load("Imagenes/EspejoHor.png")
BotonEspejoHor = Boton(VentMas, (ancho, alto), (posX, posY), imagen)

#Texto

font = pygame.font.Font(None, 30)
texto = ""
posX = int(VentVent.posicion[0] + 140)
posY = int(VentVent.posicion[1] + 30)
color = pygame.Color(255,255,255)
TextoVent = Texto(VentVent, texto, font, (posX, posY), color)

font = pygame.font.SysFont("comic sans ms", 25)
texto = "Selección"
posX = int(VentMas.posicion[0] + 20)
posY = int(VentMas.posicion[1] + 10)
color = pygame.Color(255,255,255)
TextoSelec = Texto(VentMas, texto, font, (posX, posY), color)

font = pygame.font.SysFont("comic sans ms", 25)
texto = "Zoom"
posX = int(VentMas.posicion[0] + 45)
posY = int(VentMas.posicion[1] + 145)
color = pygame.Color(255,255,255)
TextoZoom = Texto(VentMas, texto, font, (posX, posY), color)

font = pygame.font.SysFont("comic sans ms", 25)
texto = "Fondo"
posX = int(VentMas.posicion[0] + 45)
posY = int(VentMas.posicion[1] + 230)
color = pygame.Color(255,255,255)
TextoFondo = Texto(VentMas, texto, font, (posX, posY), color)

font = pygame.font.SysFont("comic sans ms", 35)
texto = "PIXEL ART"
posX = int(VentOp.posicion[0] + 520)
posY = 20
color = pygame.Color(255,255,255)
TextoIco = Texto(VentOp, texto, font, (posX, posY), color)


#Capsulas colores

altura = 375

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 20)
posY = altura
color = pygame.Color(0,200,0)
Capsula1 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 10 + ancho + 20)
posY = altura
color = pygame.Color(200,0,0)
Capsula2 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] - ancho - 20)
posY = altura
color = pygame.Color(0,0,200)
Capsula3 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 20)
posY = altura + 10 + alto
color = pygame.Color(250,250,0)
Capsula4 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 10 + ancho + 20)
posY = altura + 10 + alto
color = pygame.Color(200,0,200)
Capsula5 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] - ancho - 20)
posY = altura + 10 + alto
color = pygame.Color(0,200,200)
Capsula6 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 20)
posY = altura + 20 + 2 * alto
color = pygame.Color(50,50,50)
Capsula7 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 10 + ancho + 20)
posY = altura + 20 + 2 * alto
color = pygame.Color(255,100,0)
Capsula8 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] / 5)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + VentHerr.dimensiones[0] - ancho - 20)
posY = altura + 20 + 2 * alto
color = pygame.Color(255,255,255)
Capsula9 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] - 40)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 20)
posY = altura + 40 + 3 * alto
color = pygame.Color(50,50,50)
Color1 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentHerr.dimensiones[0] - 40)
alto = int(VentHerr.dimensiones[0] / 5)
posX = int(VentHerr.posicion[0] + 20)
posY = altura + 50 + 4 * alto
color = pygame.Color(80,250,90)
Color2 = CapsulaColor(VentHerr, (ancho, alto), (posX, posY), color)

ancho = int(VentMas.dimensiones[0] - 60)
alto = 25
posX = int(VentMas.posicion[0] + 30)
posY = int(VentMas.posicion[1] + 105)
color = seleccion.Color
CapsulaSeleccion = CapsulaColor(VentMas, (ancho, alto), (posX, posY), color)

ancho = int(VentMas.dimensiones[0] - 60)
alto = 25
posX = int(VentMas.posicion[0] + 30)
posY = int(VentMas.posicion[1] + 275)
color = Fon
CapsulaFondo = CapsulaColor(VentMas, (ancho, alto), (posX, posY), color)

#----Incio del programa---------------------------------------------------

#Variables

difRaton = [0,0]
Raton0 = [0,0]
ctrl = False
shift = False
reloj = pygame.time.Clock()

#Iniciamos proyecto

programa = mainPixelArt(programa)

SumarHistorial()

while True :

	#Eventos

	eventos()


	#Eventos
	for evento in pygame.event.get() :

		if evento.type == QUIT : #X de la ventana

			pygame.quit()
			sys.exit()

		if herramientas.Herramienta == "Mover" :

			#Obtenemos diferencia del raton con la imagen

			if evento.type == pygame.MOUSEBUTTONDOWN :
				if evento.button == 1 : #Click izquierdo
					pos = pygame.mouse.get_pos() #Posicion del cursor
					difRaton[0] = pos[0] - programa.Proyec.posicion[0]
					difRaton[1] = pos[1] - programa.Proyec.posicion[1]

				#Zoom

				if evento.button == 4 : #Ruleta hacia adelante
					if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) :	#Si el cursor está dentro de la ventana

						_Zoom_(pygame.mouse.get_pos(), 1)

				if evento.button == 5 : #Ruleta hacia atras
					if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) :	#Si el cursor está dentro de la ventana

						_Zoom_(pygame.mouse.get_pos(),-1)

		elif herramientas.Herramienta == "Seleccionar" :

			if evento.type == pygame.MOUSEBUTTONDOWN :
				if evento.button == 3 : #Click derecho

					x = None
					y = None
					
					cuadro0 = PixelTocado(programa, pygame.mouse.get_pos())
					(x, y) = PosSeleccion(seleccion)

					if cuadro0 :

						Raton0[0] = cuadro0[0] - x
						Raton0[1] = cuadro0[1] - y

					else :

						Raton0 = [None, None]



		#Atajos

		if evento.type == pygame.KEYDOWN :

			key = evento.key

			if key == K_v :

				herramientas.Herramienta = "Mover"

			elif key == K_p :

				herramientas.Herramienta = "Pincel"

			elif key == K_b :

				herramientas.Herramienta = "Borrar"

			elif key == K_g :

				herramientas.Herramienta = "Pintura"

			elif key == K_i :

				herramientas.Herramienta = "CogerColor"

			elif key == K_m :

				if ctrl :
					seleccion.Selec = False
				else :
					herramientas.Herramienta = "Seleccionar"

			elif key == K_e :

				if ctrl :

					dimensiones = dimensionesImagen(programa.Proyec.Imagenes[programa.Imag])

					seleccion.pos0 = [0,0]
					seleccion.pos1 = [dimensiones[0] - 1, dimensiones[1] - 1]
					seleccion.Selec = True
 
			elif key == K_BACKSPACE or key == K_DELETE :

				Borr()

			elif key == K_x :

				print(ctrl)

				if not ctrl :

					color = herramientas.Color

					if color == 0 :

						herramientas.Color = 1

					else :

						herramientas.Color = 0

			elif key == K_UP :

				_Zoom_((Vent.posicion[0] + (Vent.dimensiones[0] / 2), Vent.posicion[1] + (Vent.dimensiones[1] / 2)), 1)

			elif key == K_DOWN :

				_Zoom_((Vent.posicion[0] + (Vent.dimensiones[0] / 2), Vent.posicion[1] + (Vent.dimensiones[1] / 2)), -1)

			elif key == K_LEFT :

				IzqVentana()

			elif key == K_RIGHT :

				DerVentana()

			elif key == K_s :

				if ctrl and shift :

					guardarComo()
					ctrl = False
					shift = False

				elif ctrl :

					guardar()
					ctrl = False

			if key == K_o :

				if ctrl :

					abrir()
					ctrl = False

			elif key == K_n :

				if ctrl and shift :

					CrearVentana()

				elif ctrl :

					crear()
					ctrl = False

			if key == K_c :

				if ctrl :

					Cop()

				else :

					if BLOC :
						BLOC = False
					else :
						BLOC = True

			elif key == K_v :

				if ctrl :

					Peg()

			elif key == K_x :

				if ctrl and shift :

					EliminarVentana()

				elif ctrl :

					Cor()

			elif key == K_z :

				if ctrl and shift :

					AdelantarHistorial()

				elif ctrl :

					RetrocederHistorial()

			elif key == K_SPACE :

				FonPlay = DarPlay(FonPlay)

			elif key == K_q :

				if ctrl :

					png()

			if key == K_RCTRL or key == K_LCTRL :

				ctrl = True

			if key == K_RSHIFT or key == K_LSHIFT :

				shift = True

		if evento.type == KEYUP :

			key = evento.key

			if key == K_RCTRL or key == K_LCTRL :

				ctrl = False

			if key == K_RSHIFT or key == K_LSHIFT :

				shift = False

		if evento.type == pygame.MOUSEBUTTONDOWN :

			if evento.button == 1 :

				#Eventos

				if herramientas.Herramienta == "Seleccionar" :

					if colisionRecuadro(Vent.dimensiones, Vent.posicion, pygame.mouse.get_pos()) :

						cuadro = CuadroTocado(programa, pygame.mouse.get_pos())
						if cuadro :
							seleccion.Selec = True
							seleccion.pos0[0] = cuadro[0]
							seleccion.pos0[1] = cuadro[1]
							seleccion.pos1[0] = cuadro[0]
							seleccion.pos1[1] = cuadro[1]


				#Botones

				if BotonMover.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "Mover"

				elif BotonPincel.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "Pincel"

				elif BotonBorrar.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "Borrar"

				elif BotonPintura.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "Pintura"

				elif BotonCogerColor.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "CogerColor"

				elif BotonSeleccionar.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "Seleccionar"

				elif BotonCandado.PulsarBoton(pygame.mouse.get_pos()) :

					if BLOC :
						BLOC = False
					else :
						BLOC = True

				elif BotonIzq.PulsarBoton(pygame.mouse.get_pos()) :

					IzqVentana()

				elif BotonDer.PulsarBoton(pygame.mouse.get_pos()) :

					DerVentana()

				elif BotonNuevaVent.PulsarBoton(pygame.mouse.get_pos()) :

					CrearVentana()

				elif BotonEliminarVent.PulsarBoton(pygame.mouse.get_pos()) :

					EliminarVentana()

				elif BotonAbrir.PulsarBoton(pygame.mouse.get_pos()) :

					abrir()

				elif BotonGuardar.PulsarBoton(pygame.mouse.get_pos()) :

					guardar()

				elif BotonCrear.PulsarBoton(pygame.mouse.get_pos()) :

					crear()

				elif BotonRetrasar.PulsarBoton(pygame.mouse.get_pos()) :

					RetrocederHistorial()

				elif BotonAdelantar.PulsarBoton(pygame.mouse.get_pos()) :

					AdelantarHistorial()

				elif BotonDeseleccionar.PulsarBoton(pygame.mouse.get_pos()) :

					seleccion.Selec = False

				elif BotonSelec.PulsarBoton(pygame.mouse.get_pos()) :

					herramientas.Herramienta = "Seleccionar"

				elif BotonAumentar.PulsarBoton(pygame.mouse.get_pos()) :

					_Zoom_((Vent.posicion[0] + (Vent.dimensiones[0] / 2), Vent.posicion[1] + (Vent.dimensiones[1] / 2)), 1)

				elif BotonDisminuir.PulsarBoton(pygame.mouse.get_pos()) :

					_Zoom_((Vent.posicion[0] + (Vent.dimensiones[0] / 2), Vent.posicion[1] + (Vent.dimensiones[1] / 2)), -1)

				elif BotonCop.PulsarBoton(pygame.mouse.get_pos()) :

					Cop()

				elif BotonPeg.PulsarBoton(pygame.mouse.get_pos()) :

					Peg()

				elif BotonCor.PulsarBoton(pygame.mouse.get_pos()) :

					Cor()

				elif BotonPlay.PulsarBoton(pygame.mouse.get_pos()) :

					FonPlay = DarPlay(FonPlay)

				elif BotonEspejoVer.PulsarBoton(pygame.mouse.get_pos()) :

					_EspejoVer_()

				elif BotonEspejoHor.PulsarBoton(pygame.mouse.get_pos()) :

					_EspejoHor_()

				elif BotonSalir.PulsarBoton(pygame.mouse.get_pos()) :

					pygame.quit()
					sys.exit()

				elif BotonCamara.PulsarBoton(pygame.mouse.get_pos()) :

					png()
					
				#Capsulas de Colores

				color = pygame.Color(0,0,0)
				receptor = herramientas.Color
				cambiar = False

				if Capsula1.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula1.Color
					cambiar = True
				elif Capsula2.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula2.Color
					cambiar = True
				elif Capsula3.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula3.Color
					cambiar = True
				elif Capsula4.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula4.Color
					cambiar = True
				elif Capsula5.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula5.Color
					cambiar = True
				elif Capsula6.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula6.Color
					cambiar = True
				elif Capsula7.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula7.Color
					cambiar = True
				elif Capsula8.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula8.Color
					cambiar = True
				elif Capsula9.PulsarCapsula(pygame.mouse.get_pos()) :
					color = Capsula9.Color
					cambiar = True


				elif Color1.PulsarCapsula(pygame.mouse.get_pos()) :
					if receptor != 0 :
						herramientas.Color = 0
						cambiar = False
					else :
						(colorcode, hexa) = askcolor(title = "Color")
						if colorcode == None :
							cambiar = False
						else :
							try:
								color = pygame.Color(int(colorcode[0]),int(colorcode[1]),int(colorcode[2]))
								cambiar = True
							except:
								cambiar = False
								print("Error")

				elif Color2.PulsarCapsula(pygame.mouse.get_pos()) :
					if receptor == 0 :
						herramientas.Color = 1
						cambiar = False
					else :
						(colorcode, hexa) = askcolor(title = "Color")
						if color == None :
							cambiar = False
						else :
							try:
								color = pygame.Color(int(colorcode[0]),int(colorcode[1]),int(colorcode[2]))
								cambiar = True
							except:
								cambiar = False
								print("Error")

				if cambiar :
					if receptor == 0 :
						Color1.Color = color
					else :
						Color2.Color = color

				if CapsulaSeleccion.PulsarCapsula(pygame.mouse.get_pos()) :
					(colorcode, hexa) = askcolor(title = "Color de Seleccion")
					if colorcode :
						CapsulaSeleccion.Color = pygame.Color(int(colorcode[0]), int(colorcode[1]), int(colorcode[2]))
						seleccion.Color = CapsulaSeleccion.Color

				elif CapsulaFondo.PulsarCapsula(pygame.mouse.get_pos()) :
					(colorcode, hexa) = askcolor(title = "Color de fondo")
					if colorcode :
						CapsulaFondo.Color = pygame.Color(int(colorcode[0]), int(colorcode[1]), int(colorcode[2]))
						Fon = pygame.Color(int(colorcode[0]), int(colorcode[1]), int(colorcode[2]))


	reloj.tick(15)

	#Fondo
	ventana.fill(COLOR)

	#Dibujar

	dibujar()


	#Actualizar
	pygame.display.update()
	#root.update()

root.mainloop()