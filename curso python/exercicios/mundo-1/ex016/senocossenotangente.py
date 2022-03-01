import math
angulo = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tang = math.tan(math.radians(angulo))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tang))


'''pode se usar tambêm (from math import radians, sin, cos, tan) desse modo não é preciso referênciar a biblioteca math, nas variáveis.

veja o exemplo abaixo que vai obter o mesmo resultado.

from math import radians, sin, cos, tan
angulo = float(input("Digite o ângulo que deseja: "))
seno = sin(radians(angulo))
print("O ângulo de {} tem o seno de {:.2f}".format(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de {} tem o cosseno de {:.2f}".format(angulo, cosseno))
tang = tan(radians(angulo))
print("O ângulo de {} tem a tangente de {:.2f}".format(angulo, tang))'''
