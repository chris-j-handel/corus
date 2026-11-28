# Liouville's lead L(n) = sum of lambda(k), k <= n, and Mertens' lead M(n) = sum of mu(k),
# on surfaces 4^k: the largest |L| and |M| up to the surface, beside the side sqrt(surface).
N = 4**11
lam = [1]*(N+1); mu = [1]*(N+1); omega_parity = [0]*(N+1)
spf = list(range(N+1))
for i in range(2, int(N**0.5)+1):
    if spf[i] == i:
        for j in range(i*i, N+1, i):
            if spf[j] == j: spf[j] = i
lam[0] = 0; mu[0] = 0
for n in range(2, N+1):
    p = spf[n]; m = n // p
    lam[n] = -lam[m]
    mu[n] = 0 if m % p == 0 else -mu[m]
L = M = 0; maxL = maxM = 0; k = 1; side = 2
for n in range(1, N+1):
    L += lam[n]; M += mu[n]
    maxL = max(maxL, abs(L)); maxM = max(maxM, abs(M))
    if n == 4**k:
        print(f"surface {n:>9}  side {side:>5}  max|L| {maxL:>5} {'past side' if maxL > side else ''}  max|M| {maxM:>4} {'past side' if maxM > side else ''}")
        k += 1; side *= 2
