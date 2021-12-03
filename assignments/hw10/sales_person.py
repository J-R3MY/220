"""
Name: Jeremy Miller
sales_person.py

Problem: This program encapsulates data for a salesperson

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.name = name
        self.employee_id = employee_id
        self.sales = []

    def get_id(self):
        # returns the employee's id
        return self.employee_id

    def get_name(self):
        # returns the employee's name
        return self.name

    def set_name(self, name):
        # sets employee's name
        self.name = name

    def enter_sale(self, sale):
        # adds the value of a sale to the sales list
        self.sales.append(sale)

    def total_sales(self):
        # returns the sum of the sales person's sales
        total = sum(self.sales)
        return total

    def get_sales(self):
        # returns the list of sales
        return self.sales

    def met_quota(self, quota):
        # determines if employee met quota
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        # compares employee object to another employee object
        if other.total_sales() > self.total_sales():
            return -1
        if other.total_sales() < self.total_sales():
            return 1
        if other.total_sales() == self.total_sales():
            return 0

    def __str__(self):
        return "{0}-{1}:{2}".format(self.employee_id, self.name, self.total_sales())
