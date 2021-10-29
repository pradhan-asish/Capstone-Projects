class BudgetList():
    def __init__(self,budget):
        self.budget = budget
        self.sum_expenses = 0
        self.expenses = []
        self.sum_overages = 0
        self.overages = []
    def append(self,item):
        if self.sum_expenses + item < self.budget :
            self.sum_expenses = self.sum_expenses + item
            self.expenses.append(item)
        else :
            
