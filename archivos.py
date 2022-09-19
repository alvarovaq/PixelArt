import pickle
from io import *
from tkinter import *
from tkinter import filedialog
from herramientas import *

#Guardar archivo

def GuardarArchivo (proyecto, ruta) :

	archivo = open(ruta, "wb")

	pickle.dump(proyecto.Imagenes, archivo)

	archivo.close()

	del archivo

#Abrir archivo

def AbrirArchivo (ruta) :

	archivo = open(ruta, "rb")

	imagenes = pickle.load(archivo)

	archivo.close()

	del archivo

	return imagenes

