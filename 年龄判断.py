age = int(input("请输入您的年龄>>>"))

if age < 18 :
    print('你还未成年，请在家长的陪同下观看！')
elif age < 100:
     print('您已成年，可以自由观看')
     print('但也要适当休息，祝您身体健康')
else :
    print('墓前凉好')
