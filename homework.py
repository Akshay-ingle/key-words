

total_bill = float(input("Enter the total bill amount: "))


amount_paid = float(input("Enter the amount paid: "))

due_amount = total_bill - amount_paid

if due_amount > 0:
    print(f"The due amount is: ${due_amount:.2f}")
elif due_amount < 0:
    print(f"Overpaid by: ${-due_amount:.2f}")
else:
    print("The bill is fully paid!")
