# Ejemplo 3: un iterador recuerda en que posicion quedo.

lista = [1, 2, 3]

iterador_1 = iter(lista)
for x in iterador_1:
    print(x**2, end=" ")

print()
iterador_2 = iter(lista)
x = next(iterador_2)  # Tambien podria llamarse: iterador_2.__next__()
print(x**2, end=" ")
x = next(iterador_2)
print(x**2, end=" ")
x = next(iterador_2)
print(x**2, end=" ")

print()
print(iterador_1)
print(iterador_2)

# Si se vuelve a llamar next(iterador_2), se lanza StopIteration.
try:
    next(iterador_2)
except StopIteration:
    print("El iterador ya no tiene mas elementos.")
