#IMPAR ONLY
matriz=[[3,3,3,0,0,0],[3,3,3,0,0,0],[3,3,3,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
letrasProposicionales=['a','b','c','d','e','f','p','i','1','2','3']
diccionario={'a':1,'b':1, 'c':1, 'd':1, 'e':1,'f':1, 'p':1, 'i':1, '1':1, '2':1, '3':1}
def graficar(formula,diccionario):
	lista=[]
	for a in range(0,len(formula)):	
		if(formula[a] in letrasProposicionales): lista.append(formula[a])

	for a in range(0,len(lista),21):
		contador=21
		for b in range(a,a+21,1):
			if(diccionario.get(lista[b])==1): 			
				print(diccionario.get(lista[b]))				
				contador-=1

		print("contador1:" + str(contador))

		if(contador==0):
			subLista=[]
			for c in range(a,a+3,1):
				subLista.append(lista[c])
			
			if(subLista[0] in ['a','b','c']): 
				matriz[ord(subLista[0])-96+2][int(subLista[2])-1]=1
				
				for a in range(3,6):				
					matriz[ord(subLista[0])-96+2][a]=1
									
				for a in range(3,6):				
					matriz[int(subLista[2])-1][a]=1
							
						
			else:
				matriz[int(subLista[2])-1][ord(subLista[0])-96-1]=1
									
				for a in range(3,6):				
					matriz[a][ord(subLista[0])-96-1]=1
									
				for a in range(3,6):				
					matriz[a][int(subLista[2])-1]=1
						

		else:

			for a in range(0,len(lista),10):
				contador=8
				for b in range(a,a+10,1):
					if(diccionario.get(lista[b])==1): 			
						print(diccionario.get(lista[b]))				
						contador-=1

				print('CONTADOR2: ' + str(contador))			

				if(contador==0):
					subLista=[]
					for c in range(a,a+6,1):
						subLista.append(lista[c])
					
					if(subLista[0] in ['a','b','c']):  
						matriz[ord(subLista[0])-96+2][int(subLista[2])+2]=1
						for a in range(0,3):				
							matriz[ord(subLista[0])-96+2][a]=1
									
						for a in range(0,3):				
							matriz[a][int(subLista[2])+2]=1
									
						
					else: 
						matriz[int(subLista[2])+2][ord(subLista[0])-96-1]=1
						for a in range(0,3):				
							matriz[a][ord(subLista[0])-96-1]=1
									
						for a in range(0,3):				
							matriz[int(subLista[2])+2][a]=1
						

			#if(subLista[3] in ['a','b','c']): matriz[ord(subLista[3])-96+2][int(subLista[5])+2]=1
			#else: matriz[int(subLista[5])+2][ord(subLista[3])-96-1]=1

graficar("((dYp)Y3)>-((aYp)Y3)Y-((bYp)Y3)Y-((cYp)Y3)Y-((aYi)Y1)Y-((bYi)Y1)Y-((cYp)Y1)",diccionario)
for a in range(0,len(matriz)):
	print(str(matriz[a]) + '\n')
