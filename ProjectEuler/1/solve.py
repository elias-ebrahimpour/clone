def multiples_to_3_and_5(n: int) -> int:
    """
    Given a number n, return the sum of all multiples of 3 or 5 below n.
    """
    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)


print(multiples_to_3_and_5(1000)) # 233168