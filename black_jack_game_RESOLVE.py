import random
import re

mazo = [
    "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️", "A♠️",
    "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️", "A♦️",
    "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️", "A♥️",
    "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️", "A♣️",
]

turno = 0
apuesta_maxima = 10
creditos_p1 = 50
creditos_p2 = 50

plantado_p1 = False
plantado_p2 = False

suma_p1 = 0
suma_p2 = 0

def iniciar_juego():
    nombre_p1, nombre_p2 = pedir_nombres()
    cartas_p1, cartas_p2 = repartir_cartas()
    escoger_turno_mostrar_cartas(nombre_p1, nombre_p2, cartas_p1, cartas_p2)

def pedir_nombres():
    print("\n" + "=" * 60)
    print(" " * 9 + "♠️ ♦️ ♥️ ♣️ ¡BIENVENIDO AL BLACKJACK! ♠️ ♦️ ♥️ ♣️")
    print("=" * 60 + "\n")

    print("El jugador 1 ingresa su nombre")
    nombre_1 = input("-->: ").capitalize()
    print(f"✅ ¡Bienvenido, {nombre_1}!\n")

    print("El jugador 2 ingresa su nombre")
    nombre_2 = input("-->: ").capitalize()
    print(f"✅ ¡Bienvenido, {nombre_2}!\n")

    print("\n    💥💥💥-¡EMPECEMOS!💥💥💥     ")
    print("\n")

    return nombre_1, nombre_2

def repartir_cartas():
    cartas = random.sample(mazo, 4)
    return cartas[:2], cartas[2:]

def valor_carta(carta):
    valor = re.findall(r'\d+|[JQKA]', carta)[0]
    if valor.isdigit():
        return int(valor)
    elif valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11
    return 0

def suma_cartas(cartas):
    suma = 0
    num_ases = 0

    for carta in cartas:
        valor = valor_carta(carta)
        if valor == 11:
            num_ases += 1
        suma += valor

    while suma > 21 and num_ases:
        suma -= 10
        num_ases -= 1

    return suma

def escoger_turno_mostrar_cartas(nombre_p1, nombre_p2, cartas_p1, cartas_p2):
    global turno, plantado_p1, plantado_p2, suma_p1, suma_p2

    turno = random.randint(1, 2)
    suma_p1 = suma_cartas(cartas_p1)
    suma_p2 = suma_cartas(cartas_p2)

    if turno == 1:
        if suma_p1 > 21:
            plantado_p1 = True
            print(f"{nombre_p1} te pasaste! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1} \nMenos -{apuesta_maxima} puntos")
            plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        elif suma_p1 == 21:
            plantado_p1 = True
            print(f"{nombre_p1} tienes BlackJack! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1}")
            plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        else:
            print(f"Empieza {nombre_p1}, tus cartas son: {', '.join(cartas_p1)} y la suma es: {suma_p1}")
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
    else:
        if suma_p2 > 21:
            plantado_p2 = True
            print(f"{nombre_p2} te pasaste! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2} \nMenos -{apuesta_maxima} puntos")
            plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        elif suma_p2 == 21:
            plantado_p2 = True
            print(f"{nombre_p2} tienes BlackJack! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2}")
            plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        else:
            print(f"Empieza {nombre_p2}, tus cartas son: {', '.join(cartas_p2)} y la suma es: {suma_p2}")
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)

def plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2):
    global plantado_p1, plantado_p2

    if plantado_p1 and plantado_p2:
        mostrar_resultados(nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        return

    print("[1] Para pedir carta \n[2] Para plantarse")
    opcion = input("Opción: ")

    if opcion == "1":
        pedir_carta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2)
    elif opcion == "2":
        plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)

