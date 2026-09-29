def solution(numbers, hand):
    answer = ""

    # 처음 손의 위치
    left = "*"
    right = "#"

    # 키패드의 위치
    position = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        "*": (3, 0), 0: (3, 1), "#": (3, 2)
    }

    for number in numbers:

        # 1, 4, 7은 왼손
        if number in [1, 4, 7]:
            answer += "L"
            left = number

        # 3, 6, 9는 오른손
        elif number in [3, 6, 9]:
            answer += "R"
            right = number

        # 2, 5, 8, 0은 거리 비교
        else:
            left_distance = (
                abs(position[left][0] - position[number][0])
                + abs(position[left][1] - position[number][1])
            )

            right_distance = (
                abs(position[right][0] - position[number][0])
                + abs(position[right][1] - position[number][1])
            )

            # 왼손이 더 가까움
            if left_distance < right_distance:
                answer += "L"
                left = number

            # 오른손이 더 가까움
            elif right_distance < left_distance:
                answer += "R"
                right = number

            # 거리가 같음
            else:
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number

    return answer