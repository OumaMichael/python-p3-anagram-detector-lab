# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(word)

    def match(self, candidates):
        return [word for word in candidates if sorted(word) == self.sorted_word]    
listen = Anagram("listen")
silent = Anagram("silent")
listen.match(['enlists', 'google', 'inlets', 'banana'])
for word in listen.match(['enlists', 'google', 'inlets', 'banana']):
    print(word)
    sorted_word = sorted(word)
    print(sorted_word)