from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDatabase


employee_database = EmployeeDatabase()
employees = employee_database.employees
ProductivitySystem().track(employees, 40)
PayrollSystem().calculate_payroll(employees)
