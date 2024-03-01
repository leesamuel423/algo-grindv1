# 207. Course Scheduler
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        courses_left = [0] * numCourses
        visited = set()
        self.adj_graph(prerequisites, adj, courses_left)
        for index, num in enumerate(courses_left):
            if num == 0 and index not in visited:
                visited.add(index)
                self.dfs(index, adj, courses_left, visited)
        return len(visited) == numCourses

    def adj_graph(self, prereq, adj, courses_left):
        for i in prereq:
            adj[i[1]].append(i[0])
            courses_left[i[0]] += 1

    def dfs(self, curr, adj, courses_left, visited):
        for i in adj[curr]:
            courses_left[i] -= 1
            if courses_left[i] == 0:
                visited.add(i)
                self.dfs(i, adj, courses_left, visited)


"""
main fn:
adj = dic initialized w/ list
courses_left list initialized to size numCourses and 0 -> keeps track of number of prereqs needed to take that course
visited set initialize
initialize adjacency graph and list
iterate through courses_left:
  if courses_left is 0 and not in visited:
    dfs(course, adj, courses_left, visited)



def adj_graph(prereq, adj):
  iterate through prereq:
    add prereq[0] to prereq[1]
    add 1 to courses_left at index of prereq[0]

def dfs(curr, adj, courses_left, visited):
  for items in adj[curr]: -> [0, 1, 2, 3]
    if not in visited and
    

  

"""
