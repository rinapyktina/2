if __name__ == "__main__":
    k = int(input())
    d = 0
    if k % 7 == 0:
        print("воскресенье")
    elif k <= 7:
        d = k
    elif k % 7 != 0:
        d = k % 7
    else:
        d = k / 7
    if d == 1:
        print("понедельник")
    elif d == 2:
        print("вторник")
    elif d == 3:
        print("среда")
    elif d == 4:
        print("четверг")
    elif d == 5:
        print("пятница")
    elif d == 6:
        print("суббота")
© 2021 GitHub, Inc.
Terms
Privacy