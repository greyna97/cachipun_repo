from src.models.Cachipun import Cachipun

cachipun_var = Cachipun()
# soy el hijo de > Cachipun

print(cachipun_var)

cachipun_var.decir_hola()


contador_partidas = 0
contador_victorias_jugador = 0
contador_victorias_maquina = 0
contador_empates = 0

while True:
    # Desde aca, por que aca la maquina elige su jugada
    eleccion_maquina = cachipun_var.jugada_de_la_maquina()
    jugada = input("elige una opcion piedra, papel, tijera: ")
    eleccion_jugador = cachipun_var.jugada_del_jugador(jugada)
    if eleccion_jugador == "Opcion no valida":
        print("La opcion no es valida")
        continue

    print("La jugada del jugador es", eleccion_jugador)
    print("La jugada de la maquina es", eleccion_maquina)

    entrada_jugada = cachipun_var.comparacion_jugadas(eleccion_jugador, eleccion_maquina)
    print(f" {entrada_jugada}")
    if "Jugador" in entrada_jugada:
        contador_victorias_jugador += 1
    elif "Maquina" in entrada_jugada:
        contador_victorias_maquina += 1
    else:
        contador_empates += 1
    contador_partidas += 1

    # Validacion para salir del while
    if contador_victorias_jugador <= 1 or contador_victorias_maquina <= 1:
        break
    # Finaliza aca

print("El juego ha terminado")
print(f"El jugador gano {contador_victorias_jugador}")
print(f"La maquina gano {contador_victorias_maquina}")
print(f"Hubo {contador_empates} empates")
