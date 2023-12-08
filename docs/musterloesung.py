def _order(x: float, y: float) -> list[float]:
    """Returns a list of two numbers in descending order."""
    if x >= y:
        return [x, y]
    else:
        return [y, x]
    
def difference(x: float, y: float) -> float:
    """Returns the positive difference of two numbers."""
    input = _order(x, y)
    x = input[0]
    y = input[1]
    return x - y

def _test_difference() -> None:
    assert difference(3, 2) == 1
    assert difference(2, 3) == 1
    assert difference(2, 2) == 0
    print("All tests passed.")