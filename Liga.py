import random
import numpy as np

# Definición de la clase Equipo
class Equipo:
    def __init__(self, nombre, lambda_ofensiva, lambda_defensiva):
        self.nombre = nombre
        self.lambda_ofensiva = lambda_ofensiva  # Goles anotados por partido
        self.lambda_defensiva = lambda_defensiva  # Goles concedidos por partido
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.partidos_jugados = 0

    def actualizar_puntos(self, goles_favor, goles_contra):
        if goles_favor > goles_contra:
            self.puntos += 3
        elif goles_favor == goles_contra:
            self.puntos += 1

        self.goles_a_favor += goles_favor
        self.goles_en_contra += goles_contra
        self.partidos_jugados += 1  # Incrementar partidos jugados


# Definición de la clase Partido


class Partido:
    def __init__(self, equipo_local, equipo_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante

    def jugar(self):
        # Calcular lambda para cada equipo
        lambda_local = self.equipo_local.lambda_ofensiva * self.equipo_visitante.lambda_defensiva
        lambda_visitante = self.equipo_visitante.lambda_ofensiva * self.equipo_local.lambda_defensiva

        # Generar goles usando Poisson
        goles_local = np.random.poisson(lambda_local)
        goles_visitante = np.random.poisson(lambda_visitante)

        # Actualizar estadísticas
        self.equipo_local.actualizar_puntos(goles_local, goles_visitante)
        self.equipo_visitante.actualizar_puntos(goles_visitante, goles_local)

        # Mostrar resultado
        print(f"{self.equipo_local.nombre} {goles_local} - {self.equipo_visitante.nombre} {goles_visitante}")


# Definición de la clase Liga
class Liga:
    def __init__(self, equipos):
        self.equipos = equipos

    def todos_contra_todos(self):
        for i in range(len(self.equipos)):
            for j in range(i + 1, len(self.equipos)):
                # Primer partido: equipo[i] vs equipo[j] (local vs visitante)
                partido1 = Partido(self.equipos[i], self.equipos[j])
                partido1.jugar()

                # Segundo partido: equipo[j] vs equipo[i] (local vs visitante)
                partido2 = Partido(self.equipos[j], self.equipos[i])
                partido2.jugar()

    def table_posiciones(self):
        # Ordenar equipos por puntos de mayor a menor
        self.equipos.sort(key=lambda x: x.puntos, reverse=True)

        # Imprimir la tabla de posiciones
        print("\nTabla de posiciones:")
        print("-" * 80)
        print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format("Pos", "Equipo", "PJ", "Puntos", "GF", "GC"))
        print("-" * 80)
        for i, equipo in enumerate(self.equipos, start=1):
            print("{:<5} {:<20} {:<10} {:<10} {:<10} {:<10}".format(i, equipo.nombre, equipo.partidos_jugados,  equipo.puntos, equipo.goles_a_favor, equipo.goles_en_contra))
        print("-" * 80)


# Bloque principal para ejecutar el programa
if __name__ == "__main__":
    # Crear los 20 equipos con tasas realistas
    equipos = [
        Equipo("Real Madrid", 1.9, 0.8),
        Equipo("Barcelona", 2.1, 0.7),
        Equipo("Atlético de Madrid", 1.8, 0.9),
        Equipo("Sevilla", 1.5, 1.1),
        Equipo("Valencia", 1.4, 1.3),
        Equipo("Villarreal", 1.6, 1.2),
        Equipo("Real Sociedad", 1.5, 1.0),
        Equipo("Real Betis", 1.4, 1.2),
        Equipo("Athletic Club", 1.3, 1.1),
        Equipo("Granada", 1.2, 1.4),
        Equipo("Celta de Vigo", 1.3, 1.5),
        Equipo("Levante", 1.1, 1.6),
        Equipo("Getafe", 1.0, 1.3),
        Equipo("Alavés", 1.0, 1.5),
        Equipo("Osasuna", 1.1, 1.4),
        Equipo("Cádiz", 0.9, 1.6),
        Equipo("Elche", 0.8, 1.7),
        Equipo("Rayo Vallecano", 1.2, 1.5),
        Equipo("Mallorca", 0.9, 1.6),
        Equipo("Espanyol", 1.0, 1.5),
    ]

    # Crear una liga con los 20 equipos
    liga = Liga(equipos)

    # Jugar todos contra todos
    liga.todos_contra_todos()

    # Mostrar la tabla de posiciones
    liga.table_posiciones()