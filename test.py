import heapq
res = []
p = [[1,3],[-2,2],[2,-2]]
for i in range(len(p)):
    res.append((-(p[i][0]**2 + p[i][1]**2), i))
heapq.heapify(res)
print(res)
