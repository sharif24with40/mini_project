print("Welcome to the tip Calculator")
#get total bill from the user
bill=float(input("What was the total bill?:$"))
#tip from user
tip=int(input("How much tip would you like to give? 10,12 or 15:"))
#how may person split the bill
people=int(input("How many people to split the bill? "))
# clacluate total tip with bill
total_tip=bill*(1+(tip/100))
#total amount split by the each person
amount_per_person=total_tip/people
'final output'
final_amount="{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${final_amount}")