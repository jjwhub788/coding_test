def solution(tickets):
    tickets.sort()
    
    visited = [False] * len(tickets)
    
    answer = []
    
    def dfs(airport, path):
        
        if len(path) == len(tickets) +1:
            answer.extend(path)
            return True
        
        for i in range(len(tickets)):
            
            start, end = tickets[i]
            
            if start == airport and not visited[i]:
                visited[i] = True
                
                if dfs(end, path+[end]):
                    return True
                visited[i] =False
        return False
    dfs("ICN",["ICN"])
    
    return answer
                
                