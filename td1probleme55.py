def miroir(n):
    A = str(n)
    B = ""
    for i in range(len(A)):
        B = B + A[-i-1]
    return int(B)
    
def operation(n):
    return n + miroir(n)

def testpalindrome(n):
    if n == miroir(n):
        return True
    else:
        return False

def euler55(n):
    c=0
    for i in range(n):
        j = 1
        A = operation(i)
        while not testpalindrome(A) and j <= 50:
            A = operation(A)
            j = j + 1
        if j == 51:
            c += 1
    return c

print(euler55(10000))

