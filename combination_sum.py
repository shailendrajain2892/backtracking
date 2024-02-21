

def combination_sum(idx, target_sum, cmb, numbers, N, list_of_comb):
    if idx == N: 
        if target_sum == 0:
            print(cmb)
            return 
        return
    elif target_sum == 0:
        list_of_cmb.append(cmb[:])
        return 
    if target_sum >= numbers[idx]:
        cmb.append(numbers[idx])
        combination_sum(idx, target_sum-numbers[idx], cmb, numbers, N, list_of_cmb)
        cmb.remove(numbers[idx])
    combination_sum(idx+1, target_sum, cmb, numbers, N, list_of_cmb)

cmb = []
list_of_cmb=[]
a = [7, 2, 6, 5]
a.sort()
combination_sum(0, 16, cmb, a, 4,list_of_cmb)
print(list_of_cmb)
