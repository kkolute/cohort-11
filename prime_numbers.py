
def prime_numbers(end):
    out = list()

    sieve = [True] * (end + 1)
    for p in range(2, end + 1):
        if (sieve[p]):
            out.append(p)
            for i in range(p, end + 1, p):
                sieve[i] = False
    return out
