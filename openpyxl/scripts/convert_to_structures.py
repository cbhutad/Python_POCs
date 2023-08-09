import json
from openpyxl import load_workbook
from excel_headers import EEID, FULLNAME, JOB_TITLE, DEPARTMENT, AGE, ANNUAL_SALARY, GENDER, HIRE_DATE, EXIT_DATE, BONUS_PERCENT, CITY, COUNTRY, BUSINESS_UNIT, ETHNICITY

workbook = load_workbook("..\EmployeeSampleData\EmployeeSampleData.xlsx")

""" Working with converting excel data into json """

sheet = workbook.active

employees = {}

for row in sheet.iter_rows(min_row=2, max_row=10,min_col=1, max_col=10, values_only=True):
    emp_id = row[0]
    employee = {
        "full name" : row[1],
        "job title" : row[2],
        "Annual Salary" : row[9]
    }
    employees[emp_id] = employee

with open("employees.json","w") as file_obj:
    json.dump(employees,file_obj)

""" Storing data using classes """

class Employee():

    def __init__(self,empid,fullname,job_title,department,business_unit,gender,ethinicity,age,hire_date,annual_salary,bonus_percent,country,city,exit_date):
        self.empid = empid
        self.fullname = fullname
        self.job_title = job_title
        self.department = department
        self.business_unit = business_unit
        self.gender = gender
        self.ethinicity = ethinicity
        self.age = age
        self.hire_date = hire_date
        self.annual_salary = annual_salary
        self.bonus_percent = bonus_percent
        self.country = country
        self.city = city
        self.exit_date = exit_date

employees = []

for data in sheet.iter_rows(min_row=1,max_row=3,values_only=True):
    employees.append(Employee(data[EEID],
                                data[FULLNAME],
                                data[JOB_TITLE],
                                data[DEPARTMENT],
                                data[BUSINESS_UNIT],
                                data[GENDER],
                                data[ETHNICITY],
                                data[AGE],
                                data[HIRE_DATE],
                                data[ANNUAL_SALARY],
                                data[BONUS_PERCENT],
                                data[COUNTRY],
                                data[CITY],
                                data[EXIT_DATE]))

print(employees)
