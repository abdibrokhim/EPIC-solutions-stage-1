# Task 4
# We call a number beautiful if it ends with the number 6,
# and after moving this number to the beginning, it increases exactly 3 times.
# Determine what is the minimum beautiful number.

def min_bea_num():
    num_list = []
    num_list_1 = []
    num_list_2 = []

    i = 100
    while i < 1000:
        r = i % 10
        if r == 6:
            num_list.append(i)
        i += 1
    # print(num_list)

    for i in range(0, len(num_list)):
        n = str(num_list[i])
        last = n[-1]
        first = n[:-1]

        new_num = str(last) + str(first)
        num_list_1.append(int(new_num))
    print('\n')
    # print(num_list_1)

    for i in zip(num_list, num_list_1):
        if i[1] / i[0] == 3:
            num_list_2.append(i[1])
    print('\n\n', num_list_2)


# Task 6
# The child was asked to write down some integer X on a piece of paper.
# After that, he himself wrote down next to a number one more and a number one less than X.
# After that, the child multiplied all the numbers, took the result modulo 6 and got 0. Why?

def got_0():
    num_list = {}
    i = 2
    while i < 100:
        num1 = i - 1
        num2 = i + 1
        res = i * num1 * num2
        if res % 6 == 0:
            num_list.update({f'main{i-1}': i,
                             f'new{i-1}': res})
        i += 1

    c = 0
    for i in num_list:
        print(i, num_list[i], end=' | ')
        c += 1
        if c == 2:
            print('\n')
            c = 0
    print(num_list)


# Task 7
# How many different words can be obtained by rearranging the letters in the word 'INSTITUTE'?

def diff_words():
    occ_list = {}
    word = "INSTITUTE"
    for i in word:
        occ_list.update({i: word.count(i)})
    print(occ_list)
    up = permutation(len(word))
    print(up)
    down = 1
    for i in occ_list:
        down *= permutation(occ_list[i])
    print(down)
    res = up / down
    print(res)


def permutation(word):
    if word == 1:
        return 1
    else:
        return word * permutation(word - 1)


# Task 17
# Given a string S of lowercase Latin letters.
# Determine if it is possible to rearrange the letters
# in such a way that the string becomes a palindrome?
# How many different palindrome strings can you get?
# Two strings are different if there is at least one position in i where the characters of the strings differ.

# A string is a palindrome if it reads from the beginning and from the end the same way.

# Sample solution

def is_palindrome():
    occ_list = {}
    word = "rotator"
    for i in word:
        occ_list.update({i: word.count(i)})
    print(occ_list)
    c = 0
    r = int(len(word) / 2)
    print(r)
    for i in occ_list:
        if occ_list[i] == 2:
            c += 1
    if r == c:
        print('can make palindrome')
    else:
        print('cannot make palindrome')


# Accurate soluiton

def can_form_palindrome():
    NO_OF_CHARS = 254
    st = "deed"
    count = [0] * NO_OF_CHARS
    print(count)

    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
        print('letter:', st[i])
        print('char:', ord(st[i]))
        print(count[ord(st[i])], count[ord(st[i])] + 1)
    odd = 0

    for i in range(0, NO_OF_CHARS):
        print(f'count{i}:', count[i])
        if count[i] & 1:
            odd = odd + 1
            print(f'count{i}:', count[i])
            print('odd:', odd)

        if odd > 1:
            return False
            # print('false')
    print(len(count))
    return True
    # print('true')


def can_cannot_make():
    if can_form_palindrome():
        print('can make palindrome')
    else:
        print('cannot make palindrome')


# Task 10
# Suggest a way to count the number of natural numbers
# that do not exceed a given number N and are not divisible by any of the numbers 2, 3, 5, 7.

def not_divisible(n):
    for i in range(1, n+1):
        print('i:', i)
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            n -= 1
        print(n)
    print(n)


def main():
    # min_bea_num()
    # got_0()
    # diff_words()
    # is_palindrome()
    # can_cannot_make()
    not_divisible(20)


if __name__ == '__main__':
    main()
