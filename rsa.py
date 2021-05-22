from math import sqrt


# IF U ARE READING THIS CODE, PLEASE, START DO IT AFTER THIS ALL FUNCTIONS, U WILL NOT UNDERSTAND THEM, BC ALL OF IT - MATH FORMULAS


def phi(a: int, b: int) -> int:
    return (a-1) * (b-1)

def encode(n: int,e: int, N: int) -> int:
    return (n ** e) % N

def d_search(ph: int, f1: int, f2: int, e:int, q: int = 1) -> int:
    a1,b1 = f1,f2
    a2,b2 = e, q
    if a2 < 0:
        while a2 <= 0: a2 += ph
    if b2 < 0:
        while b2 <= 0: b2 += ph
    if a2 == 1: return b2
    if b2 == 1: return a2
    else:
        return d_search(ph, a2, b2, a1 % a2, b1 - a1 // a2 * b2)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    i = 2
    while i <= limit:
        if n % i == 0:
            return False
        i += 1
    return True


def decode(n: int,d: int, N: int) -> int:
    return (n ** d) % N

def gcd(a: int,b: int) -> int:
        if b == 0:
            return a
        else:
            return gcd(b,a%b)

def gcd_exp(a: int,b: int) -> int:
    if b == 0:
        return a,1,0
    else:
        d,x1,y1 = gcd_exp(b,a%b)
        x = y1
        y = x1-(a//b*y1)
        return d,x,y


print("Please,enter prime numbers lower\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\nFor example( 89,107 (e = 3) | 61,53 (e = 17) )")
a, b = map(int,input("Enter two prime numbers: ").split())
while is_prime(a) != True and is_prime(b) != True:
    print("Please,enter prime numbers lower\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    a, b = map(int,input("Enter two prime numbers: ").split())
N = a * b
F = phi(a,b)

global e
print(f"Now u should enter exponent that will be smaller then Phi({N}) - {F} and bigger en 1, its need to be mutually simple with N too\n1 < e < {F}\nGCD(a,F) must be 1")
e = int(input("Enter right exponent: \n"))
while (not 1 < e < F) and gcd(e,F) == 1:

    if gcd(a,F) != 0 and e < 1 or e > F:
        print("Are u kidding?")
    elif e < 1 or e > F:
        print(f"{e} isn`t fulfills the condition 1 < e < Phi(N)")
    elif gcd(a,F) != 0:
        print(f"U are wrong. GCD(a,F) == {gcd(a,F)}")
    e = int(input("Enter right exponent: \n"))


d = d_search(F,F,F,e)

public_key = (e,N)
private_key = (d,N)

text = int(input("Message u wanna encode: "))

print(f"Encoded message by key {public_key}: {encode(text,e,N)}")

print(f"Decoded message by {private_key}: {decode(encode(text,e,N),d,N)}")








