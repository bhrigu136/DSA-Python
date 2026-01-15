def bruteforce(nums):
    return sorted([x * x for x in nums])

def two_pointer_approach(nums):
    n = len(nums)
    result = [0] * n 
    left, right = 0, n - 1
    position = n-1

    while left <= right:
        left_square = nums[left] * nums[left]
        right_square = nums[right] * nums[right]

        if left_square > right_square:
            result[position] = left_square
            left += 1
        else:
            result[position] = right_square
            right -= 1
        position -= 1

    return result

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))

    print("Enter a sorted array")
    nums = list(map(int, input().split()))
    print("\nBruteforce Approach: ")
    ans_bf = bruteforce(nums)
    print("Sorted squares of the array are:", ans_bf)
    print("\ntwo_pointer_approach: ")
    ans_tp = two_pointer_approach(nums)
    print("Sorted squares of the array are: ", ans_tp)

    """
    Time Complexity:
    Bruteforce Approach: O(n log n)
    Two Pointer Approach: O(n)
    """
  