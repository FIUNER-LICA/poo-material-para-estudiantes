"""
Ejemplo polimorfismo con elementos de Ciencias de Datos
"""

from abc import ABC, abstractmethod


class ModeloPredictor(ABC):
    @abstractmethod
    def predecir(self, X):
        pass


class RegresionLineal(ModeloPredictor):
    def __init__(self, w, b):
        self.__w = w
        self.__b = b

    def predecir(self, X):
        return [self.__w * x + self.__b for x in X]


class ArbolDecision(ModeloPredictor):
    def predecir(self, X):
        return ["Clase A" if x > 5 else "Clase B" for x in X]

# Definición de nuevos modelos: 

# Modelo Constante 
class ModeloConstante(ModeloPredictor): 
    def __init__(self, valor):
        self.__valor = valor 

    def predecir(self, X):
        return [self.__valor for _ in X]

# Modelo de Red Neuronal 
class RedNeuronal(ModeloPredictor):
    def predecir(self, X):
        # Implementación simplificada
        return ["Clase X" if x > 7 else "Clase Y" for x in X]


def evaluar_modelos(modelos, datos):
    for modelo in modelos:
        predicciones = modelo.predecir(datos)

        print(f"{modelo.__class__.__name__}")
        print(f"  Datos:         {datos}")
        print(f"  Predicciones:  {predicciones}")
        print()


datos = [2, 6, 8]

modelos = [
    RegresionLineal(w=2, b=1),
    ArbolDecision(),
    ModeloConstante(valor=10), 
    RedNeuronal()
]

evaluar_modelos(modelos, datos)