products = dict()
products["яблоки"] = 24
products["молоко"] = 41
products["апельсины"] = 25
products["авокадо"] = 56
products ["сок"] = 102

n = 0
while n != 1:
    choose = input('Введите название товара, чтобы узнать его цену или \'выход\' для завершения программы: ')
    if choose != 'выход':
        print('Цена товара ',choose,': ',products.get(choose))
    else:
        print('Работа программы завершена')
        n = 1
