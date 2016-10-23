def lucas (n):
    if n == 0:
        return (2)
    elif n == 1:
        return (1)
    else:
        return(lucas(n-1)+lucas(n-2))
       
l = 30

n = lucas(l)

while n > 1:
    print (n)
    l = l - 1
    n = lucas(l)

print ("for")

L = [2,1]

n = 31

for i in range (1):
    m = (n-n)+2
    while m != n:
        l = L[m-1]
        print (l)
        r = L[m-2]
        print(r)
        lc = l + r
        L.append(lc)
        print(L)
        m = m + 1
