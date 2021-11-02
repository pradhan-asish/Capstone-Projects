import Expense
import matplotlib.pyplot as plt
import timeit
def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
#    if (divided_for_loop != divided_set_comp) :
#        print('Sets are NOT equal by == test')
    for a,b in zip(divided_for_loop,divided_set_comp):
        if ((a.issubset(b) or b.issubset(a))):
            print('Sets are not equal by subset test')

    stmt = "expenses.categorize_for_loop()"
    setup = '''
import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')'''

    print(timeit.timeit(stmt = stmt,setup = setup ,number=10000))
    stmt = "expenses.categorize_set_comprehension()"

    setup = '''
import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')'''

    print(timeit.timeit(stmt = stmt,setup = setup ,number=10000))

    fig,ax = plt.subplots()
    labels = ['Necessary','Food','Unnecessary']
    divided_expenses_sum = []
    for category_exps in divided_set_comp:
        divided_expenses_sum.append(sum([x.amount for x in category_exps]))


if __name__ == "__main__":
    main()
