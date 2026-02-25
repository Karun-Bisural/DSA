'''

def binary_search_recursive(array, key, first, last):
    mid = (first + last) // 2
    if array[mid] == key:
        return f"Item found at index {mid}"
    elif key < array[mid]:
        return binary_search_recursive(array, key, first, mid - 1)
    else:
        return binary_search_recursive(array, key, mid + 1, last)

a = [10, 11, 12, 13, 14]
first=0
last=len(a)-1
print(binary_search_recursive(a, 11, first, last))

'''

#