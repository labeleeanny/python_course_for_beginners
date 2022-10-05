# step 6
def convert_to_miles(km):
    km = num * 0.6214
    return km


num = int(input())

print(convert_to_miles(num))


# step 7
def get_days(month):
    list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return list1[month - 1]


num = int(input())

print(get_days(num))


# step 8
def get_factors(num):
    return [i for i in range(1, n + 1) if n % i == 0]


n = int(input())

print(get_factors(n))


# step 9
def get_factors(num1):
    return [i for i in range(1, num1 + 1) if num1 % i == 0]


def number_of_factors(num1):
    return len(get_factors(num1))


n = int(input())

print(number_of_factors(n))


# step 10
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i] == symbol]


s = input()
char = input()

print(find_all(s, char))


# step 11
def merge(list1, list2):
    return sorted(list1 + list2)


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))


# step 13
def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result


def merge_lists(n1):
    list1 = []

    for i in range(1, n1 + 1):
        list2 = [int(x) for x in input().split()]
        list1 = quick_merge(list1, list2)

    return list1


n = int(input())

print(*merge_lists(n))
