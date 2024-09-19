from math import hypot
co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente:'))
hi = hypot(co,ca)
print('a hipotenusa e {:.2f}'.format(hi))