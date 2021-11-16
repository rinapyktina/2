# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))

    if month < 1 or month > 12:
        print("Недопустимое значение month")
    else:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
                print(29)
            else:
                print(28)
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            print(31)
        else:
            print(30)