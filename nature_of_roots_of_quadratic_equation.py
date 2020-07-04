"""Python program to chaeck nature of roots of a quadratic equation """
import math
a = int(input("Enter the value of a in quadratic equation : "))
b = int(input("Enter the value of b in quadratic equation : "))
c = int(input("Enter the value of c in quadratic equation : "))
discriminant = (b**2)-(4*a*c)
if(discriminant > 0):
    root1 = (-b + math.sqrt(discriminant)/ (2*a))
    root2 = (-b - math.sqrt(discriminant)/ (2*a))
    print("Two Discriminant Real ROOts Exits : root1 = %.2f and root = %.2f " %(root1,root2))
elif (discriminant==0):
    root1 = root2 = -b / (2*a)
    print("Two Discriminant Real ROOts Exits : root1 = %.2f and root = %.2f " %(root1,root2))
elif (discriminant<0):
    root1= root2 = -b / (2*a)
    imaginary = math.sqrt(-discriminant) / (2*a)
    print("Two Discriminant Real ROOts Exits : root1 = %.2f + %.2f and root = %.2f - %.2f " %(root1,imaginary, root2, imaginary))
