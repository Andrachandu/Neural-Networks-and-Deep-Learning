class Employee:
    employee_count = 0

    def _init_(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Family: {self.family}, Salary: {self.salary}, Department: {self.department}")

    @staticmethod
    def average_salary(salary_list):
        return sum(salary_list) / len(salary_list) if len(salary_list) > 0 else 0


class FulltimeEmployee(Employee):
    def _init_(self, name, family, salary, department, hours_worked):
        super()._init_(name, family, salary, department)
        self.hours_worked = hours_worked

    def display_employee_info(self):
        super().display_employee_info()
        print(f"Hours Worked: {self.hours_worked}")


# Create instances of Employee and FulltimeEmployee classes
employee1 = Employee("John Doe", "Doe Family", 50000, "HR")
employee2 = Employee("Jane Doe", "Doe Family", 60000, "Finance")

fulltime_employee = FulltimeEmployee("Alice Smith", "Smith Family", 70000, "IT", 40)

# Call member functions
employee1.display_employee_info()
employee2.display_employee_info()

# Create a list of salaries for averaging
salaries = [employee1.salary, employee2.salary, fulltime_employee.salary]

# Call the average_salary function
average_salary = Employee.average_salary(salaries)
print(f"Average Salary: {average_salary}")

# Call the display_employee_info function of FulltimeEmployee
fulltime_employee.display_employee_info()