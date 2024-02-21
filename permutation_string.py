# naive approach
def permutation_of_string_except(s, j=0):
    if j == len(s):
        print(s, end=" ")
        return 
    for idx in range(j, len(s)):
        s[idx], s[j]  = s[j], s[idx]
        permutation_of_string_except(s, j+1)
        s[idx], s[j]  = s[j], s[idx]

permutation_of_string_except(['A', 'B', 'C'])