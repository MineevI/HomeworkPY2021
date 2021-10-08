import math

a = float(input("A =:"))
b = float(input("B =:"))
f = float(input("угол =:"))

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(f)))

print("Ответ:",c,)