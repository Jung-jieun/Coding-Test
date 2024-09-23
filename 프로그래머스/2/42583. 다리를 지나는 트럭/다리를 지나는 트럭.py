from collections import deque
def solution(bridge_length, weight, truck_weights): 
    bridge_length = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights) 
    sec = 0 
    total = 0 
    while bridge_length: 
        sec += 1 
        passed_truck = bridge_length.popleft() 
        total -= passed_truck
        if truck_weights: 
            if total + truck_weights[0] <= weight: 
                truck = truck_weights.popleft() 
                total += truck 
                bridge_length.append(truck) 
            
            else: bridge_length.append(0) 
            
    return sec