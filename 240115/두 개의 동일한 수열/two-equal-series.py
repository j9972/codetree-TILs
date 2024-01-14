n = int(input())
arr = list(map(int,input().split()))
arr_list = list(map(int,input().split()))

arr.sort()
arr_list.sort()

if arr != arr_list:
    print('No')
else:
    print('Yes')

# flag = False
# for i in range(n):
#     if arr[i] != arr_list[i]:
#         flag = True

# if flag:
#     print('No')
# else:
#     print('Yes')