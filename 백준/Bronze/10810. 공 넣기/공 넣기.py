N,M = map(int,input().split())
basket = [int() for x in range(N)]
for a in range(M):
    i,j,k = map(int,input().split())
    for b in range(i,j+1):
        basket[b-1]=k
print(*basket)