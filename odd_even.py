import math

def odd_even():
    n = int(input("Introduzca un número: "))

    if n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Weird")
        else:
            if n >= 6 and n <= 20:
                print("Weird")
            else:
                if n >= 20:
                    print("Not Weird")
    else:
        print("Weird")    

