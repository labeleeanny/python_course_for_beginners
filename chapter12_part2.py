# task 1
n = int(input())
s = []
for i in range(2, n + 1, 2):
    s.append(i)
print(s)


# task 2
l, m = input().split(), input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))


# task 3
l, m = input().split(), input().split()
print(*(int(l[i]) + int(m[i]) for i in range(len(l))))


# task 4
s = input().split("-")
flag = False
for j in s:
    if not j.isdigit():
        flag = False
        break
    if 3 <= len(s) <= 4:
        if int(s[0]) == 7 or len(s[0]) == 3:
            if len(s[1]) == 3 and len(s[-1]) == 4:
                flag = True
print("YES" if flag else "NO")


# task 5
n = [len(i) for i in input().split()]
print(max(n))


# task 6
print(*[a[1:] + a[0] + 'ки' for a in input().split()])
