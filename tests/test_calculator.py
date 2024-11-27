from src.calculator import FinanceCalculator


def test_add_expense():
    calc = FinanceCalculator()
    assert calc.add_expense(100.0, "Food") == True
    assert calc.add_expense("b", "Invalid") == False
    assert len(calc.expenses) == 1
    assert calc.expenses[0]["amount"] == 100.0
    assert calc.expenses[0]["category"] == "Food"

def test_add_income():
    calc = FinanceCalculator()
    assert calc.add_income(1000.0, "Salary") == True
    assert calc.add_income(-500.0, "Invalid") == False
    assert len(calc.income) == 1
    assert calc.income[0]["amount"] == 1000.0
    assert calc.income[0]["source"] == "Salary"

def test_get_total_expenses():
    calc = FinanceCalculator()
    calc.add_expense(100.0, "Food")
    calc.add_expense(50.0, "Transport")
    assert calc.get_total_expenses() == 150.0

def test_get_total_income():
    calc = FinanceCalculator()
    calc.add_income(1000.0, "Salary")
    calc.add_income(500.0, "Freelance")
    assert calc.get_total_income() == 1500.0

def test_get_balance():
    calc = FinanceCalculator()
    calc.add_income(1000.0, "Salary")
    calc.add_expense(600.0, "Rent")
    calc.add_expense(200.0, "Food")
    assert calc.get_balance() == 200.0

def test_get_expenses_by_category():
    calc = FinanceCalculator()
    calc.add_expense(100.0, "Food")
    calc.add_expense(50.0, "Food")
    calc.add_expense(200.0, "Rent")
    categories = calc.get_expenses_by_category()
    assert categories["Food"] == 150.0
    assert categories["Rent"] == 200.0
