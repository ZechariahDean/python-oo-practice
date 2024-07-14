"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    Program to find random words in a directory.
    >>> wf = WordFinder("/Users/student/words.txt")
    "3 words read"

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, path):
        """gets directory and prints the number of words"""
        file = open(path)
        self.words = self.parse(file)
        print(f"{len(self.words)} words read")

    def parse(self, file):
        """parse words from file return list of those words"""
        return [word.strip() for word in file]

    def random(self):
        """return random word"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    WordFinder sublclass for files that have gaps or comments
    >>> swf = SpecialWordFinder("text2.txt")
    4 words read

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    """
    def parse(self, file):
        """parse special file and return words skipping gaps and comments"""
        return [word.strip() for word in file if word.strip() and not word.startswith("#")]