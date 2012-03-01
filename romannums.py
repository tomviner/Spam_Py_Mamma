
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


def attempt_roman(tweet):
    """
    >>> attempt_roman('I love you!')
    1
    >>> attempt_roman('Please tell me the arabic numeral for MMXII')
    2012
    >>> attempt_roman('this has no roman NUMS')

    """
    for word in tweet.split():
        try:
            return to_den(word)
        except KeyError:
            pass
    return None
