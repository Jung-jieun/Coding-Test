def solution(sizes):
    answer = 0
    width = []
    height = []
    
    for size in sizes:
        width.append(max(size[0], size[1]))
        height.append(min(size[0], size[1]))
        
    return max(width)*max(height)