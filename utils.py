from datetime import datetime

def get_valid_amount():
    """Prompt user for a valid positive number."""
    while True:
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print(" Please enter a positive number.")

def get_valid_date():
    """Prompt for a date in DD-MM-YYYY format."""
    while True:
        date_str = input("Date (DD-MM-YYYY) or press Enter for today: ").strip()
        if date_str == "":
            return datetime.today().strftime("%d-%m-%Y")
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print(" Invalid date format. Use DD-MM-YYYY.")

def get_valid_category():
    """Prompt user to select a valid category."""
    categories = ["Food", "Travel", "Bills", "Shopping", "Other"]
    print("Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    while True:
        try:
            choice = int(input("Choose category (1-5): "))
            if 1 <= choice <= 5:
                return categories[choice - 1]
            else:
                print(" Enter a number between 1 and 5.")
        except ValueError:
            print(" Please enter a valid number.")