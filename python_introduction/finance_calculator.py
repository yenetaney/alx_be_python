user_income = int(input("Enter your monthly income$: "))
user_expenses = int(input("Enter your total monthly expenses$: "))
monthly_savings =  user_income - user_expenses
project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $" , monthly_savings)
print("projected savings after one year, with interest, is:$" , project_savings)
