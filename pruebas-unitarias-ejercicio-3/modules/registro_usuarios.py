from modules.usuario import Usuario
from modules.repositorio_usuarios import RepositorioUsuarios
from modules.servicio_de_correo import ServicioEmail


class RegistroUsuarios:

    def __init__(self, repositorio: RepositorioUsuarios, servicio_email: ServicioEmail):
        self._repositorio = repositorio
        self._servicio_email = servicio_email

    def registrar(self, nombre: str, password: str, correo: str):

        usuario = Usuario(nombre, password)

        self._repositorio.guardar(usuario)

        self._servicio_email.enviar(correo, "Bienvenido", "Su cuenta fue creada.")
