if __name__ == "__main__":
    n = int(input())
    if 0 <= n <= 11:
        month = n + 1
        if month == 1:
            print("январь")
        elif month == 2:
            print("февраль")
        elif month == 3:
            print("март")
        elif month == 4:
            print("апрель")
        elif month == 5:
            print("май")
        elif month == 6:
            print("июнь")
        elif month == 7:
            print("июль")
        elif month == 8:
            print("август")
        elif month == 9:
            print("сентябрь")
        elif month == 10:
            print("октябрь")
        elif month == 11:
            print("ноябрь")
        else:
            print("декабрь")
    else:
        print("недопустимое значение")