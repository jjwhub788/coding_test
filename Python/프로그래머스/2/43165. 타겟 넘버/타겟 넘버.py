def solution(numbers, target):

    answer = 0

    # 1. DFS 함수 만들기
    def dfs(index, current_sum):
        nonlocal answer

        # 2. 모든 숫자를 다 사용했는지 확인
        if index == len(numbers):

            # 3. 현재 합이 target이면 정답 증가
            if current_sum == target:
                answer += 1

            return

        # 4. 현재 숫자를 더하는 경우로 DFS 호출
        dfs(index + 1, current_sum + numbers[index])

        # 5. 현재 숫자를 빼는 경우로 DFS 호출
        dfs(index + 1, current_sum - numbers[index])

    # 6. 시작점에서 DFS 호출
    dfs(0, 0)

    return answer