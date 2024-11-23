# Simple program to calculate due amount
total_bill = float(input("Enter the total bill amount: $"))
payment_amount = float(input("Enter the payment amount: $"))

# Calculate the due amount
due_amount = total_bill - payment_amount

# Display the result
if due_amount > 0:
    print(f"The customer still owes ${due_amount:.2f}.")
elif due_amount == 0:
    print("The bill is fully paid.")
else:
    print(f"The customer has overpaid by ${-due_amount:.2f}.")
