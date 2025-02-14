n = 1000
cubes = {x: x**3 for x in range(1, n+1)}

res_combs = []
for a in range(1, n):
    for b in range(a, n):
        sum_cubes = cubes[a] + cubes[b]
        if sum_cubes in cubes.values():
            c = int(sum_cubes**(1/3) + 0.5)  # Approximate cube root and round
            if c**3 == sum_cubes and c > b and c <= n:
                res_combs.append((a, b, c))

print("The triplets are:", res_combs if res_combs else "None")
