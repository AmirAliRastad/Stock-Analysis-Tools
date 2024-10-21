expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})

def display_expenses():
    total = 0
    for expense in expenses:
        print(f"{expense['category']}: ${expense['amount']:.2f}")
        total += expense['amount']
    print(f"Total Expenses: ${total:.2f}")

def main():
    while True:
        action = input("'add' to add, 'view' to view, 'quit' to exit: ").strip().lower()
        if action == 'add': 
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                add_expense(amount, category)
            except ValueError:
                print("Numbers Only.")
        elif action == 'view': display_expenses()
        elif action == 'quit': break
        else: print("Sorry, try one of the directed options :)")

if __name__ == "__main__":
    main()
