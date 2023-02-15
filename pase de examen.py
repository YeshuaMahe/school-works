import random
sep = "-" * 15

print('''Reglas del juego
    tijeras cortan papel
    papel cortan tijeras
    piedra aplasta lagarto
    lagarto envenena a spock
    spock rompe tijeras
    tijeras decapitan lagarto
    lagarto devora papel
    papel desautoriza spock
    spock evaporiza piedra
    piedra rompe tijeras    
''')

opciones = ["piedra","papel","tijeras","lagarto","spock"]

while True:
    jugador = input("elije piedra, papel, tijeras, lagarto, spock: ").lower()
    compu = random.choice(opciones)
    print(f"la compu ha seleccionado {compu}")
    if jugador == compu:
        print(f"empate, ambos eligieron {jugador}")
    elif jugador == "piedra" and compu == "tijeras":
        print(f"ganaste, {jugador} gana en contra de {compu}")
    elif jugador == "tijeras" and compu == "papel":
        print(f"ganaste, {jugador} gana en contra de {compu}")
    elif jugador == "piedra" and compu == "lagarto":
        print(f"ganaste, {jugador} aplasta {compu}")
    elif jugador == "spock" and compu == "piedra":
        print(f"ganaste, {jugador} evaporiza {compu}")
    elif jugador == "papel" and compu == "spock":
        print(f"ganaste, {jugador} desautoriza {compu}")
    elif jugador == "lagarto" and compu == "spock":
        print(f"ganaste, {jugador} envenena {compu}")
    elif jugador == "lagarto" and compu == "papel":
        print(f"ganaste, {jugador} devora {compu}")
    else:
    print(f"{sep}fin del juego{sep}")

