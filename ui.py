import db
import datetime
from objects import Ticket

def display_menu():
    print("")
    print("Welcome to the Vecta Corp Help Desk Application (Admin)")
    print("")
    print("COMMAND MENU")
    print("-" * 100)
    print("view - View all open ticket")
    print("issue - View issue for ticket")
    print("add - Add an ticket")
    print("update - Update a ticket's status")
    print("exit - Exit the program")
    print("-" * 100)

def view_tickets():
    print("")
    print("VECTA CORP HELP DESK (CURRENT OPEN TICKETS)")
    print("-" * 100)
    line_format = "{:5s} {:15s} {:25s} {:15s} {:15s} {:15s} {:15s}"
    print(line_format.format("ID", "Name", "Email", "Date", "Employee", "Solution", "Status"))
    print("-" * 100)
    tickets = db.get_open_tickets()
    for ticket in tickets:
        print(line_format.format(str(ticket.ticketid), 
                                 ticket.customername, 
                                 ticket.customeremail,
                                 str(ticket.submitteddate),
                                 ticket.employee,
                                 ticket.solution,
                                 ticket.status))    
    print("-" * 100)

def view_ticket_issue():
    ticketid = int(input("Enter the ticket id:"))
    print("")
    print("VECTA CORP HELP DESK (CURRENT OPEN TICKETS)")
    print("-" * 100)
    issue = db.get_ticket_issue(ticketid)
    print(issue)
    print("-" * 100)

def add_ticket():
    print("Enter the details: ")
    customername = input("CustomerName: ")
    customeremail= input("CustomerEmail: ")
    submitteddate = datetime.date.today()
    line_format = "{:5s} {:10s} {:15s}"
    employees = db.get_employees()
    for employee in employees:
        print(line_format.format(str(employee[0]), employee[1], employee[2]))
        
    employee = int(input("EmployeeID: "))
    solution = int(input("SolutionId (1=vProspect, 2=vConvert, 3=vRetain): "))
    status = 1
    issue = input("Issue: ")

    ticket = Ticket(customername=customername,
                    customeremail=customeremail,
                    submittedddate=submitteddate,
                    employee=employee,
                    solution=solution,
                    status=status,
                    issue=issue)
    db.add_ticket(ticket)
    print("")
    print("The new ticket was added to the database successfully!")

def update_ticket(): 
    ticket_id = int(input("Enter the ticket id:"))
    choice = input("Are you sure you want to update this ticket? (y/n): ")
    if choice == "y":
        statusid = int(input("Enter the status  (1=Open, 2=In-Progess, 3=CLosed): "))
        db.update_ticket(statusid,ticket_id)
        print("The Ticket was successfully updated")
    else:
        print("The ticket was NOT updated.\n")
        
def main():
    db.connect() 
    while True:
        print("VECTA CORP HELP DESK ADMIN LOG IN")
        print("-" * 85)
        print("Hello ADMIN!!")
        print("Enter the username and password")
        username = input("Username: ")
        password = input("Password: ")
        if db.login(username, password):
            break
        else:
            print("\nYour credentials are invalid. Please try again.\n")
    display_menu()

    while True:
        command = input("Enter command: ")
        if command == "view":
            view_tickets()
        elif command == "issue":
            view_ticket_issue()
        elif command == "add":
            add_ticket()
        elif command == "update":
            update_ticket()
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
            display_menu()
    
    db.close()
    print("The program has been terminated!")

if __name__ == "__main__":
    main()