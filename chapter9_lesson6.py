# step 4
n, a = int(input()), int(input())
for i in range(n, a + 1):
    print(chr(i), end=' ')


# step 5
n = input()
for c in n:
    print(ord(c), end=' ')


# step 6
n, s = int(input()), input()
for c in s:
    if ord(c) - n < 97:
        print(chr(122 - (96 - ord(c) + n)), end='')
    else:
        print(chr(ord(c) - n), end='')
