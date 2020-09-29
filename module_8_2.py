def upper(s, n):
    '''Возвращает строку в верхнем регистре, если длина строки s больше n'''
    if len(s) > n:
        return s.upper()
    else:
        return s

if __name__ == "__main__":
    new_str = str(input('Введите строку: '))
    some_n = int(input('Введите число n: '))
    print(upper(new_str, some_n))
