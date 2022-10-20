from operator import sub


salary = float(input("Salary: "))
employee = int(input("Employees: "))
subsidy = salary * 0.2
tax = salary * 0.1
net_salary = (salary - tax) + subsidy
outgo = net_salary * employee
print("Subsidy: Rp.", subsidy)
print("Tax: Rp.", tax)
print("NET Salary: Rp.", net_salary)
print("Total Outgo: Rp.",outgo)
