# Dana jest lista liczb całkowitych
# Napisz program, który wyświetli po kolei wszystkie liczby razem z ich miejscem w liście

lista = [1, 5, 3, 24, 15]
licznik = 1
for l in lista:
    print(licznik, l)
    licznik = licznik + 1
print('\nkoniec pierwszego programu')

# Napisz program, który wyświetli tylko liczby parzyste LUB liczby większe od 10

lista = [1, 5, 3, 24, 15, 23, 22, 10]
for l in lista:
    if l % 2 == 0:
        print(l)
print('\nkoniec drugiego programu')