"""Reglas educativas para calcular el nivel de riesgo."""


def evaluar_riesgo(indicadores):
    """Suma los puntos y devuelve una clasificación sencilla."""
    puntuacion = sum(item["puntos"] for item in indicadores)

    if puntuacion >= 6:
        nivel = "ALTO"
    elif puntuacion >= 3:
        nivel = "MEDIO"
    else:
        nivel = "BAJO"

    return {"puntuacion": puntuacion, "nivel": nivel}
