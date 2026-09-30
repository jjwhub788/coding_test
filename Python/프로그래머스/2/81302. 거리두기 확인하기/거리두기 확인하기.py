from collections import deque

def solution(places):

    answer = []

    # 대기실 5개 확인
    for place in places:

        safe = True

        # 사람 P 찾기
        for sx in range(5):
            for sy in range(5):

                if place[sx][sy] == "P":

                    # P가 시작점인 BFS
                    q = deque()
                    visited = [[False] * 5 for _ in range(5)]

                    # 시작점 넣기
                    q.append((sx, sy, 0))
                    visited[sx][sy] = True

                    # 상하좌우
                    dx = [-1, 1, 0, 0]
                    dy = [0, 0, -1, 1]

                    # BFS
                    while q:

                        x, y, dist = q.popleft()

                        # 거리 2까지 확인했으면 더 이상 퍼지지 않음
                        if dist == 2:
                            continue

                        for i in range(4):

                            nx = x + dx[i]
                            ny = y + dy[i]

                            # 범위 안인지
                            if 0 <= nx < 5 and 0 <= ny < 5:

                                # 방문하지 않았다면
                                if not visited[nx][ny]:

                                    # 파티션은 지나갈 수 없음
                                    if place[nx][ny] == "X":
                                        continue

                                    # 다른 사람 발견 → 거리두기 실패
                                    if place[nx][ny] == "P":
                                        safe = False
                                        break

                                    # 빈 자리면 계속 BFS
                                    visited[nx][ny] = True
                                    q.append((nx, ny, dist + 1))

                        # 이미 실패했으면 BFS 종료
                        if not safe:
                            break

                # 이미 실패했으면 더 확인할 필요 없음
                if not safe:
                    break

            if not safe:
                break

        # 현재 대기실 결과 저장
        if safe:
            answer.append(1)
        else:
            answer.append(0)

    return answer