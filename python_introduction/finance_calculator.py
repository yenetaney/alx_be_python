monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $" , monthly_savings)
print("projected savings after one year, with interest, is:" , project_savings)
