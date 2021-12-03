"""
Name: Jeremy Miller
sales_force.py

Problem: This program encapsulates data for a salesperson

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""
from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        in_file = open(file_name, 'r')
        for line in in_file:
            data = line.replace(",", "").split()
            employee = SalesPerson(float(data[0]), data[1] + " " + data[2])
            sales = data[3:]
            count = 0
            while count < len(sales):
                employee.enter_sale(float(sales[i]))
                count += 1
            self.sales_people += [employee]

    def quota_report(self, quota):
        report = []
        for emp in self.sales_people:
            report.append([emp.get_id(), emp.get_name(), emp.total_sales(), emp.met_quota(quota)])
        return report

    def top_seller(self):
        sales = []
        for i in range(len(self.sales_people)):
            sales.append(self.sales_people[i].total_sales())
        highest_sales = max(sales)
        top_employee = []
        for i in range(len(self.sales_people)):
            if self.sales_people[i].total_sales() == highest_sales:
                top_employee.append(self.sales_people[i])
        return top_employee

    def individual_sales(self, employee_id):
        for sales_person in self.sales_people:
            if sales_person.get_id() == employee_id:
                return sales_person
