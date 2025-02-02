class pair_elements():
    
    def twoSum(self, nums, target):
        
        lookup = {}
        
        for i, num in enumerate(nums):
            if target - num in lookup:
                return(lookup[target-num],i)
            lookup[num] = i
        
value = int(input("Enter the number you'd like to see the sum of : "))

i1, i2 = pair_elements().twoSum((10, 20, 30, 40, 50, 60, 70, 80), value)
print(f"index1= {i1}, index2 = {i2}")