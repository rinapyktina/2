# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    g = int(input())
    m = int(input())
    n = int(input())
    date = 0
    end = 0
    next_day = 0
    prev_day = 0
    g1 = g
    if (g % 4 == 0 and g % 100 != 0) or (g % 100 == 0 and g % 400 == 0):
        february = 29
    else:
        february = 28
    if m == 2:
        end = february
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        end = 31
    else:
        end = 30
    if n > end or n < 1:
        print("Недопустимое значение n")
    else:
        if n == 1:
            next_day = 2
            m1 = m - 1
            if m1 in [1, 3, 5, 7, 8, 10, 12]:
                prev_day = 31
            elif m1 == 2:
                prev_day = february
            else:
                prev_day = 30
            if m1 == 0:
                m1 = 12
                g1 -= 1
                prev_day += 1
            print(f"Previous day is {prev_day}.{m1}.{g1}")
            print(f"Next day is {next_day}.{m}.{g}")
        elif n == end:
            m1 = m + 1
            prev_day = n - 1
            next_day = 1
            if m1 == 13:
                m1 = 1
                g1 += 1
            print(f"Previous day is {prev_day}.{m}.{g}")
            print(f"Next day is {next_day}.{m1}.{g1}")
        else:
            print(f"Previous day is {n - 1}.{m}.{g}")
            print(f"Next day is {n + 1}.{m}.{g}")