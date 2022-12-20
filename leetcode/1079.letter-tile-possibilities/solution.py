class Solution:
    # AAB: {A:2, B:1}
    def numTilePossibilities(self, tiles: str) -> int:
        results = self.genPerms(list(tiles))
        return len(results)
    def genPerms(self, tiles: List[str]) -> Set[str]:
        if len(tiles) == 0: return set()
        elif len(tiles) == 1: return set(tiles[0])
        perms_to_return = set()
        for i in range(len(tiles)):
            curTile = tiles[i]
            others = tiles[:i] + tiles[i + 1:]
            nestedPerms = self.genPerms(others)
            perms_to_return.update(nestedPerms)
            for perm in nestedPerms:
                new_perm = curTile + perm
                perms_to_return.add(new_perm)
        return perms_to_return
        
