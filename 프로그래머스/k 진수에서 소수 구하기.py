def solution(n, k):
    rev_base = ''

    while n:
        rev_base = str(n%k)+rev_base
        n=n//k
        
    rev_base=rev_base.split("0") 
    
    count=0
    for i in rev_base:
        if len(i)==0:   
            continue
        if int(i)<2:
            continue
        sosu=True
        for j in range(2,int(int(j)**0.5)+1):
            if int(i)%j==0:
                prime=False
                break
        if prime:
            count+=1
            
    return count
