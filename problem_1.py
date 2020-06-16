# Project Euler Problem #1

# Solution
print(sum([i for i in range(3, 1000) if i % 3 == 0 or i % 5 == 0]))

# Expansion 1
N = 1000  # Can be any positive integer
def sumOfMult(base, max_n):
	max_mult = (max_n - 1) // base
	return(base * (max_mult * (max_mult + 1)) // 2)
print(sumOfMult(3, N) + sumOfMult(5, N) - sumOfMult(15, N))


# Expansion 2
arr = [3, 5]
N = 1000

# Find common multiples
def findCommonMults(array):
    mult_arr = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            mult_arr.append(array[i] * array[j])
    return mult_arr
mult_arr = findCommonMults(arr)

ans = sum([sumOfMult(i, N) for i in arr]) - sum([sumOfMult(j, N) for j in mult_arr])
print(ans)

