def partition(num, low, high):  
    pivot = num[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while num[i] < pivot:
            i += 1

        j -= 1
        while num[j] > pivot:
            j -= 1

        if i >= j:
            return j

        num[i], num[j] = num[j], num[i]

def quick_sort(num): 
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(num, 0, len(num) - 1)

list = [2, 8, 6, 10, 88, 3]  
quick_sort(list)  
print(list) 
