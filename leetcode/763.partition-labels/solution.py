class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1: return [1]
        char_map = {}
        for i in range(len(s)):
            char = s[i]
            if char not in char_map:
                char_map[char] = {
                    "first": i,
                    "last": i
                } 
            else:
                char_map[char]["last"] = i
        local_char_set = set()
        last_local_index = None
        partition_count = 0
        partition_counts = []
        for i in range(len(s)):
            char = s[i]
            partition_count += 1
            if last_local_index is None:
                last_current_index = char_map[char]["last"]
                if last_current_index == i:
                    partition_counts.append(partition_count)
                    local_char_set = set()
                    last_local_index = None
                    partition_count = 0
                else:
                    local_char_set.add(char)
                    last_local_index = last_current_index
            elif last_local_index == i:
                partition_counts.append(partition_count)
                local_char_set = set()
                last_local_index = None
                partition_count = 0
            else:
                local_char_set.add(char)
                last_current_char_index = char_map[char]["last"]
                last_local_index = max(last_local_index, last_current_char_index)
        return partition_counts

