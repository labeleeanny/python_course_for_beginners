# step 3
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [i[1:] for i in keywords]
print(new_keywords)


# step 4
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(i) for i in keywords]
print(lengths)


# step 5
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
r = []
lengths = [i for i in keywords if len(i) >= 5]
print(lengths)


# step 6
palindromes = [i for i in range(100, 1001) if str(i)[:] == str(i)[::-1]]
print(palindromes)


# step 7
numbers = [i ** 2 for i in range(1, int(input()) + 1)]
print(*numbers, sep='\n')


# step 8
num = [int(i) ** 3 for i in (input().split())]
print(*num, sep=' ')


# step 9
print(*input().split(), sep='\n')


# step 10
num = [i for i in input() if i.isdigit()]
print(*num, sep='')


# step 11
num = [int(i) ** 2 for i in input().split() if int(i) % 2 == 0 if int(i) **2 % 10 != 4]
print(*num, end=' ')
