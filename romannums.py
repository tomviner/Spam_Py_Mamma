import re

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
    '1'
    >>> to_den('XXIV')
    '24'
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
    return str(tot)

def splitter(s):
    prolematic_chars = '()+-/*'
    for l in prolematic_chars: 
        s = s.replace(l, ' %s ' % l)
    return s.split()

def attempt_roman(tweet):
    """
    >>> attempt_roman('I love you!')
    
    >>> attempt_roman('Please tell me the arabic numeral for MMXII')
    'Please tell me the arabic numeral for 2012'
    >>> attempt_roman('( IV + MM ) / II')
    '1002'
    >>> attempt_roman('(IV+MM)/II')
    '1002'
    >>> attempt_roman('this has no roman NUMS')

    """
    orig = tweet
    for word in splitter(tweet):
        if tweet == orig and len(word) == 1:
            continue
        try:
            tweet = tweet.replace(word, to_den(word))
        except KeyError:
            pass
        #print tweet
    if orig != tweet:
        #print ''.join(sorted(set(tweet)))
        #print ''.join(sorted(set('()1234567890+-/*. ')))
        if not set(tweet) - set('()1234567890+-/*. '):
            return str(eval(tweet))
        return tweet
    return None
