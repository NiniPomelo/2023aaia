a = 120
# 1 2 3 4 5 6 10 12 15 ... for迴圈
ans = 0
for i in range(1, a+1): #包含1...a本身
  if a%i==0:
    print( i, end=' ')
    ans += 1 # 迴圈裡面,ans增加
print('有脊整除? ', ans) # 迴圈後面,把ans拿來用