import random
n = int(20)

for i in range(n):
    prom = random.randint(0,9)
    if prom >= 9:
        print("Excelente")
    else:
        print("Mejore")
