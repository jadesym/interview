class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set()
        destinations = set()
        for source, dest in paths:
            sources.add(source)
            destinations.add(dest)
        for destination in destinations:
            if destination not in sources:
                return destination
        raise BaseException("Unable to find the final destination")