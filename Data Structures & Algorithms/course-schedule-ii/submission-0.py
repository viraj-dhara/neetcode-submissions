class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        
        temp = defaultdict(list)
        for course, prereq in prerequisites :
            temp[course].append(prereq)

        prerequisites = temp

        visited = set()
        curr_cycle = set()
        result = list()

        def dfs(course: int) :

            if course in visited :
                return True
            elif course in curr_cycle : return False

            curr_cycle.add(course)
            for prereq in prerequisites[course] :
                if dfs(prereq) == False :
                    return False
            curr_cycle.remove(course)

            visited.add(course)

            result.append(course)

            return True


        for i in range(numCourses):
            if dfs(i) == False :
                return []

        return result
            