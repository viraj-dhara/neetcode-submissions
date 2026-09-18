"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if intervals == [] : return 0
        
        intervals.sort(key = lambda item: item.start)

        meet_rooms = list()

        for interval in intervals :

            

            if not meet_rooms or meet_rooms[0][0] > interval.start :
                new_room = [interval.end, [[interval.start, interval.end]]]
                heapq.heappush(meet_rooms, new_room)

            else :
                free_room = heapq.heappop(meet_rooms)

                free_room[1].append([interval.start, interval.end])
                free_room[0] = interval.end

                heapq.heappush(meet_rooms, free_room)


        return len(meet_rooms)

