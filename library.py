import csv
BOOKS = "books.csv"
MEMBERS = "members.csv"
LOANS = "loans.csv"
def create_files():
    try:
        open(BOOKS, "r")
    except:
        with open(BOOKS, "w", newline="") as f:
            csv.writer(f).writerow(
                ["id", "title", "author", "category", "quantity", "available"]
            )
    try:
        open(MEMBERS, "r")
    except:
        with open(MEMBERS, "w", newline="") as f:
            csv.writer(f).writerow(
                ["id", "name", "email", "phone", "type", "status"]
            )
    try:
        open(LOANS, "r")
    except:
        with open(LOANS, "w", newline="") as f:
            csv.writer(f).writerow(
                ["loan_id", "member_id", "book_id", "issue_date",
                 "due_date", "return_date", "status"]
            )
def add_book():
    with open(BOOKS, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            input("Book ID: "),
            input("Title: "),
            input("Author: "),
            input("Category: "),
            input("Quantity: "),
            input("Quantity available: ")
        ])
    print("Book added.")
def view_books():
    with open(BOOKS, newline="") as f:
        for row in csv.reader(f):
            print(" | ".join(row))
def search_book():
    key = input("Enter title or author: ").lower()
    with open(BOOKS, newline="") as f:
        found = False
        for row in csv.DictReader(f):
            if key in row["title"].lower() or key in row["author"].lower():
                print(row)
                found = True
        if not found:
            print("Book not found.")
def add_member():
    with open(MEMBERS, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            input("Member ID: "),
            input("Name: "),
            input("Email: "),
            input("Phone: "),
            input("Membership type: "),
            "Active"
        ])
    print("Member added.")
def view_members():
    with open(MEMBERS, newline="") as f:
        for row in csv.reader(f):
            print(" | ".join(row))
def issue_book():
    member = input("Member ID: ")
    book = input("Book ID: ")
    issue = input("Issue date: ")
    due = input("Due date: ")
    with open(LOANS, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            input("Loan ID: "),
            member,
            book,
            issue,
            due,
            "",
            "Issued"
        ])
    print("Book issued.")
def return_book():
    loan_id = input("Loan ID: ")
    with open(LOANS, newline="") as f:
        loans = list(csv.DictReader(f))
    found = False
    for loan in loans:
        if loan["loan_id"] == loan_id:
            loan["return_date"] = input("Return date: ")
            loan["status"] = "Returned"
            found = True
    if found:
        with open(LOANS, "w", newline="") as f:
            fields = [
                "loan_id", "member_id", "book_id",
                "issue_date", "due_date",
                "return_date", "status"
            ]
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(loans)
        print("Book returned.")
    else:
        print("Loan not found.")
def view_loans():
    with open(LOANS, newline="") as f:
        for row in csv.reader(f):
            print(" | ".join(row))
def main():
    create_files()
    while True:
        print("\nLIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Add Member")
        print("5. View Members")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. View Loans")
        print("9. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            add_member()
        elif choice == "5":
            view_members()
        elif choice == "6":
            issue_book()
        elif choice == "7":
            return_book()
        elif choice == "8":
            view_loans()
        elif choice == "9":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")
main()
