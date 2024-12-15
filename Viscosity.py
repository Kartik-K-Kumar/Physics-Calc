import math
Mass = float(input("Whats the mass of the steel ball? "))
GRAVITY = 9.81
Radius = float(input("Whats the Radius of the steel ball? "))
Density = 1260
Velocity = float(input("Whats the terminal velocity? "))
pi = math.pi

Weight = Mass*GRAVITY
SphereVolume = (4/3) * Radius**3
Denominator = 6*pi*Radius*Velocity
Visc = (Weight - SphereVolume * GRAVITY * Density) / Denominator
print(Visc)