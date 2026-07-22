from modules.usuario import Usuario
from modules.repositorio_usuarios import RepositorioUsuarios


class RepositorioUsuariosStub(RepositorioUsuarios):
    def guardar(self, usuario: Usuario):
        pass # TODO: Reemplazar `pass` por la implementación del método.

    def buscar_por_nombre(self, nombre):
        pass # TODO: Reemplazar `pass` por la implementación del método.
