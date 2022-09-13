test_n = int(input())
test_score = []
max_score = 0
div = 0

test_score = list(map(int, input().split(" ")))

max_score = max(test_score)

for i in range(test_n):
    div = div + (test_score[i] / max_score) * 100


print(div/test_n)
