class Calculadora:
    @staticmethod
    def dividir(numerador: float, denominador: float) -> float:
        if denominador == 0:
            raise ValueError("División por cero")
        return numerador / denominador
