import numpy as np
from scipy.optimize import fsolve

'''In triangle ABC, three Cevians AD, BE, and CF are concurrent if and only if the following identity holds:

    (AF / FB) * (BD / DC) * (CE / EA) = 1.

The theorem also has a lesser-known trigonometric form:

    (sin(∠ABE) / sin(∠CBE)) * (sin(∠BCF) / sin(∠ACF)) *  (sin(∠CAD) / sin(∠BAD)) = 1,

or equivalently,

    sin(∠ABE) * sin(∠BCF) * sin(∠CAD) = sin(∠CBE) * sin(∠ACF) * sin(∠BAD).

This code solves for an unknown angle in the trigonometric Ceva equation.
''' 

def equation(x, a1, a2, b1, b2, b3):
    
    x_rad = np.radians(x)
    return np.sin(np.radians(a1)) * np.sin(np.radians(a2)) * np.sin(x_rad) - np.sin(np.radians(b1)) * np.sin(np.radians(b2)) * np.sin(np.radians(b3 - x))
    
print(f"This code is for solving the Trigonometric Ceva theorem in triangles. For example:\nsin(10) * sin(26) * sin(x) = sin(22) * sin(24) * sin(98 - x)\nTo solve an equation like this, enter the values in order: 10, 26, 22, 24, 98.\n")

a1 = float(input("1st angle (degrees): "))
a2 = float(input("2nd angle (degrees): "))
b1 = float(input("4th angle (degrees): "))
b2 = float(input("5th angle (degrees): "))
b3 = float(input("6th angle (degrees): "))

x_initial_guess = 37

x_solution = fsolve(equation, x_initial_guess, args=(a1, a2, b1, b2, b3))

print(f"\nx = {x_solution[0]:.3f} degrees")
