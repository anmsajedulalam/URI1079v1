
counter=int(input())
firstNumber=float(0)
secondNumber=float(0)
thirdNumber=float(0)

for i in range (1, counter+1, 1):
    firstNumber=float(input())
    secondNumber=float(input())
    thirdNumber=float(input())
    average=float((float(firstNumber*2)+float(secondNumber*3)+float(thirdNumber*5))/10)
    print("%.1f"%(average))

'''''
n=int(input())
for i in range(1, n +1):
    md1 = input().split()
    md2 = input().split()
    md3 = input().split()
    media1 = (float(md1[0])*2 + float(md1[1])*3+float(md1[2])*5)/10
    media2 = (float(md2[0])*2 + float(md2[1])*3+float(md2[2])*5)/10
    media3 = (float(md3[0])*2 + float(md3[1])*3+float(md3[2])*5)/10
    print('{:.1f}'.format(media1))
    print('{:.1f}'.format(media2))
    print('{:.1f}'.format(media3))
'''