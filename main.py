# funkcja z słowkiem yield to generator
def gen():
    i = 0
    while i < 5:
        yield i #yield bardzo podobne do return. Zwraca wartość, ale nie przerywa działania funkcji
        i += 1

print(list(gen()))

#tylko działa dla funkcji-generatorów
for i in gen():
    print(i)

def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1

for i in parzyste(9):
    print(i)