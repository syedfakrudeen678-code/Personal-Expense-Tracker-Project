from expenses import (add_expense, view_expenses, filter_expenses,
                      total_summary, delete_expense,
                      export_to_csv, search_expenses)
from utils import get_valid_amount, get_valid_date, get_valid_category


def print_menu():
    """Display the main menu."""
    print("\n" + "=" * 40)
    print("       PERSONAL EXPENSE TRACKER")
    print("=" * 40)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Filter Expenses")
    print("  4. Total Summary")
    print("  5. Delete Expense")
    print("  6. Search Expenses")
    print("  7. Export to CSV")
    print("  0. Exit")
    print("=" * 40)


def main():
    """Main menu loop."""
    print("\n Welcome to your Personal Expense Tracker!")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        #  1. Add Expense 
        if choice == "1":
            print("\n── Add New Expense ──")
            amount = get_valid_amount()
            category = get_valid_category()
            note = input("Note/Description: ")
            date = get_valid_date()
            add_expense(amount, category, note, date)

        #  2. View All 
        elif choice == "2":
            view_expenses()

        #  3. Filter 
        elif choice == "3":
            print("\n── Filter Expenses ──")
            print("  1. By Category")
            print("  2. By Date")
            print("  3. By Month")
            f_choice = input("Choose filter type: ").strip()

            if f_choice == "1":
                val = input("Enter category: ")
                filter_expenses("category", val)
            elif f_choice == "2":
                val = input("Enter date (YYYY-MM-DD): ")
                filter_expenses("date", val)
            elif f_choice == "3":
                val = input("Enter month (YYYY-MM): ")
                filter_expenses("month", val)
            else:
                print(" Invalid choice.")

        #  4. Summary 
        elif choice == "4":
            total_summary()

        #  5. Delete 
        elif choice == "5":
            view_expenses()
            try:
                exp_id = int(input("Enter expense ID to delete: "))
                delete_expense(exp_id)
            except ValueError:
                print(" Please enter a valid numeric ID.")

        #  6. Search 
        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            search_expenses(keyword)

        #  7. Export CSV 
        elif choice == "7":
            export_to_csv()

        #  0. Exit 
        elif choice == "0":
            print("\n Goodbye! Keep tracking your expenses!\n")
            break

        else:
            print(" Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    main()
