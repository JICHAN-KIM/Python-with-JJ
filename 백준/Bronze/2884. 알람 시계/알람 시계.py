h,m = map(int,input().split())
temp = h*60 + m
if temp >= 45:
    temp -= 45
else:
    temp += 24*60-45
print(int(temp/60), temp%60)
