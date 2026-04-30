def climbStairs(n):
    if n <= 2:
        return n

    prev1 = 1  
    prev2 = 2  
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current

    return prev2
n = 5
result = climbStairs(n)
print("Number of ways:", result)
