# TODO: Problema 4.
# Diseñe e implemente una aplicación que permita jugar una versión 'Pythonica' del juego
# Black Jack (utilizando un mazo estándar de 52 cartas) con las siguientes especificaciones:
# - Al inicio del juego, se revuelven las cartas y se reparten para dos jugadores.
# - Se escoge aleatoriamente cuál de los dos jugadores hace el primer movimiento.
# - Cada jugador en su turno tiene la opción de tomar una nueva carta o plantarse.
# - Cada jugador tiene 50 créditos para apostar y en cada juego solo apostará hasta 10
# créditos. 
# - El ganador será el jugador que termine con 100 créditos.
# La aplicación debe estar construida usando funciones.
# Ustedes son libres de escoger los elementos gráficos y de jugabilidad que consideren
# adecuados. También son libres de elegir las soluciones que no se encuentren definidas
# dentro de las especificaciones. 

# Metodología
#  El proyecto debe ser desarrollado en grupos de hasta cuatro personas (mínimo tres
# personas).
#  Para cada problema los entregables son:
# 1. Análisis del problema.
# 2. Algoritmo en pseudocódigo.
# 3. Implementación funcional en Python.
# 4. Evidencias de ejecución del programa mediante capturas de pantalla.
# Entregables
#  (30%) Se debe entregar un informe en PDF con los puntos 1,2 y 4 de la metodología.
#  (40%) Código en Python debidamente comentado (notebook de Jupyter) y subido a
# GitHub.
#  (30%) Sustentación: jueves 06 de marzo de 2025 en el horario de clase.

import random

import re

mazo = [
    "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️", "A♠️",
    "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️", "A♦️",
    "2♥️", "3♥️", "4♥️", "5♥️", "6♥️", "7♥️", "8♥️", "9♥️", "10♥️", "J♥️", "Q♥️", "K♥️", "A♥️",
    "2♣️", "3♣️", "4♣️", "5♣️", "6♣️", "7♣️", "8♣️", "9♣️", "10♣️", "J♣️", "Q♣️", "K♣️", "A♣️",
]

turno = 0
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
    nombre_1 = input("El jugador 1 ingresa su nombre: ")
    nombre_2 = input("El jugador 2 ingresa su nombre: ")
    return nombre_1.capitalize(), nombre_2.capitalize()



def repartir_cartas():
    cartas = random.sample(mazo, 4)
    return cartas[:2], cartas[2:]



def valor_carta(carta):
    valor = re.findall(r'\d+|[JQKA]', carta)[0]  # Extrae solo el número o letra
    if valor.isdigit():
        return int(valor)
    elif valor in ['J', 'Q', 'K']:
        return 10
    elif valor == 'A':
        return 11 
    return 0



def suma_cartas(cartas):
    return sum(valor_carta(carta) for carta in cartas)


def escoger_turno_mostrar_cartas(nombre_p1, nombre_p2, cartas_p1, cartas_p2):
    global turno, plantado_p1, plantado_p2, suma_p1, suma_p2

    turno = random.randint(1, 2)
    suma_p1 = suma_cartas(cartas_p1)
    suma_p2 = suma_cartas(cartas_p2)

    if turno == 1:
        if suma_p1 > 21:
            plantado_p1 = True
            print(f"{nombre_p1} te pasaste! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1} \nMenos -{suma_p1} puntos")
        elif suma_p1 == 21:
            plantado_p1 = True
            print(f"{nombre_p1} tienes BlackJack! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1}")
        else:
            print(f"Empieza {nombre_p1}, tus cartas son: {', '.join(cartas_p1)} tienes: {suma_p1}")
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
    else:
        if suma_p2 > 21:
            plantado_p2 = True
            print(f"{nombre_p2} te pasaste! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2} \nMenos -{suma_p2} puntos")
        elif suma_p2 == 21:
            plantado_p2 = True
            print(f"{nombre_p2} tienes BlackJack! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2}")
        else:
            print(f"Empieza {nombre_p2}, tus cartas son: {', '.join(cartas_p2)} tienes: {suma_p2}")
        plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)



def plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2):
    global plantado_p1, plantado_p2

    if suma_p1 == 21 and not plantado_p1:
        plantado_p1 = True
        print(f"¡{nombre_p1} tiene BlackJack! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1}")
    if suma_p2 == 21 and not plantado_p2:
        plantado_p2 = True
        print(f"¡{nombre_p2} tiene BlackJack! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2}")

    if plantado_p1 and plantado_p2:
        ambos_plantados(plantado_p1, plantado_p2, suma_p1, suma_p2, nombre_p1, nombre_p2)
        return

    print("[1] Para pedir carta \n[2] Para plantarse")
    opcion = input("Opción: ")

    if opcion == "1":
        pedir_carta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2)
    elif opcion == "2":
        plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p2, suma_p1)




def pedir_carta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2):
    global suma_p1, suma_p2 

    match turno:
        case 1:
            nueva_carta = mazo[random.randint(0, 51)]
            cartas_p1.append(nueva_carta)
            suma_p1 = suma_cartas(cartas_p1) 

            if suma_p1 > 21:
                global plantado_p1
                plantado_p1 = True
                print(f"{nombre_p1} te pasaste! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1}")
                cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
                return
            
            if suma_p1 == 21:
                plantado_p1 = True
                print(f"{nombre_p1} tienes BlackJack! {', '.join(cartas_p1)} la suma de tu mazo es: {suma_p1}")
                cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2) 
                return

            print(f"{nombre_p1} ahora tienes {', '.join(cartas_p1)} y la suma es: {suma_p1}")
            plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)

        case 2:
            nueva_carta = mazo[random.randint(0, 51)]
            cartas_p2.append(nueva_carta)
            suma_p2 = suma_cartas(cartas_p2) 

            if suma_p2 > 21:
                global plantado_p2
                plantado_p2 = True
                print(f"{nombre_p2} te pasaste! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2}")
                cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
                return
            
            if suma_p2 == 21:
                plantado_p2 = True
                print(f"¡{nombre_p2} tienes BlackJack! {', '.join(cartas_p2)} la suma de tu mazo es: {suma_p2}")
                cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2) 
                return

            print(f"{nombre_p2} ahora tienes {', '.join(cartas_p2)} y la suma es: {suma_p2}")
            plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)




def plantarse(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p2, suma_p1):
    global plantado_p1, plantado_p2

    match turno:
        case 1: 
            plantado_p1 = True
            print("{} se ha plantado".format(nombre_p1))
        case 2: 
            plantado_p2 = True
            print("{} se ha plantado".format(nombre_p2))

    ambos_plantados(plantado_p1, plantado_p2, suma_p1, suma_p2, nombre_p1, nombre_p2)
    cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p2, suma_p1)


        
        
def cambio_de_turno(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p2, suma_p1):
    match turno:
        case 1: 
            turno = 2
            print("{} es tu turno tus cartas son {} la suma de tu maso es {}".format(nombre_p2,  " , ".join(cartas_p2), suma_p2))
            plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)
        case 2: 
            turno = 1
            print("{} es tu turno tus cartas son {} la suma de tu maso es {}".format(nombre_p1, " , ".join(cartas_p1 ), suma_p1))
            plantarse_pedircarta(turno, nombre_p1, nombre_p2, cartas_p1, cartas_p2, suma_p1, suma_p2)


def ambos_plantados(plantado_p1, plantado_p2, suma_p1, suma_p2, nombre_p1, nombre_p2):
    if plantado_p1 and plantado_p2:
        if suma_p1 > suma_p2:
            print(f"Gana {nombre_p1}")
        elif suma_p2 > suma_p1:
            print(f"Gana {nombre_p2}")
        else:
            print("¡Empate!")
        exit() 



        

iniciar_juego()
