"""Funciones para consultar los datos básicos de un archivo."""

from pathlib import Path


def obtener_informacion(ruta):
    """Devuelve nombre, extensión, tamaño y ruta de un archivo existente."""
    archivo = Path(ruta).expanduser()

    if not archivo.exists():
        raise FileNotFoundError(f"No existe el archivo: {archivo}")
    if not archivo.is_file():
        raise ValueError("La ruta indicada no corresponde a un archivo.")

    try:
        return {
            "nombre": archivo.name,
            "extension": archivo.suffix or "(sin extensión)",
            "tamano": archivo.stat().st_size,
            "ruta": str(archivo.resolve()),
        }
    except OSError as error:
        raise OSError(f"No se pudo consultar el archivo: {error}") from error
