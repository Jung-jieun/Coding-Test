def solution(s):
    dic = {"zero":0, "one":1, "two":2, "three":3,
          "four":4, "five":5, "six":6, "seven":7,
          "eight":8, "nine":9}
    for i, j in dic.items():
        if i in s:
            s = s.replace(i, str(j))
    return int(s)