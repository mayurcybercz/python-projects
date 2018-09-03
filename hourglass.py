arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
n,r=0,0
record=[]
for n in range(4):
    for r in range(4):
        sum=arr[n][r]+arr[n][r+1]+arr[n][r+2]+arr[n+1][r+1]+arr[n+2][r]+arr[n+2][r+1]+arr[n+2][r+2]
        record.append(int(sum))
print(max(record))
