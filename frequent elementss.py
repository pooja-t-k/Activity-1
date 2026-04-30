def topKFrequent(nums, k):
    freq_map = {}

    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in freq_map.items():
        bucket[freq].append(num)

    result = []

    for i in range(len(bucket) - 1, -1, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

nums = [1, 1, 1, 2, 2, 3]
k = 2
result = topKFrequent(nums, k)
print("Top K Frequent Elements:", result)
