#초기 상태: 시작점 정의
#반복문:routes 안에서 park 행과 열에 대해 순회 
#조건:공원 벗어났는가, 장애물을 만났는가 -> 무시 다음 명령 실행
#최종 상태:최종 좌표 
def solution(park, routes):
    rows = len(park)
    cols = len(park[0])
    
    answer = []
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                row = i
                col =j
    
    for route in routes:
        direction, distance = route.split()
        
        distance = int(distance)
        
        new_row = row
        new_col = col
        
        possible = True
        
        for _ in range(distance):
            
            if direction == "N":
                new_row -=1
            elif direction == "S":
                new_row +=1
            elif direction == "W":
                new_col -= 1
            elif direction == "E":
                new_col += 1
                
            if new_row < 0 or new_row >= rows or \
            new_col < 0 or new_col >=cols:
                possible =False
                break
                
            if park[new_row][new_col] == "X":
                possible = False
                break
                
        if possible:
            row = new_row
            col = new_col
    return [row, col]
            
            