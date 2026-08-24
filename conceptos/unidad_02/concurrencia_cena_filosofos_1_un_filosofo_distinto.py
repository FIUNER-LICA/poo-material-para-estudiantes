"""
En este ejemplo se rompe el ciclo de espera.
Implica adoptar una estrategia general para la adiquisición de recursos.
Estrategia: "tomar primero el tenedor de menor valor y luego el de mayor valor"
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
        self.__numero = numero
        self.__tenedor_izquierdo = izquierdo
        self.__tenedor_derecho = derecho

    def comer(self):
        primer_tenedor = self.__tenedor_izquierdo
        segundo_tenedor = self.__tenedor_derecho

        if self.__numero == 4:
            primer_tenedor = self.__tenedor_derecho
            segundo_tenedor = self.__tenedor_izquierdo

        primer_tenedor.levantar()

        time.sleep(0.1)

        segundo_tenedor.levantar()

        print(f"Filósofo {self.__numero} está comiendo. ")

        time.sleep(0.5)

        segundo_tenedor.dejar()
        primer_tenedor.dejar()

    def vivir(self):
        for _ in range(3):
            print(f"Filósofo {self.__numero} está pensando. ")
            time.sleep(0.1)

            self.comer()


if __name__ == "__main__":

    print("Inicia programa...")

    tenedores = [Tenedor(i) for i in range(5)]

    filosofos = []
    for i in range(5):
        f = Filosofo(i, tenedores[i], tenedores[(i + 1) % 5])
        filosofos.append(f)

    hilos = []

    # un hilo hasta aquí
    # separación en hilos que interactúan concurrentemente
    for filosofo in filosofos:
        hilo = threading.Thread(target=filosofo.vivir)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
    # unión de todos los hilos
    # un hilo desde aquí

    print("Fin")