def _earnings(expenses: float, income: float) -> float:
    """Returns the earnings."""
    return income - expenses

def return_on_investment(expenses: float, income: float, investment: float) -> float:
    """Returns the return on investment."""
    earnings = _earnings(expenses, income)
    roi = earnings / investment * 100
    print(f'Your return on investment is {roi:.2f}%.')
    return roi

def _test_return_on_investment() -> None:
    assert return_on_investment(100, 200, 1000) == 10
    assert return_on_investment(100, 200, 100) == 100
    assert return_on_investment(100, 200, 200) == 50
    assert return_on_investment(200, 140, 300) == -20
