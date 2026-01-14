def brute_force(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (i + 1, j + 1)
    return []

def two_pointer_approach(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return (left + 1, right + 1)
        elif total < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))

    print("Enter a sorted array")
    nums = list(map(int, input().split()))

    target = int(input("Enter the target sum: "))

    print("\nBruteforce Approach:")
    ans_bf = brute_force(nums, target)
    print("Indices of the two numbers are:", ans_bf)

    print("\ntwo_pointer_approach:")
    ans_tp = two_pointer_approach(nums, target)
    print("Indices of the two numbers are:", ans_tp)

"""
Notes:
Time Complexity:
- Brute Force: O(n²)
- Two Pointer: O(n) 
"""