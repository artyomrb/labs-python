import random
import operator
print("-----быстрая сортировка-----")
#1.Быстрая сортировка
def qcksort(arr, first, last):
    """Метод быстрой сортировки одномерного массива"""
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
    qcksort(arr, first, l)
    qcksort(arr, f, last)

arr1 = [random.randint(1, 10) for i in range(15)]
print('Исходный массив: ', arr1)
qcksort(arr1, 0, len(arr1)-1)
print('Быстрая сортировка: ', arr1)
#2.Сортировка слиянием
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r)
ы
#3.Сортировка Шелла
print("-----сортировка Шелла-----")
def shellsort(arr):
    """Метод сортировки Шелла для одномерного массива"""
    dist = len(arr) // 2
    while dist > 0:
        for i in range(len(arr)-dist):
            j = i
            while j >= 0 and arr[j] > arr[j+dist]:
                arr[j], arr[j+dist] = arr[j+dist], arr[j]
                j -= 1
        dist = int(dist/2)
    return arr
randarr = [random.randint(1, 10) for i in range(15)]
print('Исходный массив: ', randarr)
print('Сортировка Шелла: ', shellsort(randarr))

#4.Сортировка выбором
print("-----сортировка выбором-----")
def selectionsort(arr):
    """Метод сортировки одномерного массива выбором"""
    for i in range(len(arr) - 1):
        arrmin = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[arrmin]:
                arrmin = j
            j += 1
        arr[i], arr[arrmin] = arr[arrmin], arr[i]
    return arr
thisarr = [random.randint(1, 10) for i in range(15)]
print('Исходный массив: ', thisarr)
print('Сортировка выбором: ', selectionsort(thisarr))

#5.Сортировка пузырьком
print("-----сортировка пузырьком-----")
arr2 = [random.randint(1, 10) for i in range(15)]
print('Исходный массив: ', arr2)
def bubblesort(arr):
    """Метод сортировки одномерного массива пузырьком"""
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print('Сортировка пузырком: ', bubblesort(arr2))

#6.Сортировка вставками
print("-----сортировка вставками-----")
def insertsort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        j = i-1
        while j >=0 and curr < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
            arr[j+1] = curr 
    return arr
anyarr = [random.randint(1, 10) for i in range(15)]
print('Исходный массив: ', anyarr)
print('Сортировка вставками: ', insertsort(anyarr))
