def fibonnaci(n):

    if n <=  1:
        return n
    
    return fibonnaci(n - 1) + fibonnaci(n - 2)

def gcd(a, b):

    if b != 0:
        return gcd( b, a % b)
    else:
        return a

def compareTos(s1, s2):

    len_1 = len(s1)
    len_2 = len(s2)

    if len_1 < len_2:
        length = len_2
    else:
        length = len_2
    
    if length == 0 & len_1 > 0:
        return -1
    elif length == 0 & len_2 > 0:
        return 1

    for i in range(length):

        a1 = ord(s1[i])
        a2 = ord(s2[i])

        if a1 == a2:
            return compareTos(s1[1:len_1], s2[1:len_2])
        else:
            return a1 - a2
    return 0


if __name__ == "__main__":
    fib = fibonnaci(8)
    print(fib)

    k = gcd(12, 22)
    print(k)

    a = compareTos("John", "Chris")
    print(a)
    
    b = compareTos("Anthony", "Will")
    print(b)

    c = compareTos("Sam", "Lander")
    print(c)

    d = compareTos("", "")
    print(d)





