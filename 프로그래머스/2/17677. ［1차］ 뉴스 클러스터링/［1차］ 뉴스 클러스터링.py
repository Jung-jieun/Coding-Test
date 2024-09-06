import re
from collections import Counter
def solution(str1, str2):
    A = []
    B = []
    
    for i in range(0,len(str1)):
        element1 = str1[i:i+2].lower()
        if re.match(r'[a-z]{2}', element1):
            A.append(element1)
        
    for j in range(0, len(str2)):
        element2 = str2[j:j+2].lower()
        if re.match(r'[a-z]{2}', element2):
            B.append(element2)
    
    counterA = Counter(A)
    counterB = Counter(B)
    
    union = sum((counterA|counterB).values())
    intersection = sum((counterA&counterB).values())
    
    if union==0:
        return 65536
    return int((intersection/union)*65536)