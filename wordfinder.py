class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.path = path
        self.wordList = self.read_file()
    

    def read_file(self):
        """ Get words from file line by line and return a list of those words """

        with open(self.path) as f:
            word_list = f.read().splitlines()
        
        print(f"{len(word_list)} words read")

        return word_list

    def random():
        """ Get random word from self.wordList """



        return
