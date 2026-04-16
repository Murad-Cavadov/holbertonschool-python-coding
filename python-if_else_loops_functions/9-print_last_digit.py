#!/usr/bin/python3
def print_last_digit(number):
    # Ədədin mütləq qiymətinin 10-a bölünməsindən qalan qalığı tapırıq
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
