def _earnings(expenses, income):
    # TODO: implement function along the given task
    pass

def return_on_investment(expenses: float, income: float, investment: float) -> float:
    # TODO: implement function along the given task
    pass    

def _test_return_on_investment() -> None:
    assert return_on_investment(100, 200, 1000) == 10
    assert return_on_investment(100, 200, 100) == 100
    assert return_on_investment(100, 200, 200) == 50
    assert return_on_investment(200, 140, 300) == -20
    print("All tests passed.")