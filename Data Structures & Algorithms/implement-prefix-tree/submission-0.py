class PrefixTree:

    def __init__(self):
        self.trie = {}
        
    def insert(self, word: str) -> None:
        it = self.trie
        for s in word:
            if s not in it:
                it[s] = {}

            it = it[s]

        it["end"] = {}

    def search(self, word: str) -> bool:
        it = self.trie
        for s in word:
            if s not in it:
                return False
            it = it[s]

        if "end" in it:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        it = self.trie
        for s in prefix:
            if s not in it:
                return False
            it = it[s]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix) 