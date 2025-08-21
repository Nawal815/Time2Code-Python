# Carpet cost program

# -------------------------
# Subprograms
# -------------------------
def carpet_cost(width, length, price):
    carpet = width * length * price
    underlay = width * length * 2
    grippers = width + length
    fitting = 50
    return carpet + underlay + grippers + fitting

# -------------------------
# Main program
# -------------------------
width = int(input("Enter the width of the room to the nearest meter: "))
length = int(input("Enter the length of the room to the nearest meter: "))
price = float(input("Enter the price of the carpet per m2: "))
print("The total cost is: £", carpet_cost(width, length, price))
