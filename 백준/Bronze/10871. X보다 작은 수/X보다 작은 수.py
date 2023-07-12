N, X = map(int,input().split())
A = [int(j) for j in input().split()]
answer = [i for i in A if i<X]
print(' '.join(map(str, answer)))