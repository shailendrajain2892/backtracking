def find_all_subsets(arr, n, count, subset, ans):
    if count == n:
        if subset not in ans:
            ans.append(subset[:])
        return 
    subset.append(arr[count])
    find_all_subsets(arr, n, count+1, subset, ans)
    subset.pop()
    find_all_subsets(arr, n, count+1, subset, ans)
    
    

def unique_subset(arr, n):
    subset = []
    superset = []
    arr.sort()
    find_all_subsets(arr, n, 0, subset, superset)
    superset.sort()
    print(superset)


unique_subset(['2','1','2'], 3)