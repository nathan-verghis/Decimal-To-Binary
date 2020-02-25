import math
from typing import Dict


def greatest_two(num: int, pdict: Dict) -> int:
    '''return the greatest power of 2 less than the input

    >>> greatest_two(12)
    8
    >>> greatest_two(16)
    16'''
    counter = 0
    while pdict[counter] <= num:
        counter += 1
        if counter not in pdict:
            pdict[counter] = 2 ** counter
    counter -= 1
    return pdict[counter]


def recursive_power_finder(num: int, pdict: dict) -> list:
    '''returns a list containing all the powers of two, that when added, sum
    to the int

    >>> recursive_power_finder(10)
    [8, 2]
    >>> recursive_power_finder(31)
    [16, 8, 4, 2, 1]'''
    if num == 0:
        return [0]
    listy = [greatest_two(num, pdict)]
    diff = num - greatest_two(num, pdict)
    while diff != 0:
        listy.append(greatest_two(diff, pdict))
        diff = diff - greatest_two(diff, pdict)
    return listy


def exponent_to_power(lst: list) -> list:
    '''returns a list containing the exponents of the list passed in

    Precondition: the list passed in contains numbers that are all powers
    of two'''
    new_list = []
    for item in lst:
        a = int(math.log(item, 2))
        new_list.append(a)
    return new_list


def space_finder(lst: list) -> None:
    '''takes in a list from function exponent_to_power, and inserts a zero in
    between any spaces between consecutive items in the list. i.e, in list
    [5, 4, 3, 1], a space would be defined between 3 and 1, making the new list
    [5, 4, 3, 0, 1]'''
    start = lst[0]
    new_list = []
    for number in range(start + 1):
        new_list.append(number)
    new_list.reverse()
    for i in range(len(new_list)):
        if new_list[i] not in lst:
            lst.insert(i, 'space')


def negative_space_finder(lst: list) -> None:
    '''takes a list from function exponent_to_power, and inserts a zero in
    between any spaces between consecutive items in the list.  i.e, in list
    [5, 4, 3, 1], a space would be defined between 3 and 1, making the new list
    [5, 4, 3, 0, 1]. This applies only to lists of negative numbers such that
    lst[-1] is the smallest value in the list passed in.'''
    ending = lst[-1]
    new_list = []
    for number in range(ending, 0):
        new_list.append(number)
    new_list.reverse()
    for i in range(len(new_list)):
        if new_list[i] not in lst:
            lst.insert(i, 'space')


def final_binary_represention(lst: list) -> None:
    ''' takes a list from space_finder, a turns any value not 'space' into
    a 0, and every other value into a 1'''
    for item in range(len(lst)):
        if lst[item] == 'space':
            lst[item] = 0
        else:
            lst[item] = 1


def is_zero(num: float) -> bool:
    '''returns whether or not the input is zero'''
    return num / 1 == 0


def largest_fraction(num: float, limit: int) -> list:
    '''takes in a number such that 0 < number < 1, and outputs a list containing
    the sequence of negative powers of two (e.g. 2^ -1, 2^ -2) such that their
    sum is the number, rounding error as according to the limit on the number
    of places after the floating point'''
    counter = -1
    power_list = []
    while sum(power_list) < num:
        if abs(counter) > limit:
            break
        if 2 ** counter + sum(power_list) > num:
            counter -= 1
        elif 2 ** counter + sum(power_list) <= num:
            power_list.append(2 ** counter)
            counter -= 1
    return power_list


print("Please input a number: ")
decimal = input()
if is_zero(float(decimal)):
    print(0)
elif float(decimal) < 0:
    decimal = str(float(decimal) * -1)
    remainder = 0
    power_dict = {0: 1}
    if '.' in decimal and float(decimal) != int(float(decimal)):
        print("You are using a floating-point number, so I will need the number"
              " of places after the point to round after so I don't run forever"
              ":) (I would put 100 to be safe): ")
        limit = int(input())
        period = decimal.index('.')
        remainder = decimal[period + 1:]
        last = '0.' + remainder
        summation = largest_fraction(float(last), limit)
        summation = exponent_to_power(summation)
        negative_space_finder(summation)
        final_binary_represention(summation)
        end = ''
        for thing in summation:
            end += str(thing)
        first = decimal[:period]
        if first == '0':
            new_final = '0'
        else:
            final = recursive_power_finder(int(float(first)), power_dict)
            final = exponent_to_power(final)
            space_finder(final)
            final_binary_represention(final)
            new_final = ''
            for thing in final:
                new_final += str(thing)
        answer = new_final + '.' + end
        answer = '-0b ' + answer
        print(answer)
    else:
        period = -1
        decimal = str(int(float(decimal)))
        final = recursive_power_finder(int(float(decimal)), power_dict)
        final = exponent_to_power(final)
        space_finder(final)
        final_binary_represention(final)
        new_final = ''
        for thing in final:
            new_final += str(thing)
        new_final = '-0b ' + new_final
        print(new_final)
else:
    remainder = 0
    power_dict = {0: 1}
    assert float(decimal) >= 0
    # assert decimal.isnumeric()
    if '.' in decimal and float(decimal) != int(float(decimal)):
        print("You are using a floating-point number, so I will need the number"
              " of places after the point to round after so I don't run forever"
              ":) (I would put 100 to be safe): ")
        limit = int(input())
        period = decimal.index('.')
        remainder = decimal[period + 1:]
        last = '0.' + remainder
        summation = largest_fraction(float(last), limit)
        summation = exponent_to_power(summation)
        negative_space_finder(summation)
        final_binary_represention(summation)
        end = ''
        for thing in summation:
            end += str(thing)
        first = decimal[:period]
        if first == '0':
            new_final = '0'
        else:
            final = recursive_power_finder(int(float(first)), power_dict)
            final = exponent_to_power(final)
            space_finder(final)
            final_binary_represention(final)
            new_final = ''
            for thing in final:
                new_final += str(thing)
        answer = new_final + '.' + end
        answer = '0b ' + answer
        print(answer)
    else:
        period = -1
        decimal = str(int(float(decimal)))
        final = recursive_power_finder(int(float(decimal)), power_dict)
        final = exponent_to_power(final)
        space_finder(final)
        final_binary_represention(final)
        new_final = ''
        for thing in final:
            new_final += str(thing)
        new_final = '0b ' + new_final
        print(new_final)
