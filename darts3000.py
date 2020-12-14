def maxSumMass(mass_point,K):
    N = len(mass_point)
    max_number = 0
    max_point = 0

    if mass_point[K] < 0:
        max_number = max(mass_point)

    for i in range(0,N):
        if (K >=  0) and (K >= i):
            max_point = 0
        else:
            max_point = max_point + mass_point[i]
        if max_point < 0:
            max_point = 0
        if max_number < max_point:
            max_number = max_point
    return max_number

def maxSumCurcle(mass_point,K):
    N = len(mass_point)
    max_sum_mass = maxSumMass(mass_point,K)
    max_wrap = 0
    for i in range(0,N):
        if (K >=0) and (K == i):
            max_wrap = 0
        else:
            max_wrap = max_wrap + mass_point[i]
            mass_point[i] = -mass_point[i]
    if K <= 0:
        max_wrap = max_wrap + maxSumMass(mass_point,K)
    else:
        max_wrap = max_wrap + max_sum_mass

    if max_wrap > max_sum_mass:
        return max_wrap
    else:
        return max_sum_mass

X = int(input())
for i in range(X):
    N,K = map(int, input().split())
    mass_point = [int(i) for i in (input().split())]
    print(maxSumCurcle(mass_point,K))