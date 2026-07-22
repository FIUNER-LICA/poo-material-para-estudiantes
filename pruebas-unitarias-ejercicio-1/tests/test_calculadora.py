import unittest
from modules.calculadora import Calculadora


class TestDividir(unittest.TestCase):
    def test_1(self):
        """División normal"""
        numerador = ... # TODO: Reemplazar `...` por un valor apropiado.
        denominador = ... # TODO: Reemplazar `...` por un valor apropiado.
        resultado = ... # TODO: Reemplazar `...` por un valor apropiado.
        self.assertEqual(Calculadora.dividir(numerador, denominador), resultado)

    def test_2(self):
        """Numerador igual a cero"""
        numerador = ... # TODO: Reemplazar `...` por un valor apropiado.
        denominador = ... # TODO: Reemplazar `...` por un valor apropiado.
        resultado = ... # TODO: Reemplazar `...` por un valor apropiado.
        self.assertEqual(Calculadora.dividir(numerador, denominador), resultado)

    def test_3(self):
        """Divisor igual a uno"""
        numerador = ... # TODO: Reemplazar `...` por un valor apropiado.
        denominador = ... # TODO: Reemplazar `...` por un valor apropiado.
        resultado = ... # TODO: Reemplazar `...` por un valor apropiado.
        self.assertEqual(Calculadora.dividir(numerador, denominador), resultado)

    def test_4(self):
        """Resultado negativo"""
        numerador = ... # TODO: Reemplazar `...` por un valor apropiado.
        denominador = ... # TODO: Reemplazar `...` por un valor apropiado.
        self.assertLess(Calculadora.dividir(numerador, denominador), 0)

    def test_5(self):
        """Ambos operandos negativos"""
        numerador = ... # TODO: Reemplazar `...` por un valor apropiado.
        denominador = ... # TODO: Reemplazar `...` por un valor apropiado.
        self.assertGreater(Calculadora.dividir(numerador, denominador), 0)

    def test_6(self):
        """División por cero"""
        numerador = ... # TODO: Reemplazar `...` por un valor apropiado.
        denominador = ... # TODO: Reemplazar `...` por un valor apropiado.
        excepcion = ... # TODO: Reemplazar `...` por un valor apropiado.
        with self.assertRaises(excepcion):
            Calculadora.dividir(numerador, denominador)


if __name__ == "__main__":
    unittest.main()
