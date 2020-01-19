def intToBool(n: int):
    if n == 0:
        return ""
    else:
        return intToBool(n // 2) + str(n % 2)


def boolToInt(n: int) -> int:
    if n == 0:
        return 0
    else:
        return ((n % 10) + 2 * boolToInt(n // 10))

############### TEST ###############
# print(intToBool(4))
# print(boolToInt(111))
