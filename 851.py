n = int(input())
p1x, p1y = list(map(int, input().split()))
p3x, p3y = list(map(int, input().split()))
s = 0
for i in range(n - 2):
    p2x = p3x
    p2y = p3y
    p3x, p3y = list(map(int, input().split()))
    s += (p3x - p1x) * (p2y - p1y) - (p2x - p1x) * (p3y - p1y)
print('{0:.1f}'.format(abs(s / 2)))
