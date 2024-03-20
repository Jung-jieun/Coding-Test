t = int(input())

for time in [300,60,10]:
    if t%10!=0:
        print(-1)
        break
    else:
        if t>=time:
            print(t//time, end=' ')
            t %= time
        else:
            print(0, end=' ')