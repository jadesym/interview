class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        lower_case = string.ascii_lowercase
        mapping = {}
        stripped_key = key.replace(" ", "")
        found_in_key = set()
        new_key = ""
        for char in stripped_key:
            if char not in found_in_key:
                found_in_key.add(char)
                new_key += char
            else:
                continue

        for i in range(len(new_key)):
            if new_key[i] not in mapping:
                mapping[new_key[i]] = lower_case[i % 26]
        # print("".join(mapping.keys()))
        # print("".join(mapping.values()))
        new_message = ""
        for char in message:
            if char in mapping:
                new_message += mapping[char]
            else:
                new_message += char
        return new_message