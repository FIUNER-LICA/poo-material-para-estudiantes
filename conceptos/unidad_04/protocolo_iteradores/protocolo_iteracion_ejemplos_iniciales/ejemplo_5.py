from pathlib import Path


# Ejemplo 5: algunas estructuras devuelven otro iterador; los archivos se devuelven a si mismos.

lista = [1, 2, 3, 4]
archivo_path = Path(__file__).with_name("comidas.txt")

with open(archivo_path, encoding="utf-8") as archivo:
    iterador_1 = iter(lista)
    iterador_2 = iter(archivo)

    print(iterador_1 is lista)
    print(iterador_2 is archivo)

    print()
    print(id(lista))
    print(id(iterador_1))
    print(id(archivo))
    print(id(iterador_2))
