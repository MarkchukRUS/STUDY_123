text_polindrom = input('введите любое слово: ')
Slovar = {}

for i in text_polindrom:
    if i in Slovar.keys():
        Slovar[i] +=1
    else:
        Slovar[i] = 1

quantity_of_values = 0
for i in Slovar.values():
    if i%2 == 1:
        quantity_of_values+=1

if quantity_of_values >= 2:
    print('ПАЛЕНДРАМ НЕ ПАЛЛУЧЕЦА!')
else:
    print("палендром получается!")