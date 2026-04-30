def hammingWeight(n):
    count = 0

    while n:
        n = n & (n - 1)  
        count += 1

    return count
n = 11
result = hammingWeight(n)
print("Number of set bits:", result)
