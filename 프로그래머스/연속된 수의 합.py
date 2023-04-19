def solution(num, total):
    answer = []
    
    var = sum(range(num+1))
    differ = total-var

    start = differ//num
    answer = [i+1+start for i in range(num)]

    return answer
