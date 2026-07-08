# Personal Expense Tracker (CLI)

**CloudExify Python Internship 2026 — Month 1, Project 1**

**Name:** Sana Fayyaz
**Registration No:** CX-INT-2026-DS-0120

## 📌 Description
A command-line Python application to track daily personal expenses. Users can add
expenses by category, view all expenses in a formatted table, see a category-wise
spending summary, filter expenses by category, delete expenses, and save/load data
from a text file so nothing is lost between sessions.

## ▶️ How to Run
1. Make sure Python 3 is installed.
2. Open a terminal in this project folder.
3. Run:
   ```
   python expense_tracker.py
   ```
4. Follow the on-screen menu (options 1–7).

## ✅ Features Implemented
- Add new expense (description, amount, category) with input validation
- View all expenses in a clean formatted table with total
- Category-wise summary with percentage breakdown
- Filter expenses by category
- Delete an expense by ID (with confirmation)
- Save expenses to `expenses.txt`
- Auto-load saved expenses on startup
- Menu-driven interface with error handling for invalid input

## 🗂️ File Structure
```
expense_tracker/
├── expense_tracker.py   # Main application
├── expenses.txt         # Data storage (auto-created on save)
├── README.md            # This file
└── screenshots/         # Screenshots of the running app
```

## 📸 Screenshots
See the `screenshots/` folder for:
- Main menu
- Expense list with multiple entries
