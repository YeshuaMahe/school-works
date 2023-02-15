print("Bienvenido a la universidad de oriente, camp. Poza Rica")

my_dictionary=()
other_dictionary=[]

nombres = str(input("cuales son tus nombres: "))
apellidos = str(input("cuales son tus apellidos: "))
edad = str(input("ingresa tu edad: "))
carrera = str(input("ingresa la carrera de tu eleccion: "))

Person = {
    'nombres' : nombres,
    'apellidos' : apellidos,
    'edad' : edad,
    'carrera' : carrera,
}

Person['nombres']=nombres
Person['apellidos']=apellidos
Person['edad']=edad
Person['carrera']=carrera

print(Person)

my_set=()

nums = []
print("cuantas calificaciones desea ingresar")
n = int(input())
i = 0
while i < n:
    print("ingresa califiacion: ", i+1)
    val = float(input())
    nums.append(val)
    i+=1
prom = sum(nums) / len(nums)
print("El promedio es: ", prom)

if prom >=7	:
    print("usted es apto para continuar") 
    print("se le aplicara un examen con 3 preguntas donde debera aprobar con minimo de dos puntos")

    respuestas = ["1989", "2002", "guido van rossum", "1995"]
for vic  in range(4, 0, -1):
    if vic == 4:
        op = input("¿En que año fueron los inicios de Python?\n 1-1989\n 2-1988\n 3-1998\n 4-1870\n Escribe la respuesta")
        op = op.lower()
        if op == respuestas [0]:
            print("LA RESPUESTA ES CORRRECTA, SUMAS 1 PUNTO :)")
        else:
            print("LA RESPUESTA ES INCORRECTA, SUMAS 0 PUNTOS :(")
    if vic == 3:
        op = input("¿Quien ha desarrollado Python?\n 1-guido van rosum\n 2-guido van rossum\n 3-Bjarne Stroustrup\n 4-Brendan Eich\n Escribe la respuesta")
        op = op.lower()
        if op == respuestas [2]:
            print("LA RESPUESTA ES CORRRECTA, SUMAS 1 PUNTO :)")
        else:
            print("LA RESPUESTA ES INCORRECTA, SUMAS 0 PUNTOS :(")
    if vic == 2:
        op = input("¿En que fecha se publico el lenguaje C++?\n 1-1990\n 2-1889\n 3-2001\n 4-2002\n Escribe la respuesta")
        op = op.lower()
        if op == respuestas [1]:
            print("LA RESPUESTA ES CORRRECTA, SUMAS 1 PUNTO :)")
        else:
            print("LA RESPUESTA ES INCORRECTA, SUMAS 0 PUNTOS :(")
    if vic == 1:
        op = input("¿En que fecha se publico el lenguaje java?\n 1-1990\n 2-2002\n 3-1995\n 4-2001\n Escribe la respuesta")
        op = op.lower()
        if op == respuestas [3]:
            print("LA RESPUESTA ES CORRRECTA, SUMAS 1 PUNTO :)")
        else:
            print("LA RESPUESTA ES INCORRECTA, SUMAS 0 PUNTOS :(")    
else:
    print("usted no es apto para ingresar, se cancela el tramite")

