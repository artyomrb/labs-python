s = "У лукоморья 123 дуб зеленый 456"
print('1. ', s.find('я'))
print('2. ', s.count('у'))
if s.isalpha() == False:
    print('3. ', s.upper())
print('4. Длина строки: ', len(s))
if len(s) > 4:
    print(' ', s.lower())
print('5. ', s.replace(s[0], 'О', 1))
