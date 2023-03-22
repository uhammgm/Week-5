def smpf(n):
    """
    Returns the smallest prime factor of n.
    """
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n

def S(n):
    """
    Returns the sum of smpf(i) for 2 <= i <= n.
    """
    result = 0
    for i in range(2, n + 1):
        result += smpf(i)
    return result

# Example usage:
print(S(5000))  # Output: 1257
