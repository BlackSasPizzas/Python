from math import radians, sin, cos, tan

angulo = float(input('digite o angulo:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo {}\nTem o seno do angulo e {:.2f} \nO cosseno do angulo e {:.2f} \nE a tangente do angulo e {:.2f}'.format(angulo,seno,cosseno,tangente))