def solution(bridge_length, weight, truck_weights):
    time = 0
    # 다리를 건너는 트럭
    bridge = [0 for _ in range(bridge_length)]
    bridge_weight = 0
    
    while bridge :
        time += 1
        out_truck = bridge.pop(0)
        bridge_weight -= out_truck
        if truck_weights:
            # bridge weight와 다음 truck의 무게가 weight를 넘지않으면 추가
            if bridge_weight + truck_weights[0] <= weight: 
                pass_truck = truck_weights.pop(0)
                bridge.append(pass_truck)
                bridge_weight += pass_truck
            else:
                bridge.append(0)
    
    return time