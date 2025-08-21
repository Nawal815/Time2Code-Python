# Temperature coverter program

# -----------------------
# Subprograms
# -----------------------
# Converting centigrade to fahrenheit
def c_to_f(centigrade):
    return (centigrade * 1.8) + 32

# -----------------------
# Main program
# -----------------------
centigrade = int(input("Enter the temperature in Centigrade: "))
fahrenheit = c_to_f(centigrade)
print(centigrade, "degrees Centigrade is", fahrenheit, "degrees Fahrenheit.")
