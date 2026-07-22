class Usuario:

    def __init__(self, nombre: str, password: str):
        self._nombre = nombre
        self._password = password

    @property
    def nombre(self):
        return self._nombre

    @property
    def password(self):
        return self._password
