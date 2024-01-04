ppl = list(map(int,input().split()))

ppl.sort()

def check(arr):
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
        return True
    return False

if check(ppl):
    print(0)
else:
    print(max(0, ppl[2] - ppl[1] - 1, ppl[1] - ppl[0] - 1))