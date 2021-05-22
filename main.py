import math


# довжина відразка
from site import venv


def L_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def L_3d(x1, y1, x2, y2, z1, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def znak(x, y, x1, y1, x2, y2):
    if (y2 - y1) * x + (x2 - x1) * y + (x1 * y2 - x2 * y1) > 0:
        return 1
    if (y2 - y1) * x + (x2 - x1) * y + (x1 * y2 - x2 * y1) < 0:
        return -1
    if (y2 - y1) * x + (x2 - x1) * y + (x1 * y2 - x2 * y1) == 0:
        return 0


def add_a_b(ax, ay, bx, by):
    return ax + bx, ay + by


def subt_a_b(ax, ay, bx, by):
    return ax - bx, ay - by


def mult_a_b(ax, ay, c):
    return ax * c, ay * c


def mod_a(ax, ay):
    return math.sqrt(ax ** 2 + ay ** 2)


def kor_mvect(x1, y1, z1, x2, y2, z2):
    return (y1 * z2 - z1 * y2, z1 * x2 - x1 - z2, x1 * y2 - y1 * x2)


def vect(x1, y1, z1, x2, y2, z2):
    return (x2 - x1, y2 - y1, z2 - z1)

def L_vect(x1, y1, z1):
    return math.sqrt((x1) ** 2 + (y1) ** 2 + (z1) ** 2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    A = (0, 0)
    B = (0, 5)
    C = (9, 0)
    AB = L_2d(*A, *B)
    AC = L_2d(*A, *C)
    BC = L_2d(*B, *C)
    print(AB, AC, BC)
    p = (AB + AC + BC) / 2
    s1 = (AB * AC) / 2
    s2 = math.sqrt(p * (p - AB) * (p - AC) * (p - BC))
    print(s1, s2)
    vAB = vect(*A,0,*B,0)
    vAC = vect(*A, 0, *C, 0)
    print(vAB)
    print(vAC)
    cmvect = kor_mvect(*vAC, *vAB)
    print(cmvect)
    print(L_vect(*cmvect)/2)
