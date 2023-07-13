S = input()
answer = []
from string import ascii_lowercase
alphabet = list(ascii_lowercase)
for i in alphabet:
    answer.append(S.find(i))
print(*answer)