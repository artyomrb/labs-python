def func(left, right):  
    sorted = []
    left_i = right_i = 0

    left_length, right_length = len(left), len(right)

    for _ in range(left_length + right_length):
        if left_i < left_length and right_i < right_length:
            if left[left_i] <= right[right_i]:
                sorted.append(left[left_i])
                left_i += 1
            else:
                sorted.append(right[right_i])
                right_i += 1
        elif left_i == left_length:
            sorted.append(right[right_i])
            right_i += 1
        elif right_i == right_length:
            sorted.append(left[left_i])
            left_i += 1

    return sorted

def f_sort(num):
    if len(num) <= 1:
        return num

    m = len(num) // 2

    left = f_sort(num[:m])
    right = f_sort(num[m:])
    return func(left, right)

random_ = [12, 8, 6, 1000, 10]  
random_ = f_sort(random_)  
print(random_)
