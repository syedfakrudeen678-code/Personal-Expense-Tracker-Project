import csv
from storage import load_expenses, save_expenses


def generate_id(expenses):
    """Generate a unique ID for a new expense."""
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1


def add_expense(amount, category, note, date):
    """Add a new expense entry."""
    expenses = load_expenses()
    expense = {
        "id": generate_id(expenses),
        "amount": float(amount),
        "category": category,
        "note": note.strip(),
        "date": date
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\n Expense added successfully with ID {expense['id']}!\n")


def view_expenses(expenses=None):
    """Display all expenses in a table format."""
    if expenses is None:
        expenses = load_expenses()
    if not expenses:
        print("\n  No expenses found.\n")
        return
    print("\n" + "=" * 65)
    print(f"{'ID':<5} {'Date':<12} {'Category':<12} {'Amount':>9}  {'Note'}")
    print("=" * 65)
    for e in expenses:
        print(f"{e['id']:<5} {e['date']:<12} {e['category']:<12} ${e['amount']:>8.2f}  {e['note']}")
    print("=" * 65 + "\n")


def filter_expenses(by, value):
    """Filter expenses by category, date, or month."""
    expenses = load_expenses()
    if by == "category":
        result = [e for e in expenses
                  if e["category"].lower() == value.lower()]
    elif by == "date":
        result = [e for e in expenses if e["date"] == value]
    elif by == "month":
        result = [e for e in expenses if e["date"].startswith(value)]
    else:
        print(" Invalid filter type.")
        return
    if not result:
        print(f"\n  No expenses found for {by}: {value}\n")
    else:
        view_expenses(result)


def total_summary():
    """Show total spent overall, by category, highest category."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses to summarize.\n")
        return

    total = sum(e["amount"] for e in expenses)

    # Calculate total per category
    by_category = {}
    for e in expenses:
        cat = e["category"]
        by_category[cat] = by_category.get(cat, 0) + e["amount"]

    highest = max(by_category, key=by_category.get)

    print("\n" + "=" * 40)
    print("          EXPENSE SUMMARY")
    print("=" * 40)
    print(f"  Total Spent Overall : ${total:.2f}")
    print("\n  By Category:")
    for cat, amt in sorted(by_category.items()):
        print(f"    {cat:<15} : ${amt:.2f}")
    print(f"\n   Highest Spending  : {highest} (${by_category[highest]:.2f})")
    print("=" * 40 + "\n")


def delete_expense(expense_id):
    """Delete an expense by its ID."""
    expenses = load_expenses()
    original_count = len(expenses)
    expenses = [e for e in expenses if e["id"] != expense_id]
    if len(expenses) == original_count:
        print(f"\n No expense found with ID {expense_id}.\n")
    else:
        save_expenses(expenses)
        print(f"\n  Expense ID {expense_id} deleted successfully.\n")


def export_to_csv():
    """Export all expenses to a CSV file."""
    expenses = load_expenses()
    if not expenses:
        print("\n  No expenses to export.\n")
        return
    with open("data/expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["id", "date", "category", "amount", "note"])
        writer.writeheader()
        writer.writerows(expenses)
    print("\n Expenses exported to data/expenses.csv successfully!\n")


def search_expenses(keyword):
    """Search expenses by keyword in note or category."""
    expenses = load_expenses()
    result = [e for e in expenses if
              keyword.lower() in e["note"].lower() or
              keyword.lower() in e["category"].lower()]
    if not result:
        print(f"\n  No results found for '{keyword}'\n")
    else:
        view_expenses(result)
