def solution(s):
    answer = ''
    s = s.split()
    
    for i in s:
        for j in range(len(i)):
            if j % 2 !=0 and j/2 != 0:
                answer = answer + i[j].lower()
            else :
                answer = answer + i[j].upper()
        if i != s[-1]:
            answer = answer+" "
        
    return answer
