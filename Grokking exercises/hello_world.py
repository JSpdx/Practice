
demo_list = [1,34,45,56,67,89]

def binary_sort(demo_list, item):
    low = 0
    high = len(demo_list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = demo_list[mid]
        print(guess)
        if item == guess:
            print(mid)
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None

binary_sort(demo_list, 89)