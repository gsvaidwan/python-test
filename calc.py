# Write the program for calculator
#result=0
val1=float(input('Enter the Value 1 :'))
val2=float(input('Enter the Value 2 :'))
op=input('Enter the any of the operator (+,-,*,/):')
if op=='+':
    result=val1+val2
elif op=="-":
    if val1>val2:
        result=val1-val2
    else:
        result=val1-val2
elif op=="*":
    result=val1*val2
elif op=='/':
    if val2==0:
        print('Pls enter the value other than 0')
    else:
        result=val1/val2
else:
    print('Pls enter the any of the other operator (+,-,*,/)')
print("The result is :", result)