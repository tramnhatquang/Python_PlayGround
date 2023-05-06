# round the result to 2 decimal places
print("Welcome to the tip calculator!")
bill = float(input("How much is your bill? $"))

tip = int(input("How much tip percentage would you like to give? 10, 12, or 15?"))

people = int(input("How many people do you want to split the bill?"))

tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

# print out the total amount
print(f"Each person should pay {final_amount} dollars")
