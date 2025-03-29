#Program spyta o zarobki brutto
#Spyta o liczbę dzieci
#Obliczy, ile użytkownik dostanie pieniędzy netto.
#Podatek wynosi 10%, gdy zarabiamy powyżej 3000 zł
# 20%, gdy zarabiamy powyżej 5000 zł.
# na każde dziecko jest 800 zł

brutto = int(input('Jakie sa zarobki w Twojej rodzinie? '))
dzieci = int(input('ile masz dzieci? '))
rodzina = dzieci + 2

if  brutto > 5000:
    netto = brutto * 0.8
elif brutto >= 3000:
    netto = brutto * 0.9
else:
    netto = brutto
dochod_os = (netto + 800 * dzieci)/rodzina
print(dochod_os)