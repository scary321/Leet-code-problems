class Solution(object):
    def isPalindrome(self, x):
        self.num = x
        self.total = 0
        while self.num > 0:
            self.ids = self.num % 10
            self.total = (self.total * 10) + self.ids
            self.num //=10
        return x == self.total

