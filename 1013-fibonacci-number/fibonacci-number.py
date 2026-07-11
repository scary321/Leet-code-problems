class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    def fib1(self,num):
        answer = self.fib(num)
        return answer