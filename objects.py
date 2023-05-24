class Ticket:
    def __init__(self, ticketid=0,customername=None,customeremail=None,submittedddate=None,employee=0,solution=0,status=0,issue=None):
        self.ticketid = ticketid
        self.customername= customername
        self.customeremail = customeremail
        self.submitteddate = submittedddate
        self.employee = employee
        self.solution = solution
        self.status = status
        self.issue = issue
        