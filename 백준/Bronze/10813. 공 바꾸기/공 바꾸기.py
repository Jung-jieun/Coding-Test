N,M = map(int,input().split())
basket = [int(x) for x in range(1,N+1)]
for a in range(M):
    i,j = map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)