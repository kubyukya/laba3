class FinanceCalculator:
    def __init__(self):
        self.expenses = []
        self.income = []

    def add_expense(self, amount: float, category: str) -> bool:
        """Add an expense transaction"""
        if amount <= 0:
            return False
        self.expenses.append({"amount": amount, "category": category})
        return True

    def add_income(self, amount: float, source: str) -> bool:
        """Add an income transaction"""
        if amount <= 0:
            return False
        self.income.append({"amount": amount, "source": source})
        return True

    def get_total_expenses(self) -> float:
        """Calculate total expenses"""
        return sum(transaction["amount"] for transaction in self.expenses)

    def get_total_income(self) -> float:
        """Calculate total income"""
        return sum(transaction["amount"] for transaction in self.income)

    def get_balance(self) -> float:
        """Calculate current balance"""
        return self.get_total_income() - self.get_total_expenses()

    def get_expenses_by_category(self) -> dict:
        """Get expenses grouped by category"""
        categories = {}
        for expense in self.expenses:
            category = expense["category"]
            if category not in categories:
                categories[category] = 0
            categories[category] += expense["amount"]
        return categories
