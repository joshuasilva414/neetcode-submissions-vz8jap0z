class PrefixTree:

    def __init__(self):
        self.ending = False
        self.children = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.ending = True
        else:
            if word[0] not in self.children:
                self.children[word[0]]=PrefixTree()
            self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word)==0:
            return self.ending
        elif word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix)==0:
            return True
        elif prefix[0] in self.children:
            return self.children[prefix[0]].startsWith(prefix[1:])
        else:
            return False