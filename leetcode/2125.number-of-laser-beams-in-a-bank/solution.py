class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        one_counts = [x.count("1") for x in bank]
        last_one_count = None
        laser_count = 0
        for count in one_counts:
            if last_one_count is None:
                last_one_count = count
                continue
            if count == 0:
                continue
            laser_count += last_one_count * count
            last_one_count = count
        return laser_count
            
        