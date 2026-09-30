from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]* 102 for _ in range(102)]
    
    for x1, y1, x2, y2 in rectangle:
        
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1
    
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        
        for x in range(x1+1 , x2):
            for y in range(y1+1, y2):
                board[x][y] = 0
    
    characterX *=2
    characterY *=2
    itemX *= 2
    itemY *= 2
    
    #bfs 초기세팅
    q = deque()
    visited = [[0]* 102 for _ in range(102)]
    
    #시작점 예약
    q.append((characterX, characterY))
    visited[characterX][characterY] =1
    
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    #while문
    while q:
        #방문
        x, y =q.popleft()
        
        #도착했다면?
        if x == itemX and y == itemY:
            return (visited[x][y] -1) //2
        
        #다음 위치 확인
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<102 and 0<=ny<102:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    #거리 갱신
                    visited[nx][ny] = visited[x][y] +1
                    
                    q.append((nx,ny))
        
    
    