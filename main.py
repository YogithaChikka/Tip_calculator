#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? Rs "))
tip = int(input("What percentage tip would you like to give? 10, 12 0r 15?"))
number_of_people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_of_people
final_amount = round(bill_per_person, 2)
# Rounding of to two decimal places
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: Rs {final_amount}")