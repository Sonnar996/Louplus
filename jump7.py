#1~100 输出   不含7和7的倍数  不含7的数字
print("输出1-100，跳过7的倍数以及含7的数字")
num=0
while num<100:
    num=num+1
    if ((num%7 == 0)or(num%10 == 7)or(num//10 == 7)):
        print("jump",num)
    else:
        print(num)
