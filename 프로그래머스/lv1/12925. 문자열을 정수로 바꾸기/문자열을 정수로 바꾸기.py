def solution(s):
    return -1*int(s[1:])  if "-" in s else int(s)