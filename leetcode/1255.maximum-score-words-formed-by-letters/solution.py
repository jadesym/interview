class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lower_case_chars = string.ascii_lowercase

        char_score_map = { lower_case_chars[i] : score[i] for i in range(len(lower_case_chars)) }

        letters_count = {}
        for letter in letters:
            if letter not in letters_count:
                letters_count[letter] = 0
            letters_count[letter] += 1

        # print("Printing char score map")
        # print(char_score_map)
        # print("Printing letter count")
        # print(letters_count)

        word_char_map = {}
        for i in range(len(words)):
            word = words[i]
            word_char_map[i] = {}
            for char in word:
                if char not in word_char_map[i]:
                    word_char_map[i][char] = 0
                word_char_map[i][char] += 1
        
        # print("Outputting word char map")
        # for word in word_char_map:
        #     print(words[word], word_char_map[word])

        word_scores = {}
        for i in range(len(words)):
            cur_word_score = 0
            word = words[i]

            for char in word:
                cur_word_score += char_score_map[char]

            word_scores[i] = cur_word_score
        # print("Word Scores")
        # for word in word_scores:
        #     print(words[word], word_scores[word])

        max_score = 0
        for subset in self.getSubsets(words, 0):
            # print([words[wordIndex] for wordIndex in subset])
            count_sum_map = {}
            for wordIndex in subset:
                for key, val in word_char_map[wordIndex].items():
                    if key not in count_sum_map:
                        count_sum_map[key] = 0
                    count_sum_map[key] += val
            
            is_subset_within = True
            for key, val in count_sum_map.items():
                if key not in letters_count:
                    is_subset_within = False
                    break
                if letters_count[key] < val:
                    is_subset_within = False
                    break

            if not is_subset_within: continue

            # Indication that the number of characters is within the letters
            local_score = 0
            for wordIndex in subset:
                local_score += word_scores[wordIndex]

            # print(local_score, "-", [words[wordIndex] for wordIndex in subset])

            max_score = max(local_score, max_score)
        return max_score
                
    def getSubsets(self, words: List[str], index: int) -> List[List[int]]:
        if len(words) == 0 or index >= len(words): return [[]]

        result = []

        for nested_subset in self.getSubsets(words, index + 1):
            result.append([index] + nested_subset)
            result.append(nested_subset)
        return result

