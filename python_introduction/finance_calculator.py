monthly_income =int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your monthly expenses"))

monthly_savings = monthly_income - monthly_expenses

print(f"Projected Savings after one year, with interest = {monthly_savings * 12 + monthly_savings * 12 * 0.05}).")  