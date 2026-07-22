from abc import ABC, abstractmethod


class ServicioEmail(ABC):

    @abstractmethod
    def enviar(self, destinatario: str, asunto: str, mensaje: str):
        pass
