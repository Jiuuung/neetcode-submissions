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
        heapq.heapify(feeds)
        while len(feeds)>10:
            heapq.heappop(feeds)
        for followee in self.follows[userId]:
            for feed in self.user[followee]:
                heapq.heappush(feeds, feed)
                if len(feeds)>10:
                    heapq.heappop(feeds)
        res = []
        while feeds:
            res.append(heapq.heappop(feeds)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
