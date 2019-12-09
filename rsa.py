def nod(m, n):
    return m if n == 0 else nod(n, m % n)

def phi(n):
    result = n
    i = 2
    while i*i <= n:
        if n % i == 0:
            while (n % i == 0):
                n /= i
            result -= result / i
        i += 1
    if n > 1:
        result -= result / n
    return result

def evkl(a,b,c):
    nodAB = nod(abs(a), abs(b))
    if c % nodAB:
        print("Impossible")
        return None
    else:
        a //= nodAB
        b //= nodAB
        c //= nodAB

        for k in range(abs(a)):
            if (c - b * k) % a == 0:
                y = k
                x = (c - b * y) // a
                return x
        else:
            print("Shit happens!")
            return None

# e = 3
# n = 9173503

e = int(input("e = "))
n = int(input("n = "))
print(evkl(e,-int(phi(n)),1))
