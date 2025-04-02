# TIP CALCULATOR
bill = input("Enter the the bill amount: ")
tip_per = input("Enter tip percentage 10, 12 or 15: ")
tip = float(bill) * (int(tip_per)/100)
people = input("Enter number of people: ")
result = (float(bill) + float(tip))/ int(people)
fnl_amt = "{:.2f}".format(result) 
print(f"Each person should pay {fnl_amt}")
