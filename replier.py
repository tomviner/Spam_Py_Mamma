from romannums import attempt_roman 

def hashtag(f):
    def inner(self, *args, **kwargs):
        return '@' + args[0] + ' ' + f(self, *args[1:], **kwargs) + " #ldnpydojo"
    return inner

class Replier(object):
    
    replies = {
        'mum': "That's what your mum said",    
        'anywhere': 'You must check out PythonAnywhere.com',
    }


    keywords = {
        'where': replies['anywhere'],
        'hammer': replies['mum'],
        'drunk': replies['mum'],
        'drink': replies['mum'],
        'beer': replies['mum'],
    }

    def analyse_tweet(self, tweet):
        roman_result = attempt_roman(tweet)
        if roman_result:
            return "Mama says romans count it as: %d" % roman_result

        for keyword, reply in self.keywords.items():
            if keyword in tweet:
                return reply
        return "Spammama doesn't know"

replier = Replier()
print replier.analyse_tweet('I got hammered today');
print replier.analyse_tweet('Fancy a meal somwhere?');
print replier.analyse_tweet('MMCXL');