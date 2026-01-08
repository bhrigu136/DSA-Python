"""
    Determine if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Args:
    s (str): The first string.
    t (str): The second string.

    Returns:
    bool: True if t is an anagram of s, False otherwise.
"""

def valid_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False
    
    freq = [0] * 26

    for c in s:
        freq[ord(c) - ord('a')] += 1

    for c in t:
        freq[ord(c) - ord('a')] -= 1

    for count in freq:
        if count != 0:
            return False
        
    return True

s = str(input("Enter the first string:"))
t = str(input("Enter the second string:"))

result = valid_anagram(s, t)
print("Are the two strings anagrams?", result)  


'''
Approach (Explainable to interviewer)

If lengths differ → return false

Create frequency array of size 26

Increment count for characters in s

Decrement count for characters in t

If any count ≠ 0 → not an anagram
'''