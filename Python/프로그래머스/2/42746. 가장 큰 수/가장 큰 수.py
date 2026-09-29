#순열을 사용하지 않고 numbers를 문자열로 바꾸고 그걸 정렬하는데 조건이 x를 세번 반복했을때 내림차순으로 정리 
def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x : x*4, reverse=True)
    
    if numbers[0] == "0":
        return "0"
    
    return ''.join(numbers)