class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles #bottles drunk
        empty = numBottles #empty at the moment
        
        while empty  >= numExchange:
            if empty >= numExchange:
                empty -= numExchange
                full += 1
                empty+=1
                numExchange += 1
        return full