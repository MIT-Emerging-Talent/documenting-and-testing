def mystery_2(a, b):
    if len(a) == 0:
        return []
    else:
        if b in a[0]:
            return [a[0]] + mystery_2(a[1:], b)
        else:
            return mystery_2(a[1:], b)
