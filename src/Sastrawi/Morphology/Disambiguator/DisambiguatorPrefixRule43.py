import re

class DisambiguatorPrefixRule43(object):
    """Disambiguate Prefix Rule 43
    Rule 43 : ngeA*in -> nge-H-in
    """
    
    def disambiguate(self, word):
        """Disambiguate Prefix Rule 43
        Rule 43 : ngeA -> nge-H
        """
        matches = re.match(r'^ng(a)(.*)in$', word)
        if matches:
            return 'h' + matches.group(1) + matches.group(2)
        else:            
            matches = re.match(r'^nga(b)(.*)in$', word)
            if matches:
                return 'ka' + matches.group(1) + matches.group(2)