def return_unique(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    i = 1
    j = 0
    while i < n:
        if arr[i] == arr[j]:
            i += 1
        else:
            j += 1
            arr[j] = arr[i]
            i += 1

    return j + 1

if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print("\nTwo Pointer Approach:")
    print("Original array:", arr)

    new_length = return_unique(arr)
    print("Number of unique elements:", new_length)
    print("Array after removing duplicates:", arr[:new_length])
