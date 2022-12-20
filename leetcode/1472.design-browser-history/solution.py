class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        self.urls = self.urls[0:self.index + 1]
        self.urls.append(url)
        self.index += 1

    def back(self, steps: int) -> str:
        maxIndex = max(0, self.index - steps)
        self.index = maxIndex
        return self.urls[maxIndex]

    def forward(self, steps: int) -> str:
        minIndex = min(len(self.urls) - 1, self.index + steps)
        self.index = minIndex
        return self.urls[minIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)