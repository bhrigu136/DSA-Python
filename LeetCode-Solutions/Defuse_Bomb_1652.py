def bruteforce(code, k):
    n = len(code)
    res = [0] * n

    if k == 0:
        return res
    
    for i in range(n):
        total = 0
        if k > 0:
            for j in range(1, k + 1):
                total += code[(i + j) % n]
        else:
            for j in range(1, -k + 1):
                total += code[(i - j + n) % n]
        res[i] = total
    return res

def sliding_window_approach(code, k):
    n = len(code)
    res = [0] * n

    if k == 0:
        return res
    
    window_sum = 0

    if k > 0:
        for i in range(1, k + 1):
            window_sum += code[i % n]

        for i in range(n):
            res[i] = window_sum
            window_sum -= code[(i + 1) % n]
            window_sum += code[(i + k + 1) % n]

    else:
        k = -k
        for i in range(n - k, n):
            window_sum += code[i]

        for i in range(n):
            res[i] = window_sum

            window_sum -= code[(i - k) % n]
            window_sum += code[i % n]
    return res

if __name__ == "__main__":
    n = int(input("Enter the size of the code array: "))

    print("Enter the code array elements: ")
    code = list(map(int, input().split()))
    k = int(input("Enter the value of k: "))
    print("\nBruteforce Approach: ")
    ans_bf = bruteforce(code, k)
    print("Decrypted code array is: ", ans_bf)
    print("\nSliding Window Approach: ")
    ans_sw = sliding_window_approach(code, k)
    print("Decrypted code array is: ", ans_sw)

    """
    Time Complexity:
    Bruteforce Approach: O(n^2)
    Sliding Window Approach: O(n)   
    Space Complexity: O(1)
    """