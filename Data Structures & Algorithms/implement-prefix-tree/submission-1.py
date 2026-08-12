class PrefixTree:

    def __init__(self):
        
        self.myrecord = dict()

    def insert(self, word: str) -> None:

        if word[0] not in self.myrecord :
            self.myrecord[word[0]] = dict() 
        curr_dict = self.myrecord[word[0]]

        if len(word) == 1 : 
            curr_dict["isWord"] = True
            return

        for i in range(len(word) - 1) :
            curr_dict[word[i+1]] = dict() if word[i+1] not in curr_dict else curr_dict[word[i+1]] 
            curr_dict = curr_dict[word[i+1]]

        curr_dict["isWord"] = True

        # print("insert ", self.myrecord)

        return

    def search(self, word: str) -> bool:

        # print(self.myrecord)
        
        if word[0] not in self.myrecord : return False
        curr_dict = self.myrecord[word[0]] 

        for i in range(len(word) - 1) :
            if word[i+1] not in curr_dict : return False
            curr_dict = curr_dict[word[i+1]]

        return True if "isWord" in curr_dict else False

    def startsWith(self, prefix: str) -> bool:
        
        # print(self.myrecord)

        if prefix[0] not in self.myrecord : return False
        curr_dict = self.myrecord[prefix[0]]

        for i in range(len(prefix) - 1) :
            if prefix[i+1] not in curr_dict : return False
            curr_dict = curr_dict[prefix[i+1]] 

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)