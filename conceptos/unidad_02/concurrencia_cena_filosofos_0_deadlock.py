""" 
Ejemplo de interbloqueo (deadlock).
Distintos objetos compitiendo por recursos que nunca se liberan.
Se establece un "ciclo de espera" infinito.
"""

import threading
import time


class Tenedor:
    def __init__(self, numero):
        self.__numero = numero
        self.__lock = threading.Lock()

    def levantar(self):         # levantar tenedor de la mesa
        self.__lock.acquire()

    def dejar(self):            # dejar tenedor en la mesa
        self.__lock.release()

    @property
    def numero(self):
        return self.__numero


class Filosofo:
    def __init__(self, numero, izquierdo, derecho):
        self.numero = numero
        self.tenedor_izquierdo = izquierdo
        self.tenedor_derecho = derecho

    def comer(self):
        print(f"Filósofo {self.numero} intenta tomar "
              f"tenedor {self.tenedor_izquierdo.numero}. ")

        self.tenedor_izquierdo.levantar()

        print(f"Filósofo {self.numero} tomó "
              f"tenedor {self.tenedor_izquierdo.numero}. ")

        time.sleep(0.1)

        print(f"Filósofo {self.numero} intenta tomar "
              f"tenedor {self.tenedor_derecho.numero}. ")

        self.tenedor_derecho.levantar()

        print(f"Filósofo {self.numero} está comiendo. ")

        time.sleep(0.5)

        self.derecho.dejar()
        self.izquierdo.dejar()

        print(f"Filósofo {self.numero} terminó de comer. ")

    def vivir(self):
        for _ in range(3):
            print(f"Filósofo {self.numero} está pensando. ")
            time.sleep(0.1)

            self.comer()


if __name__ == "__main__":

    print("Inicia programa...")

    tenedores = [Tenedor(i) for i in range(5)]

    filosofos = [
        Filosofo(
            i,
            tenedores[i],
            tenedores[(i + 1) % 5]
        )
        for i in range(5)
    ]

    hilos = []

    for filosofo in filosofos:
        hilo = threading.Thread(target=filosofo.vivir)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("Fin")