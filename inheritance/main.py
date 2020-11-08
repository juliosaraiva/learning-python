import hr
import employees
import productivity

manager = employees.Manager(1, 'Julio Saraiva', 3000)
secretary = employees.Secretary(2, 'Wirllane Borges', 2000)
sales_guy = employees.SalesPerson(3, 'Pedro Augusto', 1000, 250)
factory_worker = employees.FactoryWorker(4, 'Alura Mac', 20, 15)
temporary_secretary = employees.TemporarySecretary(5, 'Denisse Stephan', 40, 9)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary
]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
