class Solution:
    def createElement(self, n: int, element: list = []) -> list[int]:
        newElement = []
        for i in range(n):
            if (i==0 or i==n-1):
                newElement.append(1)
            else:
                newElement.append(element[i-1] + element[i])
        return newElement
    
    def generate(self, numRows: int) -> list[list[int]]:
        pasTri = []
        for i in range(numRows):
            if i==0 or i==1:
                pasTri.append(self.createElement(i+1))
            else:  
                pasTri.append(self.createElement(i+1, pasTri[i-1]))
        return pasTri
    
S1 = Solution()
triangle = S1.generate(23)
for i in triangle:
    print(i)