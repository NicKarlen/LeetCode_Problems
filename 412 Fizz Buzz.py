class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        li = []
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                li.append('FizzBuzz')
            elif i % 3 == 0:
                li.append('Fizz')
            elif i % 5 == 0:
                li.append('Buzz')
            else:
                li.append(str(i))
        
        return li


sol = Solution()

print(sol.fizzBuzz(15))