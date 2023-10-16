def mystery_3(a, b=None):
    if b is None:
        b = []
    if len(a) == 0:
        return b
    else:
        c = min(a)
        a.remove(c)
        b.append(c)
        return mystery_3(a, b)
