# SafeScan — Analizador básico de archivos

SafeScan es un proyecto educativo en Python que inspecciona archivos sin ejecutarlos, modificarlos ni eliminarlos. Busca algunas cadenas configuradas como indicadores, calcula SHA-256 y genera un reporte de texto.

> **Importante:** encontrar una cadena no significa que un archivo sea malware. Esta herramienta no es un antivirus y no garantiza detectar programas maliciosos.

## Requisitos

- Python 3.8 o superior.
- No necesita instalar librerías externas; utiliza únicamente la biblioteca estándar.

## Estructura

```text
SafeScan/
├── safescan/
│   ├── __init__.py
│   ├── informacion.py
│   ├── hash_archivo.py
│   ├── indicadores.py
│   ├── riesgo.py
│   └── reporte.py
├── pruebas/
│   ├── archivo_normal.txt
│   └── archivo_sospechoso.txt
├── main.py
└── README.md
```

## Ejecutar el programa

Abre una terminal en la carpeta `SafeScan` y ejecuta:

```bash
python main.py
```

Cuando lo solicite, introduce la ruta del archivo. Para probar los archivos incluidos puedes escribir:

```text
pruebas/archivo_normal.txt
```

o:

```text
pruebas/archivo_sospechoso.txt
```

El programa presenta los resultados en consola y crea un archivo `reporte_NOMBRE.txt` en la carpeta desde la que se ejecutó.

## Reglas de puntuación

| Indicador | Puntos por coincidencia |
|---|---:|
| `powershell` | 3 |
| `cmd.exe` | 2 |
| `subprocess` | 2 |
| `os.system` | 2 |
| `eval(` | 3 |
| `base64` | 1 |

- 0 a 2 puntos: riesgo bajo.
- 3 a 5 puntos: riesgo medio.
- 6 puntos o más: riesgo alto.

Son reglas creadas para esta práctica. La puntuación aumenta por cada aparición del indicador.

## Reutilizar la librería desde otro archivo

Con la carpeta `SafeScan` en el mismo directorio que el archivo que la utilizará, se pueden importar sus funciones así:

```python
from safescan import (
    obtener_informacion,
    calcular_sha256,
    buscar_indicadores,
    evaluar_riesgo,
)

ruta = "pruebas/archivo_sospechoso.txt"

informacion = obtener_informacion(ruta)
huella = calcular_sha256(ruta)
indicadores = buscar_indicadores(ruta)
riesgo = evaluar_riesgo(indicadores)

print(informacion)
print("SHA-256:", huella)
print("Indicadores:", indicadores)
print("Evaluación:", riesgo)
```

Esto demuestra que otra persona puede importar y reutilizar las funciones del paquete sin copiar el código de cada módulo.

## Responsabilidad de cada módulo

- `informacion.py`: valida la ruta y obtiene nombre, extensión y tamaño.
- `hash_archivo.py`: calcula SHA-256 leyendo el archivo en bloques.
- `indicadores.py`: busca las cadenas definidas en el contenido.
- `riesgo.py`: suma los puntos y determina el nivel.
- `reporte.py`: construye y exporta el reporte TXT.
- `__init__.py`: expone las funciones principales del paquete.
- `main.py`: coordina los módulos y gestiona la interacción por consola.

## Seguridad y limitaciones

- El archivo se abre únicamente para lectura.
- No se ejecutan instrucciones encontradas en el contenido.
- No se modifica ni elimina el archivo analizado.
- Los archivos se inspeccionan como texto UTF-8; los bytes que no puedan decodificarse se sustituyen para poder continuar la búsqueda.
- La búsqueda es simple y no identifica malware real. Puede producir falsos positivos y no detectar amenazas.
