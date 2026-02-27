class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty=numBottles #counting empty ones
        a=numBottles #counting how much we can drink
        full=0 
        while empty>=numExchange:
            full = empty // numExchange
            empty = empty % numExchange + full
            a += full
        return a