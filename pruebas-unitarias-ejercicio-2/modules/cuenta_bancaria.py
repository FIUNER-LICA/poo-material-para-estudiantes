class CuentaBancaria:

    def __init__(self, saldo_inicial: float):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self._saldo = saldo_inicial

    @property
    def saldo(self) -> float:
        return self._saldo

    def depositar(self, monto: float):
        if monto < 0:
            raise ValueError("Monto inválido")
        self._saldo += monto

    def retirar(self, monto: float):
        if monto < 0:
            raise ValueError("Monto inválido")

        if monto >= self._saldo:
            raise ValueError("Fondos insuficientes")

        self._saldo -= monto

    def transferir(self, destino: CuentaBancaria, monto: float):
        self.retirar(monto)
        destino.depositar(monto)
