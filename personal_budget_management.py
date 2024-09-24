# question 1 task 1

class BudgetCategory:

    def __init__(self, category, budget):
        self.__category = category
        self.__budget = budget
        self.__expenses = []

    # question 1 task 2

    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        if not isinstance(category, str):
            raise ValueError("Input entered was not a valid string.")
        self.__category = category

    def get_budget(self):
        return self.__budget
    
    def set_budget(self, total):
        if not isinstance(total, (int, float)) or total <0:
            raise ValueError("You cannot have a negative budget.")
        self.__budget = total

    # question 1 task 3

    def add_expense(self, cost):
        if not isinstance(cost, (int, float) or cost < 0):
            raise ValueError("The cost of the expense cannot be less than 0.")
        if cost > self.__budget:
            raise ValueError("The cost of this expense is greater than the set budget.")
        self.__expenses.append(cost)

    def get_total_expenses(self):
        return sum(self.__expenses)
    

    # question 1 task 4 & 3
    
    def display_summary(self):
        print(f"Category: {self.__category}")
        print(f"Starting Budget: {self.__budget}")
        print(f"Money left in budget after expenses: {self.__budget - sum(self.__expenses)}")

if __name__ == "__main__":
    total_category = BudgetCategory("Total monthly income", 2376)

    food_category = BudgetCategory("Groceries", 400)
    food_category.add_expense(65)
    food_category.add_expense(70)
    food_category.add_expense(45)
    food_category.display_summary()

    gas_category = BudgetCategory("Gas", 120)
    gas_category.add_expense(45)
    gas_category.display_summary()

    total_category.add_expense(875)
    total_category.add_expense(345)
    total_category.add_expense(370)
    total_category.add_expense(60)
    total_category.add_expense(67)

    total_category.display_summary()
