def sum_two_numbers(a, b):
    result = a + b
    return result

print(sum_two_numbers(10, 20))

def copy_array(arr):
    new_arr = []
    for num in arr:
        new_arr.append(num)
    return new_arr

print(copy_array([1, 2, 3, 4]))

def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_in_place([1, 2, 3, 4]))