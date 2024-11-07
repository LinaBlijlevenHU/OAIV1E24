def reeks_van_fibonacci(n) -> list:
    """
    Bepaal de eerste n getallen van de fibonacci-reeks

    :param  n:      Aantal getallen
    :return list:   Reeks van fibonacci van lengte n
    """
    fib = [0, 1]

    for _ in range(n - 2):
        previous, previouser = fib[-1], fib[-2]
        fib.append(previous + previouser)

    return fib

lengte = 1000
reeks = reeks_van_fibonacci(lengte)
print(f"De eerste {lengte} getallen van de reeks van Fibonacci: \n"
      f"{reeks}")