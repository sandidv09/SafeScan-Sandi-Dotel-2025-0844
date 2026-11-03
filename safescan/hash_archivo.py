"""Cálculo de la huella digital SHA-256."""

import hashlib


def calcular_sha256(ruta):
    """Calcula SHA-256 leyendo el archivo por bloques, sin modificarlo."""
    sha256 = hashlib.sha256()

    try:
        with open(ruta, "rb") as archivo:
            for bloque in iter(lambda: archivo.read(4096), b""):
                sha256.update(bloque)
    except OSError as error:
        raise OSError(f"No se pudo leer el archivo para calcular SHA-256: {error}") from error

    return sha256.hexdigest()
