def value(d, *k):
    if type(d) == str:
        return d
    if len(k) == 0:
        return d
    v = d.get(k[0], '')
    if type(v) == dict:
        return value(v, *k[1:])
    else:
        return v

