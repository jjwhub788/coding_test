#N/2개를 뽑았을때 그 안에 몇개의 종류가 있는지 그 종류의 max 값 구하기
#key : 뽑았을때 그 안에 있는 number value: 개수
def solution(nums):
    numbers = len(nums) //2
    new = len(set(nums))
    
    answer = min(numbers, new)
    
    return answer