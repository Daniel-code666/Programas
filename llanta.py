import random

fix = 1

while fix < 2:
    
    llanta1 = random.randint(1,9)
    llanta2 = random.randint(1,9)
    llanta3 = random.randint(1,9)
    llanta4 = random.randint(1,9)
    
    print("Arrenglando...")

    if llanta1 > 4 and llanta2 > 4 and llanta3 > 4 and llanta4 > 4:
        print("Arreglada")
        fix += 1
