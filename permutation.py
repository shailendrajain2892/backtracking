def isSafe(s, fi, i, n):
    if fi != 0 and s[fi-1] == 'A' and s[fi] == 'B':
        print(f"find ")
        return False
    elif n == fi+1 and ((s[i]=='A' and s[fi] == 'B') or (s[i] == 'A' and s[n] == 'B')):
        return False
    return True
def permutation(s, fi):
    # print(f"Calling for fixed index : {fi} with string: {s} ")
    if fi == len(s)-1:
        print(s)
        return 
    
    for i in range(fi, len(s)):
        s[i], s[fi] = s[fi], s[i]
        permutation(s, fi+1)
        s[i], s[fi] = s[fi], s[i]

permutation(['A', 'B', 'C', 'D'], 0)
    
