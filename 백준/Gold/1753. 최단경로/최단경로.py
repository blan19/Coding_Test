import heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
start = int(input())-1
dist = [float('inf')] * v
dist[start] = 0

linked = [[] for i in range(v)]
for i in range(e):
    a,b,w = map(int,input().split())
    linked[a-1].append((b-1,w))

heap = []
heapq.heappush(heap, (0,start))
    
while(heap):
    curDist,curNode = heapq.heappop(heap)
    if dist[curNode] < curDist:
        continue
        
    for toNode, toDist in linked[curNode]:
        d = curDist + toDist
        if dist[toNode] > d:
            dist[toNode] = d
            heapq.heappush(heap, (d, toNode))
            
for i in dist:
    print(i if i != float('inf') else "INF")