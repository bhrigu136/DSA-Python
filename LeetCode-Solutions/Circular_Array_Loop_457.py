def circular_array_loop(arr):
  n = len(arr)

  def next_index(i):
    return (i + arr[i]) % n

  for start in range(n):
    forward = arr[start] > 0
    slow = start
    fast = start

    while True:
      next_slow = next_index(slow)
      if (arr[next_slow] > 0) != forward:
        break

      next_fast = next_index(fast)
      if (arr[next_fast] > 0) != forward:
        break

      next_fast2 = next_index(next_fast)
      if (arr[next_fast2] > 0) != forward:
        break

      slow = next_slow
      fast = next_fast2

      if slow == fast:
        if slow == next_index(slow):
          break
        return True

  return False

if __name__ == "__main__":
  n = int(input("Enter the size of the array: "))

  print("Enter the elements of the array: ")
  nums = list(map(int, input().split()))
  
  if circular_array_loop(nums):
    print("Circular loop exists: True")
  else:
    print("Circular loop exists: False")

"""
Output:
Enter the size of the array: 5
Enter the elements of the array: 
2 -1 1 2 2
Circular loop exists: True
"""
