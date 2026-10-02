def solution(id_list, report, k):
    # 중복 신고 제거
    report = set(report)

    # 각 사람이 신고당한 횟수
    count = {}

    for name in id_list:
        count[name] = 0

    for reports in report:
        call, back = reports.split()
        count[back] += 1

    # 각 사람이 받을 메일 수
    mail = {}

    for name in id_list:
        mail[name] = 0

    # 정지된 사람을 신고한 사람에게 메일 +1
    for reports in report:
        call, back = reports.split()

        if count[back] >= k:
            mail[call] += 1

    # id_list 순서대로 반환
    answer = []

    for name in id_list:
        answer.append(mail[name])

    return answer