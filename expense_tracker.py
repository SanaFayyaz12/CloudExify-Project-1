# expense_tracker.py
# CloudExify Python Internship — Month 1 Project 1
# Personal Expense Tracker (CLI)
#
# Your Name    : [Apna naam yahan likhein]
# Registration : CX-2026-XXXX

# ----------------------------------------------------
# Data storage
# ----------------------------------------------------
expenses = []       # List to store all expense dictionaries in memory
expense_id = 1       # Auto-incrementing ID for each new expense

CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Other"]


# ----------------------------------------------------
# Feature 1: Add a new expense
# ----------------------------------------------------
def add_expense():
    global expense_id
    print("\n--- ADD NEW EXPENSE ---")
    description = input("Description: ").strip()

    # Get amount with validation
    while True:
        try:
            amount = float(input("Amount (PKR): "))
            if amount <= 0:
                print("Amount must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    # Category selection
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Select category (1-5): "))
            if 1 <= choice <= 5:
                category = CATEGORIES[choice - 1]
                break
            print("Please select 1-5")
        except ValueError:
            print("Enter a number!")

    # Create expense record as dictionary
    expense = {
        "id": expense_id,
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense)
    expense_id += 1
    print(f"\n[+] Expense added! ID: {expense['id']}")


# ----------------------------------------------------
# Feature 2: View all expenses
# ----------------------------------------------------
def view_expenses():
    if not expenses:
        print("\nNo expenses yet. Add some first!")
        return

    print("\n--- ALL EXPENSES ---")
    print(f"{'ID':<5} {'Description':<20} {'Category':<12} {'Amount':>10}")
    print("-" * 50)

    total = 0
    for exp in expenses:
        print(f"{exp['id']:<5} "
              f"{exp['description']:<20} "
              f"{exp['category']:<12} "
              f"PKR {exp['amount']:>8.2f}")
        total += exp['amount']

    print("-" * 50)
    print(f"{'TOTAL:':<38} PKR {total:>8.2f}")


# ----------------------------------------------------
# Feature 3: Category-wise summary
# ----------------------------------------------------
def category_summary():
    if not expenses:
        print("\nNo expenses to summarize!")
        return

    summary = {}
    for exp in expenses:
        cat = exp['category']
        summary[cat] = summary.get(cat, 0) + exp['amount']

    print("\n--- CATEGORY SUMMARY ---")
    total = sum(exp['amount'] for exp in expenses)
    for category, amount in summary.items():
        percent = (amount / total) * 100
        print(f"{category:<12}: PKR {amount:>8.2f} ({percent:.1f}%)")


# ----------------------------------------------------
# Feature 4: Filter expenses by category
# ----------------------------------------------------
def filter_by_category():
    if not expenses:
        print("\nNo expenses yet!")
        return

    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")

    while True:
        try:
            choice = int(input("Select category to filter (1-5): "))
            if 1 <= choice <= 5:
                category = CATEGORIES[choice - 1]
                break
            print("Please select 1-5")
        except ValueError:
            print("Enter a number!")

    matches = [exp for exp in expenses if exp['category'] == category]

    if not matches:
        print(f"\nNo expenses found in category '{category}'.")
        return

    print(f"\n--- EXPENSES IN '{category.upper()}' ---")
    print(f"{'ID':<5} {'Description':<20} {'Amount':>10}")
    print("-" * 40)

    total = 0
    for exp in matches:
        print(f"{exp['id']:<5} {exp['description']:<20} PKR {exp['amount']:>8.2f}")
        total += exp['amount']

    print("-" * 40)
    print(f"Total for {category}: PKR {total:.2f}")


# ----------------------------------------------------
# Feature 5: Delete an expense by ID
# ----------------------------------------------------
def delete_expense():
    if not expenses:
        print("\nNo expenses to delete!")
        return

    view_expenses()

    try:
        target_id = int(input("\nEnter ID of expense to delete: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    # Find the expense with that ID
    target = None
    for exp in expenses:
        if exp['id'] == target_id:
            target = exp
            break

    if target is None:
        print(f"No expense found with ID {target_id}.")
        return

    confirm = input(f"Delete '{target['description']}' (PKR {target['amount']:.2f})? (y/n): ").strip().lower()
    if confirm == 'y':
        expenses.remove(target)
        print("[+] Expense deleted successfully!")
    else:
        print("Deletion cancelled.")


# ----------------------------------------------------
# Feature 6 & 7: Save / Load expenses from file
# ----------------------------------------------------
def save_expenses():
    with open("expenses.txt", "w") as f:
        for exp in expenses:
            line = f"{exp['id']},{exp['description']},{exp['amount']},{exp['category']}\n"
            f.write(line)
    print("[+] Expenses saved!")


def load_expenses():
    global expense_id
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    expense = {
                        "id": int(parts[0]),
                        "description": parts[1],
                        "amount": float(parts[2]),
                        "category": parts[3]
                    }
                    expenses.append(expense)
                    expense_id = int(parts[0]) + 1
    except FileNotFoundError:
        pass  # No file yet — that's fine, app starts fresh


# ----------------------------------------------------
# Menu and program entry point
# ----------------------------------------------------
def show_menu():
    print("\n" + "=" * 40)
    print("   CLOUDEXIFY EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Save Expenses")
    print("7. Save & Exit")
    print("=" * 40)


def main():
    print("Loading saved expenses...")
    load_expenses()
    print(f"Loaded {len(expenses)} expenses.")

    while True:
        show_menu()
        choice = input("Select option (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            save_expenses()
        elif choice == "7":
            save_expenses()
            print("\nGoodbye! Expenses saved.")
            break
        else:
            print("Invalid choice! Please enter 1-7.")


# Run the program
if __name__ == "__main__":
    main()
