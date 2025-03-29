#Dana jest lista nazw użytkowników
#Napisz program, który zapyta o:
# nazwę użytkownika
# poinformuje, czy nazwa użytkownika jest wolna, a jeśli nie
# poinformuje, na którym miejscu w liście jest zapisany dany użytkownik.

uzytkownicy = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']

user_name = input('Podaj nazwe uzytkownika:  ')
licznik = 1

while user_name in uzytkownicy:
        licznik = uzytkownicy.index(user_name) + 1 #uzytkownicy to nazwa listy, index(user_name) to metode, któa znajduje pierwsze wystąpienie elementu user name w liście użytkowników, indeksy w pythonie są od 0 stąd +1
        print(f'login zajety, jest na miejscu {licznik}')
        user_name = input('Podaj nazwe uzytkownika:  ')

else:
    print(f'zapraszamy login wolny!')


