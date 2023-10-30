x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def CCW(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


def isoverlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) \
            and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        return True
    return False


def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = CCW(x1, y1, x2, y2, x3, y3)
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1)
    cdb = CCW(x3, y3, x4, y4, x2, y2)

    if abc * abd == 0 and cda * cdb == 0:
        return isoverlab(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    return False


cross = isCross(x1, y1, x2, y2, x3, y3, x4, y4)


def get_crosspt(x11, y11, x12, y12, x21, y21, x22, y22):
    if x12 == x11 or x22 == x21:
        print(x12, x12)
        return
    m1 = (y12 - y11) / (x12 - x11)
    m2 = (y22 - y21) / (x22 - x21)
    if m1 == m2:
        print(x12, x12)
        return

    cx = (x11 * m1 - y11 - x21 * m2 + y21) / (m1 - m2)
    cy = m1 * (cx - x11) + y11
    if float(cx).is_integer():
        print(int(cx), int(cx))
    else:
        print("{:.16f}".format(cx), "{:.16f}".format(cy))
    return


if cross:
    print(1)
    get_crosspt(x1, y1, x2, y2, x3, y3, x4, y4)
else:
    print(0)
