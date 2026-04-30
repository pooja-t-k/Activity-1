from collections import deque

def canFinish(numCourses, prerequisites):
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            queue.append(i)

    count = 0

    while queue:
        course = queue.popleft()
        count += 1

        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return count == numCourses

numCourses = 2
prerequisites = [[1, 0]]
print("Can finish all courses:", canFinish(numCourses, prerequisites))
