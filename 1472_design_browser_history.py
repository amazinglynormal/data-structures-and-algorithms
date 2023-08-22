class Node:
    def __init__(self, url: str, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = Node(homepage)
        self.tail = self.homepage
        self.current = self.homepage

    def visit(self, url: str) -> None:
        new_url = Node(url, self.current)
        self.current.next = new_url
        self.tail = new_url
        self.current = new_url

    def back(self, steps: int) -> str:
        remaining_steps = steps

        while self.current.prev and remaining_steps > 0:
            self.current = self.current.prev
            remaining_steps -= 1

        return self.current.url

    def forward(self, steps: int) -> str:
        remaining_steps = steps

        while self.current.next and remaining_steps > 0:
            self.current = self.current.next
            remaining_steps -= 1

        return self.current.url


bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")
print(bh.back(1))  # facebook
print(bh.back(1))  # google
print(bh.forward(1))  # facebook
bh.visit("linkedin.com")
print(bh.forward(2))  # linkedin
print(bh.back(2))  # google.com
print(bh.back(7))  # leetcode
