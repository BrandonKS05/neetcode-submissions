class PrefixTree:

    def __init__(self):
        self.dictionary = []
        
    def insert(self, word: str) -> None:
        self.dictionary.append(word)

    def search(self, word: str) -> bool:
        return word in self.dictionary
    
    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for string in self.dictionary:
            string = string[:n]
            if prefix == string:
                return True
        return False

       

        