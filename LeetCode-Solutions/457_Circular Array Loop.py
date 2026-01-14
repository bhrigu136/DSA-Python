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

t = int(input("Enter number of test cases: ").strip())
for _ in range(t):
  arr = list(map(int, input("Enter array elements: ").strip().split()))

  print(circular_array_loop(arr))

""" Output:
Enter number of test cases: 3
Enter array elements: 2 -1 1 2 2  
True
Enter array elements: -1 -2 -3 -4 -5 6
False
Enter array elements: 1 -1 5 1 4
True
"""