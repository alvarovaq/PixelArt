from PIL import Image
import pygame
from pygame.locals import *

im = Image.open("Imagenes/Abrir.png")
pixelMap = im.load()

img = Image.new(im.mode, im.size)
pixelsNew = img.load()

for i in range(img.size[0]) :
	for j in range (img.size[1]) :
		print(pixelMap[i,j])
		if 22 in pixelMap[i,j] or 103 in pixelMap[i,j] or 183 in pixelMap[i,j] :
			pixelMap[i,j] = (255,0,0,255)
		pixelsNew[i,j] = pixelMap[i,j]

img.show()
img.save("Prueba.png")
im.close()

