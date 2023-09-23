# Using the input to get the exchange rate from the user/client.
# wrapping the input value in a float, because we are dealing with currency values, not to lose value.
# Storing the user exchange rate in a variable exchange_rate.
exchange_rate = float(input("Enter the exchange rate (your local currency per dollar): "))

# Geting the amount in dollars from the user/client.
# Storing it in a variable called dollars.
dollars = float(input("Enter the amount in dollars: "))

# Calculating the equivalent amount in local currency.
# formular is the dollars multiplied by the exchange_rate.
# Stored in a variable exchange_rate
local_currency = dollars * exchange_rate

# Display the result usint print()
# passing the variables dollar and local_currency in the String function.
print(f"{dollars} dollars is equal to {local_currency} in local currency.")
print(f"Calculation done...");
