class Twitter:

    def __init__(self):
        self.user = defaultdict(list)
        self.follows = defaultdict(set)
        self.post_num = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_num+=1
        self.user[userId].append((self.post_num,tweetId))
        if len(self.user[userId])>10:
            self.user[userId].pop(0)

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds=[]
        for feed in self.user[userId]:
            heapq.heappush(feeds, feed)
            if len(feeds) > 10:
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
        """솔루션 풀이는 지금처럼 한명의 모든 피드를 넣는게 아닌 모든 사람의 최신 피드를 하나씩 
        가져오고 이후 그중에서 최신 하나 뽑아내고 해당 최신 피드를 적은 유저의 그 다음 피드를 하나
        다시 heap에 넣고 다시 최신 피드 모음에서 가장 최신 하나 뽑고 해당 최신 피드를 적은 유저의 그 다음
        피드를 하나 다시 heap에 넣는 방식으로 res가 10 이 될때까지 반복함. 이렇게 하면 각 유저의 최신들을
        우선적으로 가져오기 때문에 한명의 모든 피드를 heap에 넣으면서 개수 유지하는것보다 효율적임."""

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
