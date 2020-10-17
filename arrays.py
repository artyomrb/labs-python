import random
arr=list(range(1,100))

print("-----1 вопрос-----")
#1.Как найти пропущенное число в заданном массиве целых чисел от 1 до 100?
print('1. Пропущенное число: ', 5050 - sum(arr))
#2.Как найти повторяющееся число в заданном массиве целых чисел?
print("-----2 вопрос-----")
for i in arr:
        if arr.count(i) >= 2:
            print(arr[i])
            quit()
print("Нет повторяющихся элементов")
print("-----3 вопрос-----")
#3.Как найти наибольшее и наименьшее число в неотсортированном массиве?
nmax = 1
nmin = 1
for i in range(len(arr)):
    if arr[i] < nmin:
        nmin = arr[i]
    if arr[i] > nmax:
        nmax = arr[i]
print('3. Максимальный элемент:',nmax,'\n3. Минимальный элемент:', nmin)
print("-----4 задание-----")

#4.Как найти все пары в массиве целых чисел, сумма которых равна заданному числу?
nsum = int(input('Введите искомую сумму: '))
arr.sort()
first = 1;
last = len(arr) - 1
while first < last:
    s = arr[first] + arr[last]
    if s == nsum:
        print(arr[first], arr[last])
        first += 1
        last -= 1
    else:
        if s < nsum:
            first += 1
        else:
            last -= 1
if nsum != s:
    print('Числа не найдены')

print("-----5 задание-----")
#5.Как найти повторяющиеся числа в массиве, если их несколько?
arr2 = [random.randint(1, 25) for i in range(50)]
print('Исходный массив: ', arr2)
arr2.sort()
d_arr2 = []
print("повторяющиеся числа: ")
for i in range(len(arr2) - 1):
    if (arr2[i] == arr2[i+1]) and (arr2[i] not in d_arr2):
        d_arr2.append(arr2[i])
        print(arr2[i])
print("-----6 задание-----")
#6.Как удалить повторяющиеся элементы из заданного массива?
arr3 = [random.randint(1, 25) for i in range(50)]
print('Исходный массив: ', arr3)
d_arr3 = []
for i in arr3:
    if i not in d_arr3:
        d_arr3.append(i)
print('Массив без повторяющихся элементов: ', d_arr3)
print("-----7 задание-----")
#7.Как сортировать массив целых чисел без дополнительной памяти при помощи алгоритма быстрой сортировки?
def eassrt(arr, first, last):
    if first >= last:
        return
    mid = arr[(first + last)//2]
    f, l = first, last
    while f <= l:
        while arr[f] < mid:
            f = f + 1
        while arr[l] > mid:
            l = l - 1
        if f <= l:
            arr[f], arr[l] = arr[l], arr[f]
            f, l = f +1, l -1        
    eassrt(arr, first, l)
    eassrt(arr, f, last)
eassrt(arr3, 0, len(arr3)-1)
print('Быстрая сортировка: ', arr3)
print("-----8 задание-----")
#8.Как удалить повторяющиеся элементы из массива без дополнительной памяти?
print('8. Массив без повторяющихся элементов: ', list(set(arr3)))
print("-----9 задание-----")
#9.Как сделать поменять порядок элементов в массиве на обратный без дополнительной памяти?
print('9. Массив в обратном порядке: ', list(reversed(arr3)))
print("-----10 задание-----")
#10.Как удалить повторяющиеся элементы из массива без использования коллекций?
for i in range(len(arr3)-1,-1,-1):       #(работает только в отсортированном массиве)
        if arr3[i] == arr3[i-1]: del arr3[i]
print('10. Массив без повторяющихся элементов: ', arr3)
