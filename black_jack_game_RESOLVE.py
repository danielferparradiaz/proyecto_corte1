import random

# Definir los valores de las cartas
valores_cartas = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
}

palos = ["♠️", "♥️", "♦️", "♣️"]

ronda = 0

def crear_mazo():
    """ Crea y baraja un mazo de cartas. """
    mazo = [(carta, palo) for carta in valores_cartas.keys() for palo in palos]
    random.shuffle(mazo)
    return mazo

def calcular_puntaje(mano):
    total = sum(valores_cartas[carta] for carta, _ in mano)
    ases = sum(1 for carta, _ in mano if carta == "A")
    
    while total > 21 and ases:
        total -= 10  # Convertimos un As de 11 a 1
        ases -= 1
    
    return total

def mostrar_mano(nombre, mano):
    print(f"\n{nombre}: {', '.join(f'{carta}{palo}' for carta, palo in mano)} - Puntaje: {calcular_puntaje(mano)}")

def jugar_blackjack():
    credito_jugador = 50
    credito_computadora = 50
    apuesta = 10  # Apuesta fija
    global ronda
    
    print("\n" + "=" * 60)
    print(" " * 9 + "♠️ ♦️ ♥️ ♣️ ¡BIENVENIDO AL BLACKJACK! ♠️ ♦️ ♥️ ♣️")
    print("=" * 60 + "\n")
    
    while credito_jugador > 0 and credito_computadora > 0:
        ronda += 1
        print("-------------------")
        print("Ronda: #{}".format(ronda))
        
        # Crear y barajar un mazo nuevo en cada ronda
        mazo = crear_mazo()

        # Repartir cartas
        mano_jugador = [mazo.pop(), mazo.pop()]
        mano_computadora = [mazo.pop(), mazo.pop()]
        
        mostrar_mano("Jugador", mano_jugador)
        mostrar_mano("Computadora", mano_computadora)
        
        puntaje_jugador = calcular_puntaje(mano_jugador)
        puntaje_computadora = calcular_puntaje(mano_computadora)
        
        # Verificar Blackjack natural
        if puntaje_jugador == 21 and puntaje_computadora == 21:
            print("\n♦️♠️Empate con Blackjack!♥️♣️")
        elif puntaje_jugador == 21:
            print("\n♦️♠️Jugador gana con Blackjack!♥️♣️")
            credito_jugador += apuesta
            credito_computadora -= apuesta
        elif puntaje_computadora == 21:
            print("\n♦️♠️Computadora gana con Blackjack!♥️♣️")
            credito_jugador -= apuesta
            credito_computadora += apuesta
        else:
            # Turno del jugador
            while puntaje_jugador < 21:
                accion = input("\n¿Quieres pedir carta? (s/n): ").strip().lower()
                if accion == "s":
                    mano_jugador.append(mazo.pop())
                    puntaje_jugador = calcular_puntaje(mano_jugador)
                    mostrar_mano("Jugador", mano_jugador)
                else:
                    break
            
            # Turno de la Computadora
            while puntaje_computadora < 17:
                mano_computadora.append(mazo.pop())
                puntaje_computadora = calcular_puntaje(mano_computadora)
                mostrar_mano("Computadora", mano_computadora)
            
            # Evaluar ganador
            if puntaje_jugador > 21:
                print("\n😭🤭Jugador se pasó. Gana Computadora!😭🤭")
                credito_jugador -= apuesta
                credito_computadora += apuesta
            elif puntaje_computadora > 21 or puntaje_jugador > puntaje_computadora:
                print("\n💥😎Jugador gana!💥😎")
                credito_jugador += apuesta
                credito_computadora -= apuesta
            elif puntaje_computadora > puntaje_jugador:
                print("\n😵🤢Computadora gana!😵🤢")
                credito_jugador -= apuesta
                credito_computadora += apuesta
            else:
                print("\nEmpate!")
        
        print(f"Créditos -> Jugador: {credito_jugador}, Computadora: {credito_computadora}")
        print(" ")
        
        if credito_jugador <= 0:
            print("Te quedaste sin créditos. 🥵 Fin del juego 🥵!")
            break
        elif credito_computadora <= 0:
            print("Computadora se quedó sin créditos. 🏆¡Ganaste el juego!🏆")
            break

jugar_blackjack()
