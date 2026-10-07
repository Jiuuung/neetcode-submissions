class Twitter:

    def __init__(self):
        self.user = defaultdict(list)
        self.follows = defaultdict(set)
        self.post_num = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_num+=1
        self.user[userId].append((self.post_num,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = list(self.user[userId])
        for followee in self.follows[userId]:
            feeds.extend(self.user[followee])
        heap=[]
        for feed in feeds:
            heapq.heappush(heap, feed)
            if len(heap)>10:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
