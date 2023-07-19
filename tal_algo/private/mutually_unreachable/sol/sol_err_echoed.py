#!/usr/bin/env python3
from sys import stderr, setrecursionlimit
setrecursionlimit(10**9)
import random

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        print(f"Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b = map(int, input().strip().split())
            nei[a].append(b)
            nei[b].append(a)
        #print(f"{n=}, {m=}, {nei=}", file=stderr)    
        CC = []
        seen = [False] * n
        def dfs(u, C):
            global seen
            if not seen[u]:
                C.append(u)
                seen[u] = True
                for v in nei[u]:
                     dfs(v, C)
        for v in range(n):
            if not seen[v]:
                CC.append([])
                dfs(v, CC[-1])
        print(len(CC) + 1)
        for C in CC:
            print(C[0], end=" ")
        print(CC[random.randrange(len(CC))][0])
