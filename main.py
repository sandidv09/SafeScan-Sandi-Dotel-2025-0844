"""Programa principal de SafeScan: interfaz sencilla por consola."""

from pathlib import Path

from safescan import (
    obtener_informacion,
    calcular_sha256,
    buscar_indicadores,
    evaluar_riesgo,
    generar_reporte,
    exportar_reporte,
)


def analizar_archivo(ruta):
    """Coordina los módulos y devuelve el reporte generado."""
    informacion = obtener_informacion(ruta)
    hash_sha256 = calcular_sha256(ruta)
    indicadores = buscar_indicadores(ruta)
    evaluacion = evaluar_riesgo(indicadores)

    reporte = generar_reporte(
        informacion, hash_sha256, indicadores, evaluacion
    )
    return reporte


def main():
    print("=" * 48)
    print("             SAFESCAN - ANALIZADOR")
    print("=" * 48)
    ruta = input("Introduce la ruta del archivo que deseas analizar: ").strip().strip('"')

    try:
        reporte = analizar_archivo(ruta)
        print("\n" + reporte)

        nombre = Path(ruta).stem
        ruta_reporte = Path.cwd() / f"reporte_{nombre}.txt"
        ruta_guardada = exportar_reporte(reporte, ruta_reporte, ruta_analizada=ruta)

        print(f"\nReporte exportado correctamente: {ruta_guardada}")

    except FileNotFoundError as error:
        print(f"ERROR: {error}")
    except (ValueError, PermissionError, OSError) as error:
        print(f"ERROR durante el análisis: {error}")


if __name__ == "__main__":
    main()
