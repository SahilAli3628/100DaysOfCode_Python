print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What % tip would you like to give (10, 12, 15)? "))
people = int(input("How many people to split the bill? "))

tip_amount = (tip/100) * bill
share = (tip_amount + bill) / people
share = round(share, 2)
print(f"Each person's share: {share}")
