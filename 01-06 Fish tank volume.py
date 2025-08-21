# Fish tank volume problem

# -------------------------
# Subprograms
# -------------------------
# Calculating the volume of the water
def volume(length, width, height):
    return(length * width * height) / 1000

# Converting litres to gallons
def litres_to_gallons(litres):
    return litres / 4.546

# -------------------------
# Main program
# -------------------------
length = int(input("Enter the length of the fish tank in centimeters: ")) # Centimeters
width = int(input("Enter the width of the fish tank in centimeters: ")) # Centimeters
height = int(input("Enter the height of the fish tank in centimeters: ")) # Centimeters
litres = volume(length, width, height)
gallons = litres_to_gallons(litres)
print("A", length, "x", width, "x", height, "cm tank is", litres, "litres and", gallons, "imperial gallons.")
