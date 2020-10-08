"""
Problem 2: Basic Operations
"""

amount_deposited = float(input("How much money do you want to deposite in account? "))
annual_interest_rate = float(input("What is the annual interst rate? ")) / 100

# 1. In this question, I 

bill_toal_wealth = round(amount_deposited * ((1 + annual_interest_rate) ** 10),2)
print("Bill's total wealth is ${0}".format(bill_toal_wealth))

# 2.
current_inerest_rate = 0.05
double_money = 


