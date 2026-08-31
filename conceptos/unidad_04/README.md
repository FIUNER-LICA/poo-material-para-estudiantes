# Unidad 4

Esta unidad reune ejemplos simples sobre iteradores, generadores y concurrencia en Python.

## Temas

- Protocolo de iteracion: `iter()`, `next()` y `StopIteration`.
- Generadores con `yield`.
- Comparacion entre ejecucion secuencial, hilos, procesos y `asyncio`.
- Problemas limitados por CPU y por entrada/salida.
- Condiciones de carrera al compartir datos entre hilos.

## Estructura

```text
unidad_04/
+-- protocolo_iteradores/
|   +-- protocolo_iteracion_ejemplos_iniciales/
|   +-- iteracion_en_clase_poblacion/
|   +-- ejemplo_protocolo_iterador_v1.py
|   +-- ejemplo_protocolo_iterador_v2.py
+-- concurrencia/
    +-- caso_contar_palabras_en_archivos/
    +-- caso_descarga_sitios/
    +-- cpubound_problem_sum_numbers_non_concurrent.py
    +-- cpubound_problem_sum_numbers_multiprocessing.py
    +-- race_condition_example.py
    +-- race_condition_example_2.py
    +-- uso_yield.py
```

## Como ejecutar

Desde la raiz del repositorio:

```bash
python conceptos/unidad_04/protocolo_iteradores/protocolo_iteracion_ejemplos_iniciales/ejemplo_1.py
python conceptos/unidad_04/concurrencia/caso_contar_palabras_en_archivos/test_count_words_problem.py
python conceptos/unidad_04/concurrencia/caso_descarga_sitios/test_download_sites_problem.py
python conceptos/unidad_04/concurrencia/cpubound_problem_sum_numbers_non_concurrent.py
python conceptos/unidad_04/concurrencia/cpubound_problem_sum_numbers_multiprocessing.py
```

Para los ejemplos de descarga de sitios, instalar primero las dependencias:

```bash
python -m pip install -r conceptos/unidad_04/concurrencia/caso_descarga_sitios/requirements.txt
```

Luego ejecutar, por ejemplo:

```bash
python conceptos/unidad_04/concurrencia/caso_descarga_sitios/iobound_problem_download_sites_asyncio_version.py
```

## Sugerencia de estudio

1. Ejecutar primero las versiones no concurrentes.
2. Comparar la salida con las versiones usando `threading`, `multiprocessing` y `asyncio`.
3. Observar que no todos los problemas mejoran con la misma tecnica.
4. Modificar la cantidad de datos o repeticiones y volver a medir los tiempos.

## Nota

Los tiempos pueden variar segun la computadora, la version de Python y la conexion a internet.
