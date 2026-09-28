from itertools import permutations

def solution(numbers):
    # 중복 제거용 set 사용
    made_numbers = set()
    
    for length in range(1, len(numbers)+1):
        for p in permutations(numbers, length):
            num = int(''.join(p))
            made_numbers.add(num)
    count = 0
    
    for num in made_numbers:
        
        if is_prime(num):
            count +=1
    return count

def is_prime(num):
    if num<2:
        return False
    
    i=2
    
    while i* i <= num:
        if num % i ==0:
            return False
        
        i +=1
    
    return True