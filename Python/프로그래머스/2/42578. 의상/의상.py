def solution(clothes):
    count ={}
    
    for cloth in clothes:
        name = cloth[0]
        kind = cloth[1]
        
        count[kind] = count.get(kind, 0) +1
        
        answer = 1
        
    for value in count.values():
        answer *=(value +1)
    
    return answer -1
            
        