def pedir_carta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2):
    global suma_p1, suma_p2, plantado_p1, plantado_p2

    if turno == 1:
        nueva_carta = random.choice(mazo)
        cartas_p1.append(nueva_carta)
        suma_p1 = suma_cartas(cartas_p1)

        if suma_p1 > 21:
            plantado_p1 = True
            print("\n 😵 {} te pasaste! {} la suma de tu mazo es: {} (Menos) -{} puntos 😵".format(nombre_p1, " , ".join(cartas_p1), suma_p1, apuesta_maxima))
            cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2, plantado_p1, plantado_p2)
            return

        if suma_p1 == 21:
            plantado_p1 = True
            print("{} tienes BlackJack! {} la suma de tu mazo es: {}".format(nombre_p1, " , ".join(cartas_p1), suma_p1))
            cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2, plantado_p1, plantado_p2)
            return

        print("\n{} ahora tienes {} y la suma es: {}".format(nombre_p1, " , ".join(cartas_p1), suma_p1))
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)

    else:
        nueva_carta = random.choice(mazo)
        cartas_p2.append(nueva_carta)
        suma_p2 = suma_cartas(cartas_p2)

        if suma_p2 > 21:
            plantado_p2 = True
            print("\n 😵 {} te pasaste! {} la suma de tu mazo es: {} (Menos) -{} puntos 😵".format(nombre_p2, " , ".join(cartas_p2), suma_p2, apuesta_maxima))
            cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2, plantado_p1, plantado_p2)
            return

        if suma_p2 == 21:
            plantado_p2 = True
            print("{} tienes BlackJack! {} la suma de tu mazo es: {}".format(nombre_p2, " , ".join(cartas_p2), suma_p2))
            cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2, plantado_p1, plantado_p2)
            return

        print("\n{} ahora tienes {} y la suma es: {}".format(nombre_p2, " , ".join(cartas_p2), suma_p2))
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)

def plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2):
    global plantado_p1, plantado_p2, creditos_p1, creditos_p2
    ganador = "Indefinido"

    if turno == 1:
        plantado_p1 = True
        print("{} se ha plantado".format(nombre_p1))
    else:
        plantado_p2 = True
        print("{} se ha plantado".format(nombre_p2))

    if plantado_p1 and plantado_p2:
        if suma_p1 > 21:
            ganador = nombre_p2
        elif suma_p2 > 21:
            ganador = nombre_p1
        elif suma_p1 > suma_p2:
            ganador = nombre_p1
        elif suma_p2 > suma_p1:
            ganador = nombre_p2
        elif suma_p1 == suma_p2:
            ganador = "Ambos ganan"
    cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2, plantado_p1, plantado_p2)
    return ganador

def cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2, plantado_p1, plantado_p2):
    if plantado_p1 and plantado_p2:
        mostrar_resultados(nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        return turno

    print("\n    🔃¡CAMBIO DE TURNO!🔃    \n")

    if turno == 1:
        turno = 2
        print("{}, es tu turno. Tus cartas son: {}. La suma de tu mazo es: {}".format(
            nombre_p2, " , ".join(cartas_p2), suma_p2
        ))
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
    else:
        turno = 1
        print("{}, es tu turno. Tus cartas son: {}. La suma de tu mazo es: {}".format(
            nombre_p1, " , ".join(cartas_p1), suma_p1
        ))
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)

    return turno

def mostrar_resultados(nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2):
    global creditos_p1, creditos_p2
    if suma_p1 == 21 and suma_p2 == 21:
        creditos_p1 += 10
        creditos_p2 += 10
        print("\n{} tuvo {} que suman {} \n{} tuvo {} que suman {}"
          .format(nombre_p1, " , ".join(cartas_p1), suma_p1, nombre_p2, " , ".join(cartas_p2), suma_p2))
        print("\n ¡Es un empate, ambos ganan +10 creditos!")
        resultado_en_creditos(nombre_p1, nombre_p2, creditos_p1, creditos_p2)
    else:
        print("\n{} tuvo {} que suman {} \n{} tuvo {} que suman {}"
          .format(nombre_p1, " , ".join(cartas_p1), suma_p1, nombre_p2, " , ".join(cartas_p2), suma_p2))
        resultado_en_creditos(nombre_p1, nombre_p2, creditos_p1, creditos_p2)

def resultado_en_creditos(nombre_p1, nombre_p2, creditos_p1, creditos_p2):
    print("-" * 20)
    print("{} tiene {}".format(nombre_p1, creditos_p1))
    print(" ")
    print("{} tiene {}".format(nombre_p2, creditos_p2))
    print("-" * 20)

iniciar_juego()
