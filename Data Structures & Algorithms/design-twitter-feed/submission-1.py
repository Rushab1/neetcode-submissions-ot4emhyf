class Twitter:
    tick = 0

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, Twitter.tick))
        Twitter.tick += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        i = 10

        followees = list(self.follows[userId]) + [userId]
        idxs = [len(self.tweets[followeeId]) - 1 for followeeId in followees]

        # print(followees, self.tweets)

        while i > 0 :
            _max = -1
            _max_idx = None
            break_flag = True

            for i, fid in enumerate(followees):
                # print(i, fid, idxs[i])
                if idxs[i] >= 0:
                    break_flag = False
                    # print("break false")
                else:
                    continue

                if _max < self.tweets[fid][idxs[i]][1]:
                    _max = self.tweets[fid][idxs[i]][1]
                    _max_idx = i

            if break_flag:
                break

            _fid = followees[_max_idx]
            _fidx = idxs[_max_idx]

            ret.append(self.tweets[_fid][_fidx][0])
            idxs[_max_idx] -= 1

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
