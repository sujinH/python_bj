import sys
import heapq
sys.stdin = open("C:/Users/현대오토13/Desktop/수진_개인파일/파이썬/input.txt","r")
input = sys.stdin.readline

# 택배 배송
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))
    graph[b].append((cost, a))


def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 1))
    costs = [sys.maxsize] * (N+1)
    costs[1] = 0
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v == N:
            return costs[cur_v]
        if costs[cur_v] < cur_cost:
            continue
        for next_cost, next_v in graph[cur_v]:
            if cur_cost+next_cost < costs[next_v]:
                costs[next_v] = cur_cost+next_cost
                heapq.heappush(pq, (cur_cost+next_cost, next_v))


print(dijkstra())