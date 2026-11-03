"""Búsqueda de cadenas que el proyecto considera potencialmente sospechosas."""

INDICADORES = {
    "powershell": 3,
    "cmd.exe": 2,
    "subprocess": 2,
    "os.system": 2,
    "eval(": 3,
    "base64": 1,
}


def buscar_indicadores(ruta):
    """
    Busca indicadores en el contenido como texto.
    No ejecuta ni modifica el archivo. Los archivos no UTF-8 se leen
    reemplazando los bytes que no puedan convertirse a texto.
    """
    try:
        with open(ruta, "rb") as archivo:
            contenido = archivo.read().decode("utf-8", errors="replace").lower()
    except OSError as error:
        raise OSError(f"No se pudo leer el contenido del archivo: {error}") from error

    encontrados = []
    for indicador, puntos in INDICADORES.items():
        cantidad = contenido.count(indicador.lower())
        if cantidad > 0:
            encontrados.append({
                "indicador": indicador,
                "cantidad": cantidad,
                "puntos": puntos * cantidad,
            })

    return encontrados
