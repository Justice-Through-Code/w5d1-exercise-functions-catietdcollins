# tip_calculator.py
# TODO: Create a function named calculate_tip
try:  #DO NOT MODIFY
         def tip_calculator():
            total_cost = float(input('The cost of the meal (without tax):'))
            num_people = int(input('The number of people splitting the bill:'))
            tip_percentage = float(input('The tip percentage:'))
            tip_amount = (total_cost * tip_percentage) / 100
            sales_tax = .10
            total_bill = float(total_cost + tip_amount + (sales_tax * total_cost))
            cost_per = float(total_bill / num_people)
            print(f"Total bill: ${total_bill:.2f}")
            print(f'Each person should pay: ${cost_per:.2f}')
    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
    # NOTE: Calculate the tip and tax separately.
    # TODO:
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.
    # TODO:
        # Using an f-string, print two different statements
        # Total bill: $0.00
        # Each person should pay: $0.00
    # NOTE: The amounts are displayed with 2 decimals only
except ValueError: # TODO: modify this except to include a Built-in Exception
    # TODO: Print an statement telling the user their input is invalid
         print('Uh-oh you entered it wrong! please put numbers.')
    # We all stayed in the pod untill 9:15 collectivly pod 1
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY