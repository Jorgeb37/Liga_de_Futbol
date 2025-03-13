import random

# Definición de la clase Equipo
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.goles_a_favor = 0
        self.goles_en_contra = 0
        self.partidos_jugados = 0  # Nuevo atributo

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
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def jugar(self):
        # Generar goles aleatorios para ambos equipos
        goles_equipo1 = random.randint(0, 7)
        goles_equipo2 = random.randint(0, 7)

        # Actualizar puntos y goles de los equipos
        self.equipo1.actualizar_puntos(goles_equipo1, goles_equipo2)
        self.equipo2.actualizar_puntos(goles_equipo2, goles_equipo1)

        # Mostrar el resultado del partido
        print(f"{self.equipo1.nombre} {goles_equipo1} - {self.equipo2.nombre} {goles_equipo2}")


# Definición de la clase Liga
class Liga:
    def __init__(self, equipos):
        self.equipos = equipos

    def todos_contra_todos(self):
        for i in range(len(self.equipos)):
            for j in range(i + 1, len(self.equipos)):
                partido = Partido(self.equipos[i], self.equipos[j])
                partido.jugar()

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
    # Crear algunos equipos
    equipo_a = Equipo("Real Madrid")
    equipo_b = Equipo("Barcelona")
    equipo_c = Equipo("Atlético de Madrid")
    equipo_d = Equipo("Sevilla")
    equipo_e = Equipo("Valencia")  # Nuevo equipo
    equipo_f = Equipo("Villarreal")  # Nuevo equipo
    equipo_g = Equipo("Real Sociedad")  # Nuevo equipo

    # Crear una liga con los equipos
    liga = Liga([equipo_a, equipo_b, equipo_c, equipo_d, equipo_e, equipo_f, equipo_g])

    # Jugar todos contra todos
    liga.todos_contra_todos()

    # Mostrar la tabla de posiciones
    liga.table_posiciones()