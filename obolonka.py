x = [6,2,3,1,10,4,5,4,8]
y = [4,4,3,1,3,5,2,10,7]
print(x)
print(y)
n = len(x)
t = [0] * n
xn = [0] * n
yn = [0] * n
m = 0
for i in range(1, n):
    if x[i] < x[m]:
        m = i
    else:
        if x[i] == x[m] and y[i] < y[m]:
            m = i
k = 0
x1 = x[m]
y1 = y[m]
xn[k] = x1
yn[k] = y1
print(xn)
print(yn)
p = True
while p:
    p =False
    for i in range(n):
        if t[i] == 0:
            x2 = x[i]
            y2 = y[i]
            pt = True
            for j in range(n):
                if (x[j] - x1)*(y2-y1) - (y[j]-y1)*(x2 - x1) <0:
                    pt = False
                if not (pt):
                    for jj in range(n):
                        if (x[jj] - x1)*(y2-y1) - (y[jj]-y1)*(x2 - x1) <0:
                            pt =False
            if pt:
                k +=1
                x1=x2
                y1=y2
                t[i] = k
                xn[k] = x1
                yn[k] = y1
                p = True
print('Координати точок опуклої оболонки:')
for i in range(k):
    print(xn[i], yn[i])
