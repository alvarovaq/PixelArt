from clases import *

def dimensionesImagen (Imagen) :

	ancho = 0
	alto = 0

	if len(Imagen) :
		ancho = len(Imagen)
		alto = len(Imagen[0])

	dimensiones = [ancho, alto]

	return dimensiones

def colisionRecuadro (dimensiones, posicion1, posicion2) :

	ancho = dimensiones[0]
	alto = dimensiones[1]

	posX1 = posicion1[0]
	posY1 = posicion1[1]

	posX2 = posicion2[0]
	posY2 = posicion2[1]

	if posX2 >= posX1 and posX2 <= posX1 + ancho :
		if posY2 >= posY1 and posY2 <= posY1 + alto :

			return True

	return False

def CuadroDentro (dimensiones, posicion, dimensiones2, posicion2) :

	esquinas = [

		(posicion2[0], posicion2[1]),
		(posicion2[0] + dimensiones2[0], posicion2[1]),
		(posicion2[0], posicion2[1] + dimensiones2[1]),
		(posicion2[0] + dimensiones2[0], posicion2[1] + dimensiones2[1])

	]

	contador = 0

	for i in range(4) :
		if colisionRecuadro(dimensiones, posicion, esquinas[i]) :
			contador += 1

	return contador

def CuadroTocado (programa, pos) :

	Imagen = programa.Proyec.Imagenes[programa.Imag]
	posicion = programa.Proyec.posicion
	Tam = programa.Proyec.Tam
	Borde = programa.Proyec.Borde
	dimensiones = dimensionesImagen(Imagen)

	difx = pos[0] - posicion[0]
	dify = pos[1] - posicion[1]

	if difx < 0 or dify < 0 :
		return None

	cuadrox = int(difx / (Tam + Borde))
	cuadroy = int(dify / (Tam + Borde))

	if cuadrox >= dimensiones[0] or cuadroy >= dimensiones[1] :
		return None

	return (cuadrox, cuadroy)

def PosSeleccion (seleccion) :

	pos0 = seleccion.pos0
	pos1 = seleccion.pos1

	x = None
	y = None

	if pos0[0] <= pos1[0] :	
		x = pos0[0]
	else :
		x = pos1[0]
	if pos0[1] <= pos1[1] :
		y = pos0[1]
	else :
		y = pos1[1]

	return (x,y)


