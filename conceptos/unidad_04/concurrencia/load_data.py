
from pathlib import Path


def load_filenames(paths):
    """Devuelve los archivos encontrados en las carpetas indicadas.

    Se ordenan para que las mediciones sean comparables entre ejecuciones.
    Si una carpeta no existe, se informa con un error claro para el estudiante.
    """
    filenames = []
    for path in paths:
        directory = Path(path)
        if not directory.exists():
            raise FileNotFoundError(f"No existe la carpeta de datos: {directory}")
        filenames.extend(str(file) for file in sorted(directory.iterdir()) if file.is_file())
    return filenames
