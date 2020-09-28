 
    

sortedList = [1,4,6,12,23,34,45,56,67,888,999]

def binary_sort(sortedList, item):
    print('test')
    low = 0
    high = len(sortedList) - 1
    
    while low <= high:
        mid = int((low + high)  / 2)
        guess = sortedList[mid]
        print(guess)
        if guess == item:
            return(mid)
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

binary_sort(sortedList, 888)