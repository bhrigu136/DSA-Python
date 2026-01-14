from collections import Counter

def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    target_freq = Counter(t)
    window_freq = {}

    l