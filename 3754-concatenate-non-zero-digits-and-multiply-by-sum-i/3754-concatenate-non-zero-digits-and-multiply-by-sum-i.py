class Solution(object):
    def sumAndMultiply(self, n):
        x=0
        total=0
        for i in str(n):
            if i !='0':
                x=x*10+int(i)
        for j in str(x):
            total= total+int(j)
               
        
        return x*total
        