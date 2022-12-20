import string

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alpha_chars = string.ascii_lowercase
        morse_chars = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        char_map = {}
        for i in range(len(alpha_chars)):
            alpha_char = alpha_chars[i]
            morse_char = morse_chars[i]
            char_map[alpha_char] = morse_char
        
        transformations = set()
        for word in words:
            translation = ''.join([char_map[char] for char in word])
            transformations.add(translation)
        return len(transformations)
            

        