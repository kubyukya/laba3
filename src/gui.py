import tkinter as tk
from tkinter import ttk
from calculator import FinanceCalculator


class FinanceCalculatorGUI:
    def __init__(self, root):
        self.calculator = FinanceCalculator()
        self.root = root
        self.root.title("Personal Finance Calculator")

        # Create tabs
        self.tab_control = ttk.Notebook(root)
        self.expense_tab = ttk.Frame(self.tab_control)
        self.income_tab = ttk.Frame(self.tab_control)
        self.summary_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.expense_tab, text='Expenses')
        self.tab_control.add(self.income_tab, text='Income')
        self.tab_control.add(self.summary_tab, text='Summary')
        self.tab_control.pack(expand=1, fill="both")

        self._setup_expense_tab()
        self._setup_income_tab()
        self._setup_summary_tab()

    def _setup_expense_tab(self):
        # Expense inputs
        ttk.Label(self.expense_tab, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.expense_amount = ttk.Entry(self.expense_tab)
        self.expense_amount.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.expense_tab, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.expense_category = ttk.Entry(self.expense_tab)
        self.expense_category.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.expense_tab, text="Add Expense",
                   command=self._add_expense).grid(row=2, column=0, columnspan=2, pady=10)

    def _setup_income_tab(self):
        # Income inputs
        ttk.Label(self.income_tab, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.income_amount = ttk.Entry(self.income_tab)
        self.income_amount.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.income_tab, text="Source:").grid(row=1, column=0, padx=5, pady=5)
        self.income_source = ttk.Entry(self.income_tab)
        self.income_source.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.income_tab, text="Add Income",
                   command=self._add_income).grid(row=2, column=0, columnspan=2, pady=10)

    def _setup_summary_tab(self):
        self.summary_text = tk.Text(self.summary_tab, height=10, width=40)
        self.summary_text.pack(padx=10, pady=10)

        ttk.Button(self.summary_tab, text="Update Summary",
                   command=self._update_summary).pack(pady=5)

    def _add_expense(self):
        try:
            amount = float(self.expense_amount.get())
            category = self.expense_category.get()
            if self.calculator.add_expense(amount, category):
                self.expense_amount.delete(0, tk.END)
                self.expense_category.delete(0, tk.END)
                self._update_summary()
        except ValueError:
            pass

    def _add_income(self):
        try:
            amount = float(self.income_amount.get())
            source = self.income_source.get()
            if self.calculator.add_income(amount, source):
                self.income_amount.delete(0, tk.END)
                self.income_source.delete(0, tk.END)
                self._update_summary()
        except ValueError:
            pass

    def _update_summary(self):
        self.summary_text.delete(1.0, tk.END)
        summary = f"Total Income: ${self.calculator.get_total_income():.2f}\n"
        summary += f"Total Expenses: ${self.calculator.get_total_expenses():.2f}\n"
        summary += f"Current Balance: ${self.calculator.get_balance():.2f}\n\n"

        summary += "Expenses by Category:\n"
        for category, amount in self.calculator.get_expenses_by_category().items():
            summary += f"{category}: ${amount:.2f}\n"

        self.summary_text.insert(1.0, summary)


