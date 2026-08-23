import threading
import time


class C:
    def __init__(self):
        self.__valor = 0

    def incrementar(self):
        valor_actual = self.__valor
        time.sleep(0.0001)  # Simula una interrupción u operación lenta
        self.__valor = valor_actual + 1

    def decrementar(self):
        valor_actual = self.__valor
        time.sleep(0.0001)  # Simula una interrupción u operación lenta
        self.__valor = valor_actual - 1

    @property
    def valor(self):
        return self.__valor


class A:
    def __init__(self, objeto_c):
        self.__obj_C = objeto_c

    def ejecutar(self):
        for _ in range(1000):
            self.__obj_C.incrementar()


class B:
    def __init__(self, objeto_c):
        self.__obj_C = objeto_c

    def ejecutar(self):
        for _ in range(1000):
            self.__obj_C.decrementar()


# Objeto compartido
c = C()

# Objetos activos
a = A(c)    # incrementa
b = B(c)    # decrementa

# Cada objeto activo se ejecuta en un hilo
hilo_a = threading.Thread(target=a.ejecutar)
hilo_b = threading.Thread(target=b.ejecutar)

hilo_a.start()
hilo_b.start()

hilo_a.join()
hilo_b.join()

print("Valor esperado: 0")
print("Valor obtenido:", c.valor)