# 다익스트라 (dijkstra)
import heapq

def dijkstra(graph,start,final):
    costs = {}
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        cur_cost,cur_value = heapq.heappop(pq)
        if cur_value not in costs:
            costs[cur_value] = cur_cost
            for cost,next_v in graph[cur_value]:
                next_cost = cost + cur_cost
                heapq.heappush(pq,(next_cost, next_v))
    return costs[final]



dijkstra(graph,1,8)