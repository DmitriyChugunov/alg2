def monoton(arr):                                         # def Функция с функией arr которая возвращает показатели max и min
    n = len(arr)                                          # "n" переменная / len считает индексы в строке
    start = 0                                             # Просто переменная
    max_length = 1                                        # Просто переменная
    current_length = 2                                    # Просто переменная
    is_increasing = None                                  # Переменная со значением ничего

    for i in range(1, n):                                 # Цикл For i с оператором in для проверки возврата
        if arr[i] > arr[i - 1]:
            if is_increasing is None:
                is_increasing = True
            elif not is_increasing:
                current_length = 2
                is_increasing = True
            else:
                current_length += 1
        elif arr[i] < arr[i - 1]:
            if is_increasing is None:
                is_increasing = False
            elif is_increasing:
                current_length = 2
                is_increasing = False
            else:
                current_length += 1
        else:
            current_length = 1
            is_increasing = None

        if current_length > max_length:
            max_length = current_length
            start = i - max_length + 1

    return arr[start: start + max_length]
arr = [100, 2, 3, 4, 100, 5, 6, 100]
monotonic_subarray = monoton(arr)
a = monotonic_subarray[0]
b = monotonic_subarray[-1]
print(monotonic_subarray)
print(a)
print(b)