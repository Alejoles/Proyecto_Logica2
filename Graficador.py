from tkinter import *

ventana=Tk()
ventana.geometry("700x700")

imagenes=[]	# Lista de imagenes
MAPA = {}	# Diccionario que da la interpretacion
Verdad = []	# Lista en la que se guardan las interpretaciones que son verdaderas


cuboaa=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboaa)

for a in range(97,123):		# Acá se guardan todas las imagenes en la lista imagenes
	imagen="cubo"+chr(a)+".png"
	path="/home/alejo/Downloads/todaslasimagenes/"+imagen
	imagenx = PhotoImage(file=(path),width=500,height=500)
	imagenes.append(imagen)
	

"""

cuboa=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboa)
cubob=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubob)
cuboc=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboc)
cubod=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubod)
cuboe=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboe)
cubof=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubof)
cubog=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubog)
cuboh=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboh)
cuboi=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboi)
cuboj=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboj)
cubok=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubok)
cubol=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubol)
cubom=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubom)
cubon=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubon)
cuboo=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboo)
cubop=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubop)
cuboq=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboq)
cubor=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubor)
cubos=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubos)
cubot=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubot)
cubou=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubou)
cubov=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubov)
cubow=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubow)
cubox=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cubox)
cuboy=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboy)
cuboz=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboz)
cuboaa=PhotoImage(file=(path),width=500,height=500)
imagenes.append(cuboaa)
"""
for a in imagenes: # Empezamos con todas las imagenes en 0 
	MAPA[a] = 0
	
MAPA[imagenes[1]] = 1 # a excepcion de una que tiene el valor 1


for i in MAPA:		# Agregamos las interpretaciones que son verdaderas a la lista Verdad
	if(MAPA.get(i)==1):
		Verdad.append(i)
		
lienzo=Canvas(ventana,width=1080,height=720)
lienzo.place(x=0,y=0)


lienzo.create_image(0,0,image=imagenes[0],anchor=NW)
lienzo.create_image(0,0,image=imagenes[1],anchor=NW)
lienzo.create_image(0,0,image=imagenes[2],anchor=NW)
	


ventana.mainloop()
