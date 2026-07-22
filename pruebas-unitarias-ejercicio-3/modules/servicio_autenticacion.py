class ServicioAutenticacion:

    def __init__(self, repositorio):
        self._repositorio = repositorio

    def autenticar(self, usuario: str, password: str):

        u = self._repositorio.buscar_por_nombre(usuario)

        if u is None:
            return False

        return u.password == password
