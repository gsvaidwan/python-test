# program to calculate the income tax of an employee
basic=int(input('Enter the basic salary : '))
saving=int(input('Enter the total saving made : '))
if basic<=250000:
    tax=0
elif basic <= 500000:
    if saving > 150000:
        saving=150000
    total_income=basic-saving-250000
    tax=total_income * 0.05
elif basic <= 1000000:
    if saving > 150000:
        saving = 150000
    total_income_5slab=50000-saving-250000
    total_income_20slab= 50000-saving-250000
    tax= total_income_5slab * 0.05 + total_income_20slab * 0.02
else:
    if saving > 150000:
        saving = 150000
    total_income_5slab = 50000 - saving - 250000
    total_income_30slab = basic - 1000000
    tax = total_income_5slab * 0.05 + total_income_30slab * 0.03 + 100000
print('Total income tax to be paid = ', tax)