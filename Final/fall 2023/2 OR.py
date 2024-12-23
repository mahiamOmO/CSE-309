class Employee:
    def __init__(self, name, age, salary):
        """
        Constructor to initialize the attributes of the employee.
        :param name: Name of the employee
        :param age: Age of the employee
        :param salary: Salary of the employee
        """
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        """
        Method to display the details of the employee.
        """
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary, bonus):
        """
        Constructor to initialize attributes for a full-time employee.
        :param name: Name of the employee
        :param age: Age of the employee
        :param salary: Salary of the employee
        :param bonus: Bonus of the employee
        """
        super().__init__(name, age, salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        """
        Method to calculate the total salary including bonus.
        :return: Total salary
        """
        return self.salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, age, salary, hours_worked):
        """
        Constructor to initialize attributes for a part-time employee.
        :param name: Name of the employee
        :param age: Age of the employee
        :param salary: Base salary of the employee
        :param hours_worked: Number of hours worked
        """
        super().__init__(name, age, salary)
        self.hours_worked = hours_worked

    def calculate_payment(self, hourly_rate):
        """
        Method to calculate the payment based on the hourly rate.
        :param hourly_rate: Rate per hour
        :return: Total payment
        """
        return self.hours_worked * hourly_rate


# Example usage:
full_time_emp = FullTimeEmployee("Alice", 28, 60000, 5000)
part_time_emp = PartTimeEmployee("Bob", 22, 0, 20)

# Display details and calculations
full_time_emp.display_details()
print(f"Total Salary with Bonus: {full_time_emp.calculate_total_salary()}")

part_time_emp.display_details()
print(f"Total Payment: {part_time_emp.calculate_payment(25)}")
