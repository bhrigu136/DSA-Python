def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    print("Enter the array elements: ")
    nums = list(map(int, input().split()))
    val = int(input("Enter the value to be removed: "))
    result = removeElement(nums, val)
    print("Array after removing the element:", nums[:result])
    print("New length of the array:", result)
"""
Time Complexity: O(n)
Space Complexity: O(1) 
"""
