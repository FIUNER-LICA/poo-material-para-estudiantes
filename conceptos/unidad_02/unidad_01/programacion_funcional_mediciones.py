"""Ejemplo introductorio de programacion funcional con mediciones.

El programa muestra, sobre un mismo conjunto de datos:

- funciones puras;
- transformaciones sin modificar los datos originales;
- funciones como valores y funciones de orden superior;
- filter y map;
- composicion de transformaciones;
- calculo de la temperatura promedio de las mediciones validas.

No se informa una suma de temperaturas porque, por si sola, no representa una
magnitud fisica util para este ejemplo. El promedio se calcula solo entre
mediciones validas.
"""

from statistics import fmean
from typing import Callable, TypeAlias


Medicion: TypeAlias = dict[str, str | float | None]
Transformacion: TypeAlias = Callable[[list[Medicion]], list[Medicion]]


# Datos de entrada. La medicion del sensor B es invalida porque no contiene
# una temperatura.
MEDICIONES: list[Medicion] = [
    {"sensor": "A", "celsius": 22.5},
    {"sensor": "B", "celsius": None},
    {"sensor": "C", "celsius": 24.0},
    {"sensor": "D", "celsius": 23.5},
]


# 1. FUNCIONES PURAS
# Para una misma entrada siempre producen la misma salida y no modifican
# estado externo.
def celsius_a_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def celsius_a_kelvin(celsius: float) -> float:
    return celsius + 273.15


def es_valida(medicion: Medicion) -> bool:
    return medicion["celsius"] is not None


# 2. INMUTABILIDAD
# Se crea un nuevo diccionario. La medicion recibida no se modifica.
def agregar_fahrenheit(medicion: Medicion) -> Medicion:
    celsius = medicion["celsius"]
    if not isinstance(celsius, (int, float)):
        raise ValueError("La medicion debe contener una temperatura valida")

    return {
        **medicion, # ** significa "desempaquetar" el diccionario original. Permite crear un nuevo diccionario con los mismos pares clave-valor.
        "fahrenheit": celsius_a_fahrenheit(float(celsius)),
    }


# 3. FUNCIONES COMO VALORES Y FUNCIONES DE ORDEN SUPERIOR
def transformar_valor(
    valor: float,
    conversion: Callable[[float], float], ## callable es un tipo que representa una funcion. En este caso, la funcion recibe un float y devuelve un float.
) -> float:
    return conversion(valor)

# Un clausura en programacion funcional es una funcion que "recuerda" el contexto 
# en el que fue creada. En este caso, la funcion convertir recuerda los valores
# de factor y desplazamiento que se le pasaron a crear_conversor.
# Permite configurar una transformacion sin crear una clase.
def crear_conversor(
    factor: float,
    desplazamiento: float,
) -> Callable[[float], float]:
    def convertir(valor: float) -> float:
        return valor * factor + desplazamiento

    return convertir


# 4. FILTER Y MAP
def seleccionar_validas(mediciones: list[Medicion]) -> list[Medicion]:
    return list(filter(es_valida, mediciones))


def convertir_validas(mediciones: list[Medicion]) -> list[Medicion]:
    return list(map(agregar_fahrenheit, mediciones))


# 5. COMPOSICION
def componer(
    f: Transformacion,
    g: Transformacion,
) -> Transformacion:
    return lambda datos: f(g(datos))


procesar_mediciones = componer(convertir_validas, seleccionar_validas)


# 6. AGREGACION CON SIGNIFICADO PARA EL EJEMPLO
# Se obtiene el promedio aritmetico; no se presenta la suma de temperaturas.
def temperatura_promedio(mediciones: list[Medicion]) -> float | None:
    temperaturas = [
        float(medicion["celsius"])
        for medicion in mediciones
        if es_valida(medicion)
    ]

    return fmean(temperaturas) if temperaturas else None

# FUNCION PRINCIPAL
# esta parte del código muestra los resultados de las funciones anteriores, 
# incluyendo la verificación de que los datos originales no fueron modificados.

def mostrar_resultados() -> None:
    resultado = procesar_mediciones(MEDICIONES)
    promedio = temperatura_promedio(MEDICIONES)

    print("Datos originales:")
    for medicion in MEDICIONES:
        print(f"  {medicion}")

    print("\nMediciones validas transformadas:")
    for medicion in resultado:
        print(f"  {medicion}")

    print("\nFunciones como valores:")
    print(
        "  20 °C equivalen a "
        f"{transformar_valor(20, celsius_a_kelvin):.2f} K"
    )

    conversor_a_fahrenheit = crear_conversor(9 / 5, 32)
    print(
        "  Clausura configurada: 20 °C equivalen a "
        f"{conversor_a_fahrenheit(20):.2f} °F"
    )

    if promedio is None:
        print("\nNo hay mediciones validas para calcular el promedio.")
    else:
        print(f"\nTemperatura promedio: {promedio:.2f} °C")

    # Verificacion didactica: las funciones de transformacion no alteraron
    # los diccionarios originales agregandoles la clave 'fahrenheit'.
    originales_sin_modificar = all(
        "fahrenheit" not in medicion for medicion in MEDICIONES
    )
    print(f"Datos originales sin modificar: {originales_sin_modificar}")


if __name__ == "__main__":
    mostrar_resultados()
