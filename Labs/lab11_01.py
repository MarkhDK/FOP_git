employees = {}
overtime_salary = -1.0
salary = 0.0

for i in range(0, 3):
    name = input("Type employee name: ")
    total_working_hours = int(
        input("Type the total amount of working hours for employee " + name + ": ")
    )
    salary = float(input("Type the salary for " + name + ": "))

    employees[name] = {"total_working_hours": total_working_hours, "salary": salary}

if overtime_salary < 0:
    overtime_salary = float(
        input("Type the salary increase for hours worked over 40: ")
    )

if overtime_salary > 0:
    for employee in employees:
        if employees[employee]["total_working_hours"] > 40:
            employees[employee]["salary"] = employees[employee]["salary"] * (
                overtime_salary + 1.0
            )

for employee in employees:
    print(
        employee
        + " worked "
        + str(employees[employee]["total_working_hours"])
        + " hours and earned "
        + str(employees[employee]["salary"])
        + " SEK."
    )
