n = int(input())
data = input()
answer = ''
i=0
while i<n:
    if answer=='':
        if data[i]=="S":
            answer += "*S*"
        elif data[i:i+2]=="LL":
            answer += "*LL*"
            i += 2
            continue
    else:
        if data[i]=="S":
            answer += "S*"
        elif data[i:i+2]=="LL":
            answer += "LL*"   
            i+= 2
            continue
    i += 1
result = answer.count("*")
print(min(result, n))