def solution(cacheSize, cities):
    answer = 0
    stack = []
    for city in cities:
        city = city.casefold()
        if city not in stack:
            if len(stack)<cacheSize:
                stack.append(city)
            elif len(stack)==cacheSize:
                    stack.append(city)
                    stack.pop(0)
            answer += 5
        else:
            stack.remove(city)
            stack.append(city)
            answer += 1
    return answer