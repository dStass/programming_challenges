def findSmallestDivisor(s, t):
    divisible = isDivisible(s, t)
    if not divisible:
        return -1
    
    for i in range(1, len(t) + 1):
        divisor = t[:i]
        if isDivisible(s, divisor):
            return len(divisor)

    return len(t)

def isDivisible(s, t):
    s_split = s.split(t)
    divisible = True
    if len(s_split) == 1:
        return False
    for each in s_split:
        if each != '':
            divisible = False
            break
    return divisible

s = 'rbrb'
t = 'rbrb'
print(findSmallestDivisor(s,t))