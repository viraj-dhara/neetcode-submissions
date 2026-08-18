import string

class WordDictionary:

    def __init__(self):
        
        self.dictionary = dict()

    def addWord(self, word: str) -> None:
        
        curr_dict = self.dictionary

        for letter in word :
            if letter not in curr_dict : curr_dict[letter] = dict()
            curr_dict = curr_dict[letter]

        curr_dict["isWord"] = True

        return

    def search(self, word: str) -> bool:
        
        curr_dict = self.dictionary

        for i in range(len(word)) :
            if word[i] == "." :
                for letter in string.ascii_lowercase :
                    if letter not in curr_dict : continue
                    tempword = word.replace(".", letter, 1)
                    if self.search(str(tempword)) == True : return True
                return False
            elif word[i] not in curr_dict :
                return False
            elif word[i] in curr_dict :
                curr_dict = curr_dict[word[i]]

        if "isWord" in curr_dict : return True
        else : return False
        
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


