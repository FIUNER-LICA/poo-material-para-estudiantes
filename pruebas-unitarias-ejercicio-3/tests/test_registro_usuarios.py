import unittest
from unittest.mock import Mock
from modules.registro_usuarios import RegistroUsuarios


class TestRegistrar(unittest.TestCase):
    def setUp(self):
        self._repo = Mock()
        self._email = Mock()
        self._registro = RegistroUsuarios(self._repo, self._email)

    def test_registrar_usuario(self):
        self._registro.registrar("juan", "1234", "juan@gmail.com")
        self._repo.guardar.assert_called_once()
        self._email.enviar.assert_called_once_with(
            "juan@gmail.com", "Bienvenido", "Su cuenta fue creada."
        )


if __name__ == "__main__":
    unittest.main()
