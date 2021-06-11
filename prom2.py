
run = 1
nota = 0
prom = 0
while run == 1:
    numEst = int(input("Ingrese cantidad estudiantes: "))
    if numEst < 0:
        print("Debe ser un valor mayor a cero")
    else:
        for i in range(numEst):
            print("Nota para el estudiante ", i, " :")
            nota = int(input())
            nota += nota
            
        prom = nota / numEst
        print("Promedio ", prom)