# --- Problem Constraints & Givens ---
cost_per_hour = 0.51
total_budget = 918

# --- Calculations ---
# Hours in time frames
hours_per_day = 24
days_per_week = 7
days_per_month = 30  # Standard assumption for budgeting

# Cost Calculations
cost_per_day = cost_per_hour * hours_per_day
cost_per_week = cost_per_day * days_per_week
cost_per_month = cost_per_day * days_per_month

# Operating Days Calculation
days_with_budget = total_budget / cost_per_day

print(f"How much does it cost to operate one server per day?")
print(f"Answer: ${cost_per_day:.2f}\n")

print(f"How much does it cost to operate one server per week?")
print(f"Answer: ${cost_per_week:.2f}\n")

print(f"How much does it cost to operate one server per month?")
print(f"Answer: ${cost_per_month:.2f}\n")

print(f"How many days can I operate one server with ${total_budget}?")
print(f"Answer: {days_with_budget:.2f} days")