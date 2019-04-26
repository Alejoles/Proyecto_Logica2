 
"""				REGLA 1 SIN ITERACION Y CON 27 LP
LetrasProp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A']

R1 = 'l-k-Yj-Ys-Yv-Yy-Ya>'
R2 = 'l-k-Yj-Yt-Yw-Yz-Yb>'
R3 = 'l-k-Yj-Yu-Yx-YA-Yc>'
R4 = 'o-n-Ym-Ys-Yv-Yy-Yd>'
R5 = 'o-n-Ym-Yt-Yw-Yz-Ye>'
R6 = 'o-n-Ym-Yu-Yx-YA-Yf>'
R7 = 'r-q-Yp-Ys-Yv-Yy-Yg>'
R8 = 'r-q-Yp-Yt-Yw-Yz-Yh>'
R9 = 'r-q-Yp-Yu-Yx-YA-Yi>'
R10 = 'a-b-Yc-Yy-Yz-YA-Yj>'
R11 = 'a-b-Yc-Yv-Yw-Yx-Yk>'
R12 = 'a-b-Yc-Ys-Yt-Yu-Yl>'
R13 = 'd-e-Yf-Yy-Yz-YA-Ym>'
R14 = 'd-e-Yf-Yv-Yw-Yx-Yn>'
R15 = 'd-e-Yf-Ys-Yt-Yu-Yo>'
R16 = 'g-h-Yi-Yy-Yz-YA-Yp>'
R17 = 'g-h-Yi-Yv-Yw-Yx-Yq>'
R18 = 'g-h-Yi-Ys-Yt-Yu-Yr>'
R19 = 'l-o-Yr-Ya-Yd-Yg-Ys>'
R20 = 'l-o-Yr-Yb-Ye-Yh-Yt>'
R21 = 'l-o-Yr-Yc-Yf-Yi-Yu>'
R22 = 'k-n-Yq-Ya-Yd-Yg-Yv>'
R23 = 'k-n-Yq-Yb-Ye-Yh-Yw>'
R24 = 'k-n-Yq-Yc-Yf-Yi-Yx>'
R25 = 'j-m-Yp-Ya-Yd-Yg-Yy>'
R26 = 'j-m-Yp-Yb-Ye-Yh-Yz>'
R27 = 'j-m-Yp-Yc-Yf-Yi-YA>'

Regla1 = R1 + R2 + 'Y' + R3 + 'Y'+ R4 + 'Y' + R5 + 'Y'+ R6 + 'Y' + R7 + 'Y'+ R8 + 'Y' + R9 + 'Y'+ R10 + 'Y' + R11 + 'Y'+ R12 + 'Y' + R13 + 'Y'+ R14 + 'Y' + R15 + 'Y'+ R16 + 'Y' + R17 + 'Y'+ R18 + 'Y' + R19 + 'Y'+ R20 + 'Y' + R21 + 'Y'+ R22 + 'Y' + R23 + 'Y'+ R24 + 'Y' + R25 + 'Y'+ R26 + 'Y' + R27 + 'Y'

"""




LetrasProp = ['a','b','c','d','e','f','p','i','1','2','3']
#		Cara 1 (PAR) IZQUIERDA
R1 = '(((aYp)Y1)>(-((dYp)Y1)Y-((eYp)Y1)Y-((fYp)Y1)Y-((dYi)Y1)Y-((eYi)Y1)Y-((fYi)Y1)))'
R2 = '(((aYp)Y2)>(-((dYp)Y2)Y-((eYp)Y2)Y-((fYp)Y2)Y-((dYi)Y1)Y-((eYi)Y1)Y-((fYi)Y1)))'
R3 = '(((aYp)Y3)>(-((dYp)Y3)Y-((eYp)Y3)Y-((fYp)Y3)Y-((dYi)Y1)Y-((eYi)Y1)Y-((fYi)Y1)))'
R4 = '(((bYp)Y1)>(-((dYp)Y1)Y-((eYp)Y1)Y-((fYp)Y1)Y-((dYi)Y2)Y-((eYi)Y2)Y-((fYi)Y2)))'
R5 = '(((bYp)Y2)>(-((dYp)Y2)Y-((eYp)Y2)Y-((fYp)Y2)Y-((dYi)Y2)Y-((eYi)Y2)Y-((fYi)Y2)))'
R6 = '(((bYp)Y3)>(-((dYp)Y3)Y-((eYp)Y3)Y-((fYp)Y3)Y-((dYi)Y2)Y-((eYi)Y2)Y-((fYi)Y2)))'
R7 = '(((cYp)Y1)>(-((dYp)Y1)Y-((eYp)Y1)Y-((fYp)Y1)Y-((dYi)Y3)Y-((eYi)Y3)Y-((fYi)Y3)))'
R8 = '(((cYp)Y2)>(-((dYp)Y2)Y-((eYp)Y2)Y-((fYp)Y2)Y-((dYi)Y3)Y-((eYi)Y3)Y-((fYi)Y3)))'
R9 = '(((cYp)Y3)>(-((dYp)Y3)Y-((eYp)Y3)Y-((fYp)Y3)Y-((dYi)Y3)Y-((eYi)Y3)Y-((fYi)Y3)))'

