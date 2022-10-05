# step 2
def is_valid_triangle(side1, side2, side3):
    return a + b > c and a + c > b and c + b > a


a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))


# step 3
def is_prime(num):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


n = int(input())

print(is_prime(n))


# step 4
def is_prime(num):
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


n = int(input())

print(get_next_prime(n))


# step 5
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


txt = input()

print(is_password_good(txt))


# step 6
def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])


txt = input()

print(is_password_good(txt))


# step 7
def is_palindrome(text):
    text = [i.lower() for i in text if i not in ',.!?- ']
    return text == text[::-1]


txt = input()

print(is_palindrome(txt))


# step 8
def is_valid_password(password):
    p = password.split(':')
    a1 = p[0]
    b1 = int(p[1])
    c1 = int(p[2])
    flag1 = False
    flag2 = False
    flag3 = False
    flag4 = False

    if len(p) == 3:
        flag1 = True

    if a1 == a1[::-1]:
        flag2 = True

    for i in range(2, b1):
        if b1 % i == 0:
            break
        else:
            flag3 = True

    if c1 % 2 == 0:
        flag4 = True

    return flag1 and flag2 and flag3 and flag4


psw = input()

print(is_valid_password(psw))


# step 9
def is_correct_bracket(text):
    while "()" in text:
        text = text.replace("()", "")
    return len(text) == 0


txt = input()

print(is_correct_bracket(txt))


# step 10
def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]


print(convert_to_python_case(input()))
