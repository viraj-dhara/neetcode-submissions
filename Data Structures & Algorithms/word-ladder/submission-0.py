class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        
        def replace_at(s: str, char: str, index: int) -> str :
            return s[:index] + char + s[index+1:]

        word_to_templ = defaultdict(list)
        templ_to_word = defaultdict(list)

        for i in range(len(beginWord)) :
            word_to_templ[beginWord].append(replace_at(beginWord, "*", i))

        for word in wordList :
            for i in range(len(word)) :
                word_to_templ[word].append(replace_at(word, "*", i))

        # print(f"{dict(word_to_templ) = }\n")

        for word in wordList :
            for templ in word_to_templ[word] :
                templ_to_word[templ].append(word)

        # print(f"{dict(templ_to_word) = }\n")


        queue = deque()
        queue.append((beginWord, 1))
        already_checked = set([beginWord])
        counter = 1

        while queue and endWord not in already_checked :


            curr_word, curr_counter = queue.popleft()

            # print(f"{queue , already_checked , counter , curr_word = }")

            for templ in word_to_templ[curr_word] :
                for word in templ_to_word[templ] :
                    if word not in already_checked :
                        
                        queue.append((word, curr_counter + 1))
                        already_checked.add(word)



            
            counter = min(counter, curr_counter) + 1

        if endWord not in already_checked : return 0

        return counter



                