#		Cara 2 (PAR) ARRIBA

R10 = '(((dY1)Yp)>(-((aY1)Yp)Y-((bY1)Yp)Y-((cY1)Yp)Y-((aY1)Yi)Y-((bY1)Yi)Y-((cY1)Yi)))'
R11 = '(((dY2)Yp)>(-((aY2)Yp)Y-((bY2)Yp)Y-((cY2)Yp)Y-((aY1)Yi)Y-((bY1)Yi)Y-((cY1)Yi)))'
R12 = '(((dY3)Yp)>(-((aY3)Yp)Y-((bY3)Yp)Y-((cY3)Yp)Y-((aY1)Yi)Y-((bY1)Yi)Y-((cY1)Yi)))'
R13 = '(((eY1)Yp)>(-((aY1)Yp)Y-((bY1)Yp)Y-((cY1)Yp)Y-((aY2)Yi)Y-((bY2)Yi)Y-((cY2)Yi)))'
R14 = '(((eY2)Yp)>(-((aY2)Yp)Y-((bY2)Yp)Y-((cY2)Yp)Y-((aY2)Yi)Y-((bY2)Yi)Y-((cY2)Yi)))'
R15 = '(((eY3)Yp)>(-((aY3)Yp)Y-((bY3)Yp)Y-((cY3)Yp)Y-((aY2)Yi)Y-((bY2)Yi)Y-((cY2)Yi)))'
R16 = '(((fY1)Yp)>(-((aY1)Yp)Y-((bY1)Yp)Y-((cY1)Yp)Y-((aY3)Yi)Y-((bY3)Yi)Y-((cY3)Yi)))'
R17 = '(((fY2)Yp)>(-((aY2)Yp)Y-((bY2)Yp)Y-((cY2)Yp)Y-((aY3)Yi)Y-((bY3)Yi)Y-((cY3)Yi)))'
R18 = '(((fY3)Yp)>(-((aY3)Yp)Y-((bY3)Yp)Y-((cY3)Yp)Y-((aY3)Yi)Y-((bY3)Yi)Y-((cY3)Yi)))'

#		Cara 3 (IMPAR) CENTRO Tomando D,E,F

R19 = '(((dY1)Yi)>(-((aY1)Yp)Y-((aY2)Yp)Y-((aY3)Yp)Y-((dY1)Yp)Y-((dY2)Yp)Y-((dY3)Yp)))'
R20 = '(((dY2)Yi)>(-((bY1)Yp)Y-((bY2)Yp)Y-((bY3)Yp)Y-((dY1)Yp)Y-((dY2)Yp)Y-((dY3)Yp)))'
R21 = '(((dY3)Yi)>(-((cY1)Yp)Y-((cY2)Yp)Y-((cY3)Yp)Y-((dY1)Yp)Y-((dY2)Yp)Y-((dY3)Yp)))'
R22 = '(((eY1)Yi)>(-((aY1)Yp)Y-((aY2)Yp)Y-((aY3)Yp)Y-((eY1)Yp)Y-((eY2)Yp)Y-((eY3)Yp)))'
R23 = '(((eY2)Yi)>(-((bY1)Yp)Y-((bY2)Yp)Y-((bY3)Yp)Y-((eY1)Yp)Y-((eY2)Yp)Y-((eY3)Yp)))'
R24 = '(((eY3)Yi)>(-((cY1)Yp)Y-((cY2)Yp)Y-((cY3)Yp)Y-((eY1)Yp)Y-((eY2)Yp)Y-((eY3)Yp)))'
R25 = '(((fY1)Yi)>(-((aY1)Yp)Y-((aY2)Yp)Y-((aY3)Yp)Y-((fY1)Yp)Y-((fY2)Yp)Y-((fY3)Yp)))'
R26 = '(((fY2)Yi)>(-((bY1)Yp)Y-((bY2)Yp)Y-((bY3)Yp)Y-((fY1)Yp)Y-((fY2)Yp)Y-((fY3)Yp)))'
R27 = '(((fY3)Yi)>(-((cY1)Yp)Y-((cY2)Yp)Y-((cY3)Yp)Y-((fY1)Yp)Y-((fY2)Yp)Y-((fY3)Yp)))'

