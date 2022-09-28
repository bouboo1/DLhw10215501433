def sqrt1():
    c=2
    i=0
    g=0
    for j in range (0,c+1):
        if (j*j>c and g==0):#找到一个j,平方大于0但是(j-1)小于0
            g=j-1
    while(abs(g*g-c)>0.0001):
        g=g+0.00001
        i=i+1
    print("%.5f" %g)#.3f的意思是保留小数点后3位进行输出，同时也是一个占位符，把后面%g代表的值在这个位置输出
sqrt1()

def sqrt2():
    i=0
    c=2
    max=c
    min=0
    g=(max+min)/2
    while(abs(g*g-c)>0.00000000000001):
        if(g*g<c):
            min=g
        else:
            max=g
        g=(max+min)/2
        i+=1
    print("%.13f" % g)
sqrt2()

def sqrt3():
    c=2
    g=c/2
    i=0
    while(abs(g*g-c)>0.00000000000001):
        g=(g+c/g)/2
        i+=1
    print("%.13f" % g)
sqrt3()