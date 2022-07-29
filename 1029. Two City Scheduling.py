class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        li = []
        for cost in costs:
            cost.insert(0,abs(cost[0]-cost[1]))
            if cost[1] > cost[2]:
                cost.insert(1,'b')
            else:
                cost.insert(1,'a')
            li.append(cost)
        
        li = sorted(li, reverse=True)
        size = len(costs)
        amount_a = 0
        amount_b = 0
        total = 0
        for cost in li:
            if (cost[1] == 'a' and amount_a < size/2) or amount_b >= size/2:
                total += cost[2]
                amount_a += 1
            else:
                total += cost[3]
                amount_b += 1

        return total

sl = Solution()

print(sl.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))

