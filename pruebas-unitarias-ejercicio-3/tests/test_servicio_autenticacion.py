import unittest
from unittest.mock import Mock

from modules.servicio_autenticacion import ServicioAutenticacion
from modules.usuario import Usuario
from tests.stubs.repositorio_usuarios_stub import RepositorioUsuariosStub


class TestAutenticarMock(unittest.TestCase):
    """Test del método autenticar con repositorio de usuarios como mock"""

    def setUp(self):
        self._usuario = "josé"
        self._password = "1234"
        repo = Mock()
        repo.buscar_por_nombre.return_value = Usuario(self._usuario, self._password)
        self._servicio = ServicioAutenticacion(repo)

    def test_usuario_password_correcto(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_usuario_password_incorrecto(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.


class TestAutenticarStub(unittest.TestCase):
    """Test del método autenticar con repositorio de usuarios como stub"""

    def setUp(self):
        self._usuario = "josé"
        self._password = "1234"
        repo = RepositorioUsuariosStub()
        repo.guardar(Usuario(self._usuario, self._password))
        self._servicio = ServicioAutenticacion(repo)

    def test_usuario_password_correcto(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.

    def test_usuario_password_incorrecto(self):
        pass # TODO: Reemplazar `pass` por la implementación de la prueba unitaria.


if __name__ == "__main__":
    unittest.main()
