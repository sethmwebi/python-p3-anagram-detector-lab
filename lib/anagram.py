# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, arr):
        matched_word = []
        for word in arr:
            if sorted(word) == sorted(self.word):
                matched_word.append(word)
        return matched_word


listen = Anagram("listen")
listen.match(["enlists", "google", "inlets", "banana"])

