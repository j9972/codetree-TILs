ppl = list(map(int,input().split()))

ppl.sort()

# 전부 연속
if ppl[1] - ppl[0] == ppl[2] - ppl[1] == 1:
    print(0)
# 2개의 숫자 차이가 2인경우
elif ppl[0] + 2 == ppl[1] or ppl[1] + 2 == ppl[2]:
    print(1)
else:
    print(2)