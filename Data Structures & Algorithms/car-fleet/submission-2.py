class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(list(zip(position, speed)), reverse=True)
        fleet=0
        stack=[]
        for p,s in car:
            time=(target-p)/s
            if stack and time<=stack[-1]:
                continue
            else:
                stack.append(time)
                fleet+=1
        return fleet