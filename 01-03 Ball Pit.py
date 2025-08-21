# Ball pit program

# -----------------------
# Subprograms
# -----------------------
#Function to return the volume of the ball pit
def ball_pit_volume(ball_pit_radius, ball_pit_height):
    pi = 3.14
    return pi * (ball_pit_radius * ball_pit_radius) * ball_pit_height


#Function to return the volume of a ball
def ball_volume(ball_radius):
    pi = 3.14
    return (4 / 3) * pi * (ball_radius * ball_radius * ball_radius)


# -----------------------
# Main program
# -----------------------
ball_pit_radius = float(input("What is the radius of the ball pit in metres?")) # Meters
ball_pit_height = float(input("What is the height of the ball pit in metres?")) # Meters
ball_radius = float(input("What is the radius of one ball in meters?")) # Meters
packing_density = 0.75 # Volume taken up by the balls
balls = int(((ball_pit_volume(ball_pit_radius, ball_pit_height) / ball_volume(ball_radius)) * packing_density)+1)
print("You need", balls, "balls to fill the ball pit.")

