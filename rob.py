def rob(nums):
    prev1 = 0  
    prev2 = 0  

    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current

    return prev1
nums = [2, 7, 9, 3, 1]
result = rob(nums)
print("Maximum money you can rob:", result)
