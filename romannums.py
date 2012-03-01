
vals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def to_den(rom):
    """
    >>> to_den('I')
    1
    >>> to_den('XXIV')
    24
    """
    tot = 0
    last_l = 0
    for l in rom.upper()[::-1]:
        val = vals[l]
        if val < last_l:
            tot -= val
        else:
            tot += val
        last_l = val
    return tot

