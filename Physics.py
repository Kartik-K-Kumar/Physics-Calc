import math
FindOut = int(input("press 1 for the Viscosity formula, press 2 for the time to be found in mechanics"))
GRAVITY = 9.81
pi = math.pi

if FindOut==1:
    Mass = float(input("Whats the mass of the steel ball? "))
    Radius = float(input("Whats the Radius of the steel ball? "))
    Density = 1260
    Velocity = float(input("Whats the terminal velocity? "))
    

    Weight = Mass*GRAVITY
    SphereVolume = (4/3) * Radius**3
    Denominator = 6*pi*Radius*Velocity
    Visc = (Weight - SphereVolume * GRAVITY * Density) / Denominator
    print(Visc)
elif FindOut==2:
    Angle = float(input("Whats the angle to the horizontal? "))
    Initial = float(input("Whats the initial velocity? "))
    formula = (2 * Initial * math.sin(Angle)) / GRAVITY
    print("the time taken for the object from start to the end of its journey for it travelling is: " + str(formula))
else:
    print("Invalid")
