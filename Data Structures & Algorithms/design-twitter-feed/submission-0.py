class Twitter:

    def __init__(self):
        
        self.timestamp = 0
        self.user_followers = defaultdict(list)        # dict(list)
        self.user_feed = defaultdict(list)             # dict(heap)

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.timestamp -= 1
        heapq.heappush(self.user_feed[userId], (self.timestamp, tweetId, userId))
        for user in self.user_followers[userId] :
            heapq.heappush(self.user_feed[user], (self.timestamp, tweetId, userId))



    def getNewsFeed(self, userId: int) -> List[int]:
        
        feed = list()

        while len(feed) < 10 and len(self.user_feed[userId]) >= 1 :
            feed.append(heapq.heappop(self.user_feed[userId]))

        for i in range(len(feed)) :
            heapq.heappush(self.user_feed[userId], feed[i])

        result = [ item[1] for item in feed ]

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId in self.user_followers[followeeId] : return
        self.user_followers[followeeId].append(followerId)

        for item in self.user_feed[followeeId]:
            if item[2] == followeeId :
                heapq.heappush(self.user_feed[followerId], item)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        new_feed = list()
        for item in self.user_feed[followerId] :
            if item[2] != followeeId : 
                heapq.heappush(new_feed, item)

        self.user_feed[followerId] = new_feed
        try :
            self.user_followers[followeeId].remove(followerId)
        except ValueError :
            pass



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)