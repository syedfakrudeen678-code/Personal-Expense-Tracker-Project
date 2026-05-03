import json
import os

DATA_FILE = "data/expenses.json"

def load_expenses():
    """Load expenses from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    """Save expenses to JSON file."""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)