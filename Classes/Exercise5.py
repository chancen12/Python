class ex5:
   def FindSum(self, nums, target):
        b = {}
        for i, num in enumerate(nums):
            if target - num in b:
                return (b[target - num], i )
            b[num] = i
print(ex5().FindSum((10,15,35,70,80),50))