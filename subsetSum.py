def subsetSum(numbers, target_sum, i=0):
    if i == len(numbers):
        return 1 if target_sum == 0 else 0
    return subsetSum(numbers, target_sum, i+1)+subsetSum(numbers, target_sum-numbers[i], i+1)

print(subsetSum([20, 10, 15], 45))
