def set(mask, i): # set bit at position i to 1
    return mask | (1 << i)

def clear(mask, i): # clear bit at position i to 1
    return mask & (~(1 << i))

def toggle(mask, i): # 
    return mask ^ (1 << i)

def get(mask, i):
    return (mask >> i) & 1

def count(mask): # count number of bit = 1
    return mask.bit_count()

def length(mask):
    return mask.bit_length()

def isOdd(num):
    return (num & 1) == 1

def power2(n):
    return 1 << n

def isPower2(n):
    return n & (n - 1) == 0