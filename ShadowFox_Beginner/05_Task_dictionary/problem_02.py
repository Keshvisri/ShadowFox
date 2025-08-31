
# Your expenses
print("Enter your expenses:- ")
your_expenses = {
    "Hotel": int(input("Enter your hotel expense: ")),
    "Food": int(input("Enter your food expense: ")),
    "Transportation": int(input("Enter your transportation expense: ")),
    "Shopping": int(input("Enter your shopping expense: ")),
    "Miscellaneous": int(input("Enter your miscellaneous expense: "))
}

# Partner's expenses
print("\nEnter  partner's expenses:")
partner_expenses = {
    "Hotel": int(input("Enter partner's hotel expense: ")),
    "Food": int(input("Enter partner's food expense: ")),
    "Transportation": int(input("Enter partner's transportation expense: ")),
    "Shopping": int(input("Enter partner's shopping expense: ")),
    "Miscellaneous": int(input("Enter partner's miscellaneous expense: "))
}

# sum of expense of each 
your = sum(your_expenses.values())
partner = sum(partner_expenses.values())


#greater value of expense
if your > partner :
    print(f"{your} , this is largest value that i expense")
else:
    print(f"{partner} , this is largest value of my partner expense")


#expense category
print("\nYour Expenses: ", your_expenses)
print("Partner's Expenses: ", partner_expenses)


print(f'my expense {your}')
print(f'my partner expense {partner}')