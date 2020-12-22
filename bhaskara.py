import math

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

x = (b**2)-(4*a*c)
x = math.sqrt(x)
x1 = (-b+x)/(2*a)
x2 = (-b-x)/(2*a)

x = (b ** 2) - (4 * a * c)

if x < 0:
    print("Raiz negativa nao pode ser extraida.")
    exit()

else:
    x = math.sqrt(x)
    x1 = (-b + x) / (2 * a)
    x2 = (-b - x) / (2 * a)
print("\n\nX¹ = %s \nX² = " % x1, x2)

