class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def construct_trie(words) -> dict:

            root = dict()
            curr = root

            for word in words : 
                
                for letter in word :
                    if letter not in curr : curr[letter] = dict()
                    curr = curr[letter]

                curr["isWord"] = True
                curr = root

            return root

        root = construct_trie(words)

        # print(root, "\n")

        def dfs_backtracking(curr_word, curr_dict, curr_coods : Tuple, visited_letters) : 

            i, j = curr_coods
            
            # print("++++", curr_coods, visited_letters, curr_word,  "\n\n", curr_dict, "\n")

            if board[i][j] not in curr_dict : return
            
            curr_word.append(board[i][j])
            curr_dict = curr_dict[board[i][j]]

            visited_letters.add((i,j))
            
            if "isWord" in curr_dict : 
                _ = ""
                for letter in curr_word :
                    _ += letter
                results.add(_)

            valid_coods = []
            if i > 0 :
                valid_coods.append((i - 1, j))
            if j > 0 :
                valid_coods.append((i, j - 1))
            if i < len(board) - 1 :
                valid_coods.append((i + 1, j))
            if j < len(board[0]) - 1 :
                valid_coods.append((i, j + 1))
            
            # print(valid_coods, "\n")

            for l, m in valid_coods :
                if (l,m) in visited_letters : continue
                dfs_backtracking(curr_word, curr_dict, (l, m), visited_letters)
            
            if curr_word : 
                visited_letters.remove((i,j))
                curr_word.pop(-1)
            
            # print("~~~~~~~full loop~~~~~~")


        results = set()
        

        for i in range(len(board)) :
            for j in range(len(board[0])) :
                # print("--------------------")
                dfs_backtracking([], root, (i,j), set())     

        return list(results)



