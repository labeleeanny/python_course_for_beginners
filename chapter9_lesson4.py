# step 8
s = input()
print(s.count(' ') + 1)


# step 9
n = input()
n = n.lower()
print('Аденин:', n.count('а'))
print('Гуанин:', n.count('г'))
print('Цитозин:', n.count('ц'))
print('Тимин:', n.count('т'))


# step 10
n = int(input())
count = 0
for i in range(n):
    s = input()
    if s.count('11') >= 3:
        count += 1
print(count)


# step 11
n = input()
k = 0
for i in n:
    if i in '0123456789':
        k += 1
print(k)


# step 12
n = input()
if n.endswith('.com') or n.endswith('.ru'):
    print('YES')
else:
    print('NO')


# step 13
s = input()
c = 0
a = 0
for i in s:
    if s.count(i) >= c:
        c = s.count(i)
        a = i
print(a)


# step 14
n = input()
if n.count('f') == 1:
    print(n.find('f'))
elif n.count('f') >= 2:
    print(n.find('f'), n.rfind('f'))
else:
    print('NO')


# step 15
st = input()
first = st.find('h')
last = st.rfind('h')
st = st[:first] + st[(last + 1):]
print(st)
