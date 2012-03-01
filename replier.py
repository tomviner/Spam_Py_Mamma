


class Replier(object):
    
    replies = {
        'mum': "That's what your mum said",    
        'anywhere': 'PythonAnywhere DOT com',
    }


    keywords = {
        'where': replies['anywhere'],
        'hammer': replies['mum'],
        'drunk': replies['mum'],
        'drink': replies['mum'],
        'beer': replies['mum'],
    }

    def analyse_tweet(self, tweet):
       for keyword, reply in self.keywords.items():
           if keyword in tweet:
               return reply

replier = Replier()
print replier.analyse_tweet('I got hammered today');
print replier.analyse_tweet('Fancy a meal somwhere?');