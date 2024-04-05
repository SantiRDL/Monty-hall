import random

def monty_hall(cambiar_puerta, imprimir):
    # Seleccionar aleatoriamente la puerta donde está el auto
    puerta_auto = random.randint(1, 3)

    # El participante elige una puerta aleatoria
    puerta_elegida = random.randint(1, 3)

    # El presentador elige una de las puertas restantes que no tiene el auto ni fue elegida por el participante
    puertas_disponibles = [1, 2, 3]
    puertas_disponibles.remove(puerta_auto)
    if puerta_elegida in puertas_disponibles:
        puertas_disponibles.remove(puerta_elegida)
    puerta_abierta = random.choice(puertas_disponibles)

    # Si el participante decide cambiar de puerta
    if cambiar_puerta:
        puertas_disponibles = [1, 2, 3]
        puertas_disponibles.remove(puerta_elegida)
        puertas_disponibles.remove(puerta_abierta)
        puerta_elegida = puertas_disponibles[0]

    if imprimir == True:
        # Imprimir detalles del juego
        print("------------------------")
        print("Puerta elegida por el participante:", puerta_elegida)
        print("Puerta donde está el auto:", puerta_auto)
        print("Puerta abierta por el presentador:", puerta_abierta)

        if cambiar_puerta == True:
            print ("El participante cambió de puerta")
        else:
            print("El participante no cambió de puerta")
        

        # Determinar si el participante ganó el auto
        if puerta_elegida == puerta_auto:
            print("El participante gana el auto!")
            print("------------------------")
            return True
        else:
            print("El participante no gana el auto.")
            print("------------------------")
    else:
        if puerta_elegida == puerta_auto:
            return True



def simulacion_monty_hall(cambiar_puerta, num_intentos, imprimir):
    ganadas = 0
    perdidas = 0

    for intentos in range(num_intentos):
        puerta_ganadora = monty_hall(cambiar_puerta, imprimir)
        if puerta_ganadora == True:
            ganadas += 1
        else:
            perdidas += 1

    print("Veces ganadas:", ganadas)
    print("Veces perdidas:", perdidas)

# Ejemplo de uso
cambiar_puerta = False  # Cambiar de puerta
num_intentos = 100000
imprimir = False
simulacion_monty_hall(cambiar_puerta, num_intentos, imprimir)





       