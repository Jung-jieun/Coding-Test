def solution(people, limit):
    first = 0
    last = len(people) - 1
    answer = 0

    people.sort(reverse = True)

    while first <= last:

        if people[first] + people[last] <= limit:
            last -= 1

        first += 1
        answer += 1


    return answer