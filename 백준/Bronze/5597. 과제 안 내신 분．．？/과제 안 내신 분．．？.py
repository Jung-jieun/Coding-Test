N = []
for i in range(1,31):
    N.append(i)
    
M = [int(input()) for x in range(28)]
    
L = sorted(list(set(N)-set(M)))
print(L[0])
print(L[1])