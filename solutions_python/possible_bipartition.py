#Problem 886:Possible Bipartition

# Given a set of N people(numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

# Each person may dislike some other people, and they should not go into the same group.

# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

# Return true if and only if it is possible to split everyone into two groups in this way.


# Example 1:

# Input: N = 4, dislikes = [[1, 2], [1, 3], [2, 4]]
# Output: true
# Explanation: group1[1, 4], group2[2, 3]
# Example 2:

# Input: N = 3, dislikes = [[1, 2], [1, 3], [2, 3]]
# Output: false
# Example 3:

# Input: N = 5, dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
# Output: false

from queue import Queue


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        visited = [0] * N
        graph = [[] for _ in range(N)]
        for edge in dislikes:
            u = edge[0] - 1
            v = edge[1] - 1
            graph[u].append(v)
            graph[v].append(u)

        q = Queue()
        for i in range(0, N):
            if visited[i] != 0:
                continue
            visited[i] = 1
            q.put(i)
            while not q.empty():
                s = q.qsize()
                for j in range(0, s):
                    u = q.get()
                    for k in range(0, len(graph[u])):
                        v = graph[u][k]
                        if visited[v] == 0:
                            visited[v] = 2 if visited[u] == 1 else 1
                            q.put(v)

                        if visited[v] == visited[u]:
                            return False

        return True
