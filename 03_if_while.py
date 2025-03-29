print('Czesc, wyliczmy miesieczny koszt ogrzania Twojego mieszkania.')

size_house = int(input('Jaki jest metraz Twojego mieszkania?  '))
days = int(input('Za ile dni chcesz policzyc koszt ogrzewania?  '))
type_house = input('Jaki jest typ Towjego mieszkania? (cegla/plyta)?  ')

while type_house != 'cegla' and type_house != 'plyta':
    print('Bledne dane')
    type_house = input('Jaki jest typ Towjego mieszkania? (cegla/plyta)?  ')
if type_house == 'cegla':
    print(size_house*0.3*days)
elif type_house == 'plyta':
    print(size_house*0.5*days)