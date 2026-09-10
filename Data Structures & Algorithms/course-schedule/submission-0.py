class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_req_courses = defaultdict(dict)
        dependant_courses = defaultdict(dict)

        for course, pre_req in prerequisites :
            pre_req_courses[course][pre_req] = 1
            dependant_courses[pre_req][course] = 1

        # print(f"{pre_req_courses = }\n{dependant_courses = }\n")

        myqueue = deque()

        for course in range(numCourses) :
            if pre_req_courses[course] == {} :
                myqueue.append(course)

        print(f"{myqueue = }")

        while myqueue :

            curr = myqueue.popleft()

            do_something = True
            for value in pre_req_courses[curr].values() :
                if value == 1 :
                    do_something = False

            if do_something :
                for dependant in list(dependant_courses[curr].keys()) :
                    pre_req_courses[dependant].pop(curr)
                    dependant_courses[curr].pop(dependant)
                    myqueue.append(dependant)

        # print(f"\n{pre_req_courses = }")
        for item in pre_req_courses.values() :
            for value in item.values() :
                if value :
                    return False
        
        return True
                
