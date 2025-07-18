# data.py

# Simulated monthly expenses by lifestyle
SIMULATED_COSTS = {
    "Frugal": {
        "food": 30000,
        "transport": 10000,
        "rent": 40000,
        "utilities": 7000,
        "others": 5000
    },
    "Moderate": {
        "food": 50000,
        "transport": 20000,
        "rent": 70000,
        "utilities": 12000,
        "others": 10000
    },
    "Lavish": {
        "food": 90000,
        "transport": 40000,
        "rent": 150000,
        "utilities": 25000,
        "others": 20000
    }
}

# Different inflation scenarios (increase in cost)
INFLATION_SCENARIOS = {
    "Low (15%)": 0.15,
    "Medium (25%)": 0.25,
    "High (30%)": 0.30,
    "Extreme (50%)": 0.50
}

# Function to calculate adjusted expenses
def calculate_adjusted_expenses(income, lifestyle, inflation_rate):
    base_costs = SIMULATED_COSTS[lifestyle]
    adjusted_costs = {category: round(amount * (1 + inflation_rate)) for category, amount in base_costs.items()}
    total_expense = sum(adjusted_costs.values())
    balance = income - total_expense
    return adjusted_costs, total_expense, balance
