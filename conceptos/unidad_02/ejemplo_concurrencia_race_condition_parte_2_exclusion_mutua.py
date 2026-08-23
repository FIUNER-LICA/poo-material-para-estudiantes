import threading
import time


class C:
    def __init__(self):
        self.valor = 0
        self.__lock = threading.Lock()

    def incrementar(self):
        with self.__lock:         # excluye ejecución simultánea dentro del ámbito with            valor_actual = self.__valor
            valor_actual = self.valor
            time.sleep(0.0001)
            self.__valor = valor_actual + 1
    
    def decrementar(self):
        with self.__lock:
            valor_actual = self.__valor
            time.sleep(0.0001)
            self.__valor = valor_actual - 1


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
a = A(c)
b = B(c)

# Cada objeto activo se ejecuta en un hilo
hilo_a = threading.Thread(target=a.ejecutar)
hilo_b = threading.Thread(target=b.ejecutar)

hilo_a.start()
hilo_b.start()

hilo_a.join()
hilo_b.join()

print("Valor esperado: 0")
print("Valor obtenido:", c.valor)