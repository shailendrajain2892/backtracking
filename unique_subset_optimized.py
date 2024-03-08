
# Helper function to find all unique subsets
def findSubsets(v, idx, subset, result):
   
    # If the current subset is not empty insert it into
    # the result
    if (len(subset) != 0):
        if (subset not in result):
            result.append(subset[:])
 
    # Iterate over every element in the array
    for j in range(idx, len(v)):
       
        # Pick the element and move ahead
        subset.append(v[j])
        findSubsets(v, j + 1, subset, result)
 
        # Backtrack to drop the element
        subset.pop()
 
# Function to return all unique subsets
def solve(v):
   
    # To store the resulting subsets.
    result = []
    subset = []
 
    # Helper function call
    findSubsets(v, 0, subset, result)
 
    res = []
    for i in range(len(result)):
        res.append(list(result[i]))
 
    return res

solve([1, 2, 2])