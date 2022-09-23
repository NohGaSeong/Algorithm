n = int(input())

for i in range(n):
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    count = 0
    for score in nums[1:]:
        if score > avg:
            count += 1  
    rating = count/num[0] *100
    print(f'{rating:.3f}%')
