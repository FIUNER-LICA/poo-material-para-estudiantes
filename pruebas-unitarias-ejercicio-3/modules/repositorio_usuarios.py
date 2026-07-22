from abc import ABC, abstractmethod
from modules.usuario import Usuario


class RepositorioUsuarios(ABC):

    @abstractmethod
    def guardar(self, usuario: Usuario):
        pass

    @abstractmethod
    def buscar_por_nombre(self, nombre: str):
        pass
