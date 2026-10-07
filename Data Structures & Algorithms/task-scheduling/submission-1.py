class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic= defaultdict(int)
        for task in tasks:
            dic[task]+=1
        group = [(-v,k) for k, v in dic.items()]
        heapq.heapify(group)
        max_task_num= -heapq.heappop(group)[0]
        m=1
        while len(group)>0 and max_task_num==-heapq.heappop(group)[0]:
            m+=1
        ans = (max_task_num-1)*(n+1)+m
        return max(len(tasks), ans)