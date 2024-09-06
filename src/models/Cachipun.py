import random


class Cachipun:

    # Initialize the class
    def __init__(self):
        print("Hola saludos desde la clase Cachipun")
        pass

    def decir_hola(self):
        print("Hola desde la clase Cachipun")

    """
        Que queremos hacer: que la maquina juegue conmigo
        - Ingresar mi jugada Lista
        - La maquina elige una jugada Lista
        - Comparar las jugadas
        - Decidir quien gana
    """

    def jugada_de_la_maquina(self):
        jugadas_permitidas = ["piedra", "papel", "tijera"]
        jugada_seleccionada = random.choice(jugadas_permitidas)
        return jugada_seleccionada

    def jugada_del_jugador(self, opcion_del_usuario):
        opciones_valida = ["piedra", "papel", "tijera"]
        # Opcion larga
        # for opcion in opciones_valida:
        #     if opcion_del_usuario == opcion:
        #         print("opcion valida")
        #         break
        if opcion_del_usuario.lower() not in opciones_valida:
            return "Opcion no valida"
        return opcion_del_usuario.lower()

    def comparacion_jugadas(self, opcion_jugador, opcion_maquina):
        # la key - la lista a los que les gana
        lista_ganador = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}
        if opcion_jugador == opcion_maquina:
            return "Empate"
        if lista_ganador[opcion_jugador] == opcion_maquina:
            return "Gana El Jugador"
        elif lista_ganador[opcion_maquina] == opcion_jugador:
            return "Gana La Maquina"
