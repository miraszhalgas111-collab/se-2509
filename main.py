# 1
def f1(n):
    if n==0: return
    f1(n-1)
    print(n,end=" ")

# 2
def f2(n):
    if n==0: return
    print(n,end=" ")
    f2(n-1)

# 3
def f3(n):
    if n==0: return 0
    return n+f3(n-1)

# 4
def f4(n):
    if n<=1: return 1
    return n*f4(n-1)

# 5
def f5(a,b):
    if b==0: return 1
    return a*f5(a,b-1)

# 6
def f6(n):
    if n==0: return 0
    return n%10+f6(n//10)

# 7
def f7(n):
    if n==0: return 0
    return 1+f7(n//10)

# 8
def f8(n,r=0):
    if n==0: return r
    return f8(n//10,r*10+n%10)

# 9
def f9(n):
    if n<=1: return n
    return f9(n-1)+f9(n-2)

# 10
def f10(s):
    if len(s)<=1: return True
    if s[0]!=s[-1]: return False
    return f10(s[1:-1])

# 11
def f11(a,n):
    if n==0: return 0
    return a[n-1]+f11(a,n-1)

# 12
def f12(a,n):
    if n==1: return a[0]
    return max(a[n-1],f12(a,n-1))

# 13
def f13(a,n,t):
    if n==0: return 0
    return (1 if a[n-1]==t else 0)+f13(a,n-1,t)

# 14
def f14(a,n,t):
    if n==0: return False
    if a[n-1]==t: return True
    return f14(a,n-1,t)

# 15
def f15(a,n):
    if n==1: return True
    if a[n-1]<a[n-2]: return False
    return f15(a,n-1)

# 16
def f16(a,l,r,t):
    if l>r: return -1
    m=(l+r)//2
    if a[m]==t: return m
    if a[m]>t: return f16(a,l,m-1,t)
    return f16(a,m+1,r,t)