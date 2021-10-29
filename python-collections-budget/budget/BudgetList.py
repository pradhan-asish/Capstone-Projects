import Expense

class BudgetList():
    def __init__(self,budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
        print('Budget:',budget)
    def append(self,item):
        print('1')
        if self.sum_expenses + item < self.budget :
            self.sum_expenses = self.sum_expenses + item
            self.expenses.append(item)
        else :
            self.overages.append(item)
            self.sum_overages = self.sum_overages + item
    def __len__(self):
        return length(self.expenses)+length(self.overages)

def main():
    myBudgetList = BudgetList(1200)
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    for expense in expenses.list:
        myBudgetList.append(expense.amount)
        print('The count of all expenses: ', myBudgetList.__len__())
