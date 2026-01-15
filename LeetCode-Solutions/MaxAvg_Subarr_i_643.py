def find_max_avg(nums, k):
    n = len(nums)
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, n):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))

    print("Enter the array elements: ")
    nums = list(map(int, input().split()))
    k = int(input("Enter the size of the subarray (k): "))
    result = find_max_avg(nums, k)
    print(f"The maximum average of subarrays of size {k} is: {result}")

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """