import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.path = path
        self.word_list = self.read_file()
    
    # CR maybe think about opening the file in __init__
    # so read_file becomes more parse or parse_contents and
    # can handle polymorphism better with SpecialWordFinder
    def read_file(self):
        """ Get words from file line by line and return a list of those words """

        with open(self.path) as f:
            word_list = f.read().splitlines()
        
        print(f"{len(word_list)} words read")

        return word_list

    def random(self):
        """ Get random word from self.word_list """
    #CR also think about random.choice(list) 
        return self.word_list[random.randrange(0,len(self.word_list))]


class SpecialWordFinder(WordFinder):
    """ Special Word Finder inherits from WordFinder,
     can parse blank lines and ignore comment lines
     """
    def __init__(self, path):
        """ Initializing function, inherits with super(),
        creates SpecialWordFinder which ignores comments
        and new lines.
         """
        super().__init__(path)
        self.word_list = self.handle_special_lines()

    def handle_special_lines(self):
        """ Removes comments and new lines from initally read
        text file  """
    # CR no need to set variable, just return it
        return [wrd for wrd in self.word_list 
            if not wrd == "" and 
            not wrd.startswith("#")]
                
        
