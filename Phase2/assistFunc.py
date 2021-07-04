#Finds 2-S compliment of given input
def twoS(s):
    f = ""
    f = ["0" if s[i] == '1' else "1" for i in range(len(s))]

    i = -1
    while (f[i] == '1' and abs(i) <= len(f)):
        f[i] = "0"
        i -= 1
    if (abs(i) != len(f)):
        f[i] = "1"
    f = "".join(f)
    return f

#Converts input binary list to decimal
def two2dec(s):
    flag = "".join(s)
    if flag[0] == '1':
        return -1 * (int(''.join('1' if x == '0' else '0' for x in flag), 2) + 1)
    else:
        return int(flag, 2)


#Converts input decimal to binary list
def dec2two(n):
    s = bin(int(n)).replace("0b", "").zfill(32)
    s = s[-32:]
    if (n >= 0):
        return list(s)
    else:
        return list(twoS(s))