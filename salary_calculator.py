hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 38:
    regular_pay = 38 * rate
    overtime_hours = hours - 38
    overtime_pay = overtime_hours * rate * 1.5
    salary = regular_pay + overtime_pay
else:
    salary = hours * rate

print("Total salary:", salary)
