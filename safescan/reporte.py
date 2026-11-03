"""Construcción, visualización y exportación del reporte.""" 

from pathlib import Path


def generar_reporte(informacion, hash_sha256, indicadores, evaluacion):
    """Construye el reporte como texto para mostrarlo o guardarlo."""
    lineas = [
        "=" * 48,
        "             SAFESCAN - ANALIZADOR",
        "=" * 48,
        f"Archivo: {informacion['nombre']}",
        f"Extensión: {informacion['extension']}",
        f"Tamaño: {informacion['tamano']} bytes",
        f"Ruta: {informacion['ruta']}",
        "",
        "SHA-256:",
        hash_sha256,
        "",
        "INDICADORES ENCONTRADOS:",
    ]

    if indicadores:
        for item in indicadores:
            lineas.append(
                f"- {item['indicador']} | coincidencias: {item['cantidad']} "
                f"| puntos: {item['puntos']}"
            )
    else:
        lineas.append("- No se encontraron indicadores definidos.")

    lineas.extend([
        "",
        f"Puntuación total: {evaluacion['puntuacion']} puntos",
        f"Nivel de riesgo: {evaluacion['nivel']}",
        "",
        "Nota: los indicadores y puntuaciones son reglas educativas.",
        "Un indicador encontrado no demuestra que el archivo sea malicioso.",
        "El análisis fue estático: el archivo no fue ejecutado ni modificado.",
        "=" * 48,
    ])

    return "\n".join(lineas)


def exportar_reporte(contenido, ruta_salida, ruta_analizada=None):
    """Guarda el reporte TXT y evita sobrescribir el archivo analizado."""
    destino = Path(ruta_salida).expanduser()
    destino.parent.mkdir(parents=True, exist_ok=True)

    if ruta_analizada is not None:
        try:
            if destino.resolve() == Path(ruta_analizada).expanduser().resolve():
                destino = destino.with_name(destino.stem + "_analisis" + destino.suffix)
        except OSError:
            pass

    try:
        destino.write_text(contenido, encoding="utf-8")
    except OSError as error:
        raise OSError(f"No se pudo exportar el reporte: {error}") from error

    return str(destino.resolve())
