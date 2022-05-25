# The road transport corporation (RTC) of a city wants to know whether a particular bus-route 
# is running on profit or loss.

# Assume that the following information are given:
# Price per litre of fuel = 70
# Mileage of the bus in km/litre of fuel = 10
# Price(Rs) per ticket = 80

# The bus runs on multiple routes having different distance in kms and number of passengers.
# Write a function to calculate and return the profit earned (Rs) in each route. 
# Return -1 in case of loss.

def calculate(distance,no_of_passengers):
    profit_earned = 0
    fuel_price = 70
    mileage = 10
    ticket_price = 80

    fuel_refill_price = (distance/mileage) * fuel_price
    ticket_income = no_of_passengers * ticket_price

    profit_earned = ticket_income - fuel_refill_price
    if profit_earned > 0:
        return profit_earned
    else:
        return -1


#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))