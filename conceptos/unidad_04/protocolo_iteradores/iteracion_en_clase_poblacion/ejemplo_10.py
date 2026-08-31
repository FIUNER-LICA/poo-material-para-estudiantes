# Ejemplo 10: iteracion en una clase personalizada Poblacion.


class Individuo:
    def __init__(self, codigo):
        self.__codigo = codigo

    def __str__(self):
        return "Individuo: " + self.__codigo


class Poblacion:
    def __init__(self):
        self.__individuos = [Individuo("A"), Individuo("B"), Individuo("C")]

    def __iter__(self):
        self.__indice = 0
        return self  # Se retorna a si mismo porque tambien actua como iterador.

    def __next__(self):
        if self.__indice < len(self.__individuos):
            individuo = self.__individuos[self.__indice]
            self.__indice += 1
            return individuo
        raise StopIteration


poblacion = Poblacion()
for individuo in poblacion:
    print(individuo)
