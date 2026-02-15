def factorial_digits(n):
    fact = 1

    # Calculate factorial
    for i in range(1, n + 1):
        fact *= i

    # Convert factorial to list of digits
    return [int(d) for d in str(fact)]
