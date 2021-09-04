year = input('Введите год\n')

if year.isdigit():
    if int(year[-2:]) % 4 == 0:
        print('Год високосный')
    else:
        print('Год не високосный')
else:
    print('Введите год ЦИФРАМИ')