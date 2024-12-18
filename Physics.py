import math
FindOut = int(input("press 1 for the Viscosity formula, press 2 for the range and time to be found in mechanics, press 3 for stress to be found."))
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
    radAngle = math.radians(Angle)
    
    Initial = float(input("Whats the initial velocity? "))
    Time = (2 * Initial * math.sin(radAngle)) / GRAVITY
    Range = ((Initial**2) * math.sin(2*RadAngle)) / GRAVITY
    print(f"The time for the object is: {Time}. The range is: {Range}.")

elif FindOut==3:
    Force = float(input("Whats the Force in Newtons? "))
    CSArea = float(input("Whats the Cross Sectional area of the object? "))
    Stress = Force/CSArea
    print(f"The Stress is {Stress}pa.")
else:
    print("Invalid")
