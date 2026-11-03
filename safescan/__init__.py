"""
SafeScan: librería educativa para inspeccionar archivos sin ejecutarlos.
"""

from .informacion import obtener_informacion
from .hash_archivo import calcular_sha256
from .indicadores import buscar_indicadores
from .riesgo import evaluar_riesgo
from .reporte import generar_reporte, exportar_reporte

__all__ = [
    "obtener_informacion",
    "calcular_sha256",
    "buscar_indicadores",
    "evaluar_riesgo",
    "generar_reporte",
    "exportar_reporte",
]