#			Regla1-----------------------------------------------

Reglita = ''
x = 0
y = 0
z = 0

for i in range(0,9):
	if(i<3):
		Reglita = Reglita + '(((aYp)Y'+ str(i%3+1) +')>(-((dYp)Y'+ str(i%3+1) +')Y-((eYp)Y'+ str(i%3+1) +')Y-((fYp)Y'+ str(i%3+1) +')Y-((dYi)Y1)Y-((eYi)Y1)Y-((fYi)Y1)))' + 'O'
	elif(i>=3 and i<6):
		Reglita = Reglita + '(((bYp)Y'+ str(i%3+1) +')>(-((dYp)Y'+ str(i%3+1) +')Y-((eYp)Y'+ str(i%3+1) +')Y-((fYp)Y'+ str(i%3+1) +')Y-((dYi)Y2)Y-((eYi)Y2)Y-((fYi)Y2)))' + 'O'
	elif(i>=6):
		Reglita = Reglita + '(((cYp)Y'+ str(i%3+1) +')>(-((dYp)Y'+ str(i%3+1) +')Y-((eYp)Y'+ str(i%3+1) +')Y-((fYp)Y'+ str(i%3+1) +')Y-((dYi)Y3)Y-((eYi)Y3)Y-((fYi)Y3)))' + 'O'

#				CARA ARRIBA(PAR)
for i in range(0,9):
	if(i<3):
		Reglita = Reglita + '(((dYp)Y'+ str(i%3+1) +')>(-((aYp)Y'+ str(i%3+1) +')Y-((bYp)Y'+ str(i%3+1) +')Y-((cYp)Y'+ str(i%3+1) +')Y-((aYi)Y1)Y-((bYi)Y1)Y-((cYi)Y1)))' + 'O'
	elif(i>=3 and i<6):
		Reglita = Reglita + '(((eYp)Y'+ str(i%3+1) +')>(-((aYp)Y'+ str(i%3+1) +')Y-((bYp)Y'+ str(i%3+1) +')Y-((cYp)Y'+ str(i%3+1) +')Y-((aYi)Y2)Y-((bYi)Y2)Y-((cYi)Y2)))' + 'O'
	elif(i>=6):
		Reglita = Reglita + '(((fYp)Y'+ str(i%3+1) +')>(-((aYp)Y'+ str(i%3+1) +')Y-((bYp)Y'+ str(i%3+1) +')Y-((cYp)Y'+ str(i%3+1) +')Y-((aYi)Y3)Y-((bYi)Y3)Y-((cYi)Y3)))' + 'O'
		
#				Cara del medio con d,e,f

for i in range(0,9):
	if(i<3):
		Reglita = Reglita + '(((dYi)Y'+ str(i%3+1) +')>(-(('+ str(chr((97+x+100)%100)) +'Yp)Y1)Y-(('+ str(chr((97+x+100)%100)) +'Yp)Y2)Y-(('+ str(chr((97+x+100)%100)) +'Yp)Y3)Y-((dYp)Y1)Y-((dYp)Y2)Y-((dYp)Y3)))' + 'O'
		x += 1
	elif(i>=3 and i<6):
		Reglita = Reglita + '(((eYi)Y'+ str(i%3+1) +')>(-(('+ str(chr((97+y+100)%100)) +'Yp)Y1)Y-(('+ str(chr((97+y+100)%100)) +'Yp)Y2)Y-(('+ str(chr((97+y+100)%100)) +'Yp)Y3)Y-((eYp)Y1)Y-((eYp)Y2)Y-((eYp)Y3)))' + 'O'
		y += 1
	elif(i>=6):
		Reglita = Reglita + '(((fYi)Y'+ str(i%3+1) +')>(-(('+ str(chr((97+z+100)%100)) +'Yp)Y1)Y-(('+ str(chr((97+z+100)%100)) +'Yp)Y2)Y-(('+ str(chr((97+z+100)%100)) +'Yp)Y3)Y-((fYp)Y1)Y-((fYp)Y2)Y-((fYp)Y3)))' + 'O'
		z += 1

Reglita = '(' + Reglita + ')'
print(Reglita)


#-----------------------------------------------------------------------------------------------






