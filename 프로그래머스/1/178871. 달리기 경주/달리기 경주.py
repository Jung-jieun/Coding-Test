def solution(players, callings):
    answer = []
    race = {}
    
    for rank, player in enumerate(players):
        if player not in race:
            race[player] = rank+1
    
    
    for call in callings:
        idx = race[call]
        race[call] -= 1
        race[players[idx-2]] += 1
        
        players[idx-2], players[idx-1] = players[idx-1], players[idx-2]
    
    return players