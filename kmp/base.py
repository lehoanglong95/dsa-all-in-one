def kmp(pattern, text):
    new_text = f"{pattern}#{text}"
    m = len(pattern)
    n = len(new_text)
    kmp = [0] * n

    for i in range(1, n):
        j = kmp[i-1]
        while j and new_text[i] != new_text[j]:
            j = kmp[j-1]
        if new_text[i] == new_text[j]:
            j += 1
        kmp[i] = j
        if j == len(pattern):
            return i - (2 * m)

    return -1

if __name__ == "__main__":
    print(kmp("hello", "helloworld"))
    print(kmp("hello1", "helloworld"))