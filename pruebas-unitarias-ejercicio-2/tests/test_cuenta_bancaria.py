import unittest
from modules.cuenta_bancaria import CuentaBancaria


class TestSaldoInicial(unittest.TestCase):
    def test_saldo_inicial_negativo(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_saldo_inicial_cero(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.


class TestDeposito(unittest.TestCase):
    def setUp(self):
        self._monto = 1000
        self._cuenta_bancaria = CuentaBancaria(saldo_inicial=0)

    def test_deposito_positivo(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_deposito_cero(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_deposito_negativo(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.


class TestRetiro(unittest.TestCase):
    def setUp(self):
        self._monto = 1000
        self._cuenta_bancaria = CuentaBancaria(saldo_inicial=self._monto)

    def test_retiro_válido(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_retiro_igual_al_saldo(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_retiro_mayor_al_saldo(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_retiro_cero(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_retiro_negativo(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.


class TestTransferencia(unittest.TestCase):
    def setUp(self):
        self._monto_inicial = 1000
        self._cuenta_bancaria_origen = CuentaBancaria(saldo_inicial=self._monto_inicial)
        self._cuenta_bancaria_destino = CuentaBancaria(saldo_inicial=0)

    def test_transferencia_valida(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_transferencia_monto_invalido(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_transferencia_con_cuenta_destino_nula(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.


if __name__ == "__main__":
    unittest.main()
