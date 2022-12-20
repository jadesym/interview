import random

class RandomizedSet:

    def __init__(self):
        self.size = 0
        self.val_to_index = {}
        # linkedlist ({val: val})
        self.val_arr = []

    def insert(self, val: int) -> bool:
        new_index = len(self.val_arr)
        if val not in self.val_to_index:
            self.val_to_index[val] = new_index
            self.val_arr.append(val)
            return True
        else:
            return False
            

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        else:
            val_index = self.val_to_index[val]
            if val_index == len(self.val_arr) - 1:
                self.val_arr.pop()
                del self.val_to_index[val]
            else:
                last_item = self.val_arr.pop()
                self.val_arr[val_index] = last_item
                self.val_to_index[last_item] = val_index
                del self.val_to_index[val]
            return True
            

    def getRandom(self) -> int:
        return self.val_arr[random.randint(0, len(self.val_arